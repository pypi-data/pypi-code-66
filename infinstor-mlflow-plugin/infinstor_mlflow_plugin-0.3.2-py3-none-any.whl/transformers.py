"""
The ``mlflow.sklearn`` module provides an API for logging and loading scikit-learn models. This
module exports scikit-learn models with the following flavors:

Python (native) `pickle <https://scikit-learn.org/stable/modules/model_persistence.html>`_ format
    This is the main flavor that can be loaded back into scikit-learn.

:py:mod:`mlflow.pyfunc`
    Produced for use by generic pyfunc-based deployment tools and batch inference.
"""

from __future__ import absolute_import

import math
import os
from multiprocessing import Pool
import torch
import yaml
import transformers
from tensorboardX import SummaryWriter
from tqdm import tqdm, trange
from transformers import BertConfig, BertForSequenceClassification, BertTokenizer, XLNetConfig, \
    XLNetForSequenceClassification, XLNetTokenizer, XLMConfig, XLMForSequenceClassification, XLMTokenizer, \
    RobertaConfig, RobertaForSequenceClassification, RobertaTokenizer, DistilBertConfig, \
    DistilBertForSequenceClassification, DistilBertTokenizer, InputExample, InputFeatures, \
    get_linear_schedule_with_warmup, AdamW
from transformers import glue_compute_metrics as compute_metrics
from transformers import glue_processors as processors
from transformers import glue_output_modes as output_modes
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler, TensorDataset
from torch.utils.data.distributed import DistributedSampler
import numpy as np

import mlflow
from mlflow import pyfunc
from mlflow.exceptions import MlflowException
from mlflow.models import Model
from mlflow.protos.databricks_pb2 import RESOURCE_ALREADY_EXISTS
from mlflow.tracking.artifact_utils import _download_artifact_from_uri
from mlflow.utils.environment import _mlflow_conda_env
from mlflow.utils.model_utils import _get_flavor_configuration
from sklearn.metrics import accuracy_score, matthews_corrcoef, confusion_matrix, \
    label_ranking_average_precision_score

from mlflow.utils.file_utils import TempDir
from infinstor_mlflow_plugin import transformers as infinstor_transformers

FLAVOR_NAME = "transformers"

MODEL_CLASSES = {
    'bert': (BertConfig, BertForSequenceClassification, BertTokenizer, 'bert-base-uncased'),
    'xlnet': (XLNetConfig, XLNetForSequenceClassification, XLNetTokenizer, 'xlnet-base-cased'),
    'xlm': (XLMConfig, XLMForSequenceClassification, XLMTokenizer, 'xlm-mlm-enfr-1024'),
    'roberta': (RobertaConfig, RobertaForSequenceClassification, RobertaTokenizer, 'distilbert-base-uncased'),
    'distilbert': (DistilBertConfig, DistilBertForSequenceClassification, DistilBertTokenizer, 'roberta-base'),
}

SERIALIZATION_FORMAT_PICKLE = "pickle"
SERIALIZATION_FORMAT_CLOUDPICKLE = "cloudpickle"

SUPPORTED_SERIALIZATION_FORMATS = [
    SERIALIZATION_FORMAT_PICKLE,
    SERIALIZATION_FORMAT_CLOUDPICKLE
]


def get_default_conda_env(include_cloudpickle=False):
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`.
    """
    pip_deps = None
    if include_cloudpickle:
        import cloudpickle
        pip_deps = ["cloudpickle=={}".format(cloudpickle.__version__)]
    return _mlflow_conda_env(
        additional_conda_deps=[
            "transformers={}".format(transformers.__version__),
        ],
        additional_pip_deps=pip_deps,
        additional_conda_channels=None
    )


def save_model(transformers_model, tokenizer, path, conda_env=None, mlflow_model=Model()):
    """
    Save a scikit-learn model to a path on the local file system.

    :param transformers_model: scikit-learn model to be saved.
    :param path: Local path where the model is to be saved.
    :param conda_env: Either a dictionary representation of a Conda environment or the path to a
                      Conda environment yaml file. If provided, this decsribes the environment
                      this model should be run in. At minimum, it should specify the dependencies
                      contained in :func:`get_default_conda_env()`. If `None`, the default
                      :func:`get_default_conda_env()` environment is added to the model.
                      The following is an *example* dictionary representation of a Conda
                      environment::

                        {
                            'name': 'mlflow-env',
                            'channels': ['defaults'],
                            'dependencies': [
                                'python=3.7.0',
                                'scikit-learn=0.19.2'
                            ]
                        }

    :param mlflow_model: :py:mod:`mlflow.models.Model` this flavor is being added to.
    :param tokenizer: tokenizer
    """
    if os.path.exists(path):
        raise MlflowException(message="Path '{}' already exists".format(path),
                              error_code=RESOURCE_ALREADY_EXISTS)
    os.makedirs(path)
    model_data_subpath = ""
    _save_model(transformers_model, tokenizer, model_path=os.path.join(path, model_data_subpath))
    conda_env_subpath = "conda.yaml"
    if conda_env is None:
        conda_env = get_default_conda_env(
            include_cloudpickle=SERIALIZATION_FORMAT_CLOUDPICKLE == SERIALIZATION_FORMAT_CLOUDPICKLE)
    elif not isinstance(conda_env, dict):
        with open(conda_env, "r") as f:
            conda_env = yaml.safe_load(f)
    with open(os.path.join(path, conda_env_subpath), "w") as f:
        yaml.safe_dump(conda_env, stream=f, default_flow_style=False)
    pyfunc.add_to_model(mlflow_model, loader_module="infinstor_mlflow_plugin.transformers", data=model_data_subpath,
                        env=conda_env_subpath)
    mlflow_model.add_flavor(FLAVOR_NAME,
                            pickled_model=model_data_subpath,
                            transformers_version=transformers.__version__)
    mlflow_model.save(os.path.join(path, "MLmodel"))


def log_model(transformers_model, tokenizer, conda_env=None):
    return transformers_log(artifact_path='infinstor/model',
                                  transformers_model=transformers_model,
                                  tokenizer=tokenizer,
                                  flavor=infinstor_transformers,
                                  registered_model_name=None,
                                  conda_env=conda_env)

def transformers_log(artifact_path, transformers_model, tokenizer, flavor, registered_model_name=None,
                     **kwargs):
    """
    Log model using supplied flavor module. If no run is active, this method will create a new
    active run.

    :param artifact_path: Run relative path identifying the model.
    :param transformers_model: The transformers model to log.
    :param tokenizer: The tokenizer to log.
    :param flavor: Flavor module to save the model with. The module must have
                   the ``save_model`` function that will persist the model as a valid
                   MLflow model.
    :param registered_model_name: Note:: Experimental: This argument may change or be removed
                                  in a future release without warning. If given, create a model
                                  version under ``registered_model_name``, also creating a
                                  registered model if one with the given name does not exist.
    :param kwargs: Extra args passed to the model flavor.
    """
    with TempDir() as tmp:
        local_path = tmp.path("model")
        save_model(transformers_model, tokenizer, local_path, None, Model())
        mlflow.tracking.fluent.log_artifacts(local_path, artifact_path)
        if registered_model_name is not None:
            run_id = mlflow.tracking.fluent.active_run().info.run_id
            mlflow.register_model("runs:/%s/%s" % (run_id, artifact_path),
                                  registered_model_name)

def _load_model_from_local_file(model_type, model_path):
    """Load a scikit-learn model saved as an MLflow artifact on the local file system."""
    config_class, model_class, tokenizer_class, _ = MODEL_CLASSES[model_type]
    config = config_class.from_pretrained(model_path)
    tokenizer = tokenizer_class.from_pretrained(model_path)
    model = model_class.from_pretrained(model_path, config=config)
    return model, tokenizer, config


def _load_pyfunc(path):
    """
    Load PyFunc implementation. Called by ``pyfunc.load_pyfunc``.

    :param path: Local filesystem path to the MLflow Model with the ``transformers`` flavor.
    """
    return _transformer_load_pyfunc(path)


def _transformer_load_pyfunc(path, model_type=None):
    if not model_type:
        model_type = "bert"
    return _load_model_from_local_file(model_type, path)


def _save_model(transformers_model, tokenizer, model_path):
    """
    :param transformers_model: The scikit-learn model to serialize.
    :param model_path: The file path to which to write the serialized model.
    :param tokenizer: Tokenizer to save.
    """
    transformers_model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)


def load_model(model_type, model_uri=None):
    """
    Load a transformer-learn model from a local file or a run.
    :param model_type: The type of transformer model we are using
    :param model_uri: The location, in URI format, of the MLflow model, for example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.

    :return: A transformers-learn model.
    """
    run_id = mlflow.tracking.fluent._get_or_start_run().info.run_id
    model_save_dir = os.path.join("runs:/", run_id)
    model_save_dir = os.path.join(model_save_dir, "model")
    if not model_uri:
        local_model_path = _download_artifact_from_uri(artifact_uri=model_save_dir)
    else:
        local_model_path = _download_artifact_from_uri(artifact_uri=model_uri)
    flavor_conf = _get_flavor_configuration(model_path=local_model_path, flavor_name=FLAVOR_NAME)
    transformers_model_artifacts_path = os.path.join(local_model_path, flavor_conf['pickled_model'])
    return _load_model_from_local_file(model_type=model_type, model_path=transformers_model_artifacts_path)


class _TransformersModelWrapper:
    def __init__(self, transformers_model):
        self.model = transformers_model[0]
        self._tokenizer = transformers_model[1]
        self._config = transformers_model[2]
        self.results = {}
        if self.args['local_rank'] == -1 or self.args['no_cuda']:
            device = torch.device("cuda" if torch.cuda.is_available() and not self.args['no_cuda'] else "cpu")
        else:  # Initializes the distributed backend which will take care of sychronizing nodes/GPUs
            torch.cuda.set_device(self.args['local_rank'])
            device = torch.device("cuda", self.args['local_rank'])
            torch.distributed.init_process_group(backend="nccl")
        self.args = {'silent': False,
                     'local_rank': -1,
                     'max_seq_length': 128,
                     'no_cuda': True,
                     'overwrite_cache': True,
                     'num_labels': self._config.to_dict['num_labels'],
                     'use_topK': True,
                     'weight': None,
                     # change this
                     'output_dir': 'outputs/',
                     'cache_dir': 'cache_dir/',
                     'fp16': False,
                     'fp16_opt_level': 'O1',
                     'train_batch_size': 8,
                     'gradient_accumulation_steps': 1,
                     'eval_batch_size': 8,
                     'num_train_epochs': 1,
                     'weight_decay': 0,
                     'learning_rate': 4e-5,
                     'adam_epsilon': 1e-8,
                     'warmup_ratio': 0.06,
                     'warmup_steps': 0,
                     'max_grad_norm': 1.0,
                     'no_cache': False,
                     'logging_steps': 500,
                     'save_steps': 2000,
                     'evaluate_during_training': False,
                     'device': device,
                     'overwrite_output_dir': False,
                     'reprocess_input_data': False,

                     'process_count': 1,
                     'n_gpu': 1,
                     'use_multiprocessing': True}

    def accuracy_topK(self, output, target, topk=None):
        """
        Computes the precision@k for the specified values of k
        Args:

        """
        if not topk:
            topk = self._config.to_dict()['top_k']
        topk_range = range(1, topk + 1)
        maxk = max(topk_range)
        batch_size = output.shape[0]
        output = torch.from_numpy(output)
        target = torch.from_numpy(target)

        _, pred = output.topk(maxk, 1, True, True)
        pred = pred.t()
        correct = pred.eq(target.view(1, -1).expand_as(pred))

        res = []
        for k in topk_range:
            correct_k = correct[:k].view(-1).float().sum(0, keepdim=True)
            res.append(correct_k.mul_(100.0 / batch_size))
        return res

    def train_model(self, train_df, output_dir=None, show_running_loss=True, args=None, eval_df=None):
        """
        Trains the model using 'train_df'
        Args:
            train_df: Pandas Dataframe containing at least two columns. If the Dataframe has a header, it should contain a 'text' and a 'labels' column. If no header is present,
            the Dataframe should contain at least two columns, with the first column containing the text, and the second column containing the label. The model will be trained on this Dataframe.
            output_dir: The directory where model files will be saved. If not given, self.args['output_dir'] will be used.
            show_running_loss (optional): Set to False to prevent running loss from being printed to console. Defaults to True.
            args (optional): Optional changes to the args dict of the model. Any changes made will persist for the model.
            eval_df (optional): A DataFrame against which evaluation will be performed when evaluate_during_training is enabled. Is required if evaluate_during_training is enabled.
        Returns:
            None
        """

        if args:
            self.args.update(args)

        if self.args['silent']:
            show_running_loss = False

        if self.args['evaluate_during_training'] and eval_df is None:
            raise ValueError(
                """evaluate_during_training is enabled but eval_df is not specified. 
                Pass eval_df to model.train_model() if using evaluate_during_training.""")

        if not output_dir:
            output_dir = self.args['output_dir']

        if os.path.exists(output_dir) and os.listdir(output_dir) and not self.args["overwrite_output_dir"]:
            raise ValueError(
                "Output directory ({}) already exists and is not empty. Use --overwrite_output_dir to overcome.".format(
                    output_dir))

        self._move_model_to_device()

        if 'text' in train_df.columns and 'labels' in train_df.columns:
            train_examples = [InputExample(i, text, None, label) for i, (text, label) in
                              enumerate(zip(train_df['text'], train_df['labels']))]
        else:
            train_examples = [InputExample(i, text, None, label) for i, (text, label) in
                              enumerate(zip(train_df.iloc[:, 0], train_df.iloc[:, 1]))]

        train_dataset = self.load_and_cache_examples(train_examples, no_cache=self.args['no_cache'])
        global_step, tr_loss = self.train(train_dataset, output_dir, show_running_loss=show_running_loss,
                                          eval_df=eval_df)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        model_to_save = self.model.module if hasattr(self.model, "module") else self.model
        model_to_save.save_pretrained(output_dir)
        self._tokenizer.save_pretrained(output_dir)
        torch.save(self.args, os.path.join(output_dir, "training_args.bin"))

        print("Training of {} model complete. Saved to {}.".format(self.args["model_type"], output_dir))

    def train(self, train_dataset, output_dir, show_running_loss=False, eval_df=None):
        """
        Trains the model on train_dataset.
        Utility function to be used by the train_model() method. Not intended to be used directly.
        """

        tokenizer = self._tokenizer
        model = self.model
        args = self.args
        device = args['device']

        tb_writer = SummaryWriter()
        train_sampler = RandomSampler(train_dataset)
        train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=args["train_batch_size"])

        t_total = len(train_dataloader) // args["gradient_accumulation_steps"] * args["num_train_epochs"]

        no_decay = ["bias", "LayerNorm.weight"]
        optimizer_grouped_parameters = [
            {"params": [p for n, p in model.named_parameters() if not any(
                nd in n for nd in no_decay)], "weight_decay": args["weight_decay"]},
            {"params": [p for n, p in model.named_parameters() if any(
                nd in n for nd in no_decay)], "weight_decay": 0.0}
        ]

        warmup_steps = math.ceil(t_total * args["warmup_ratio"])
        args["warmup_steps"] = warmup_steps if args["warmup_steps"] == 0 else args["warmup_steps"]

        optimizer = AdamW(optimizer_grouped_parameters, lr=args["learning_rate"], eps=args["adam_epsilon"])
        scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=args["warmup_steps"],
                                                    num_training_steps=t_total)

        if args["fp16"]:
            try:
                from apex import amp
            except ImportError:
                raise ImportError(
                    "Please install apex from https://www.github.com/nvidia/apex to use fp16 training.")

            model, optimizer = amp.initialize(model, optimizer, opt_level=args["fp16_opt_level"])

        if args["n_gpu"] > 1:
            model = torch.nn.DataParallel(model)

        global_step = 0
        tr_loss, logging_loss = 0.0, 0.0
        model.zero_grad()
        train_iterator = trange(int(args["num_train_epochs"]), desc="Epoch", disable=args['silent'])

        model.train()
        for epoch_no in train_iterator:
            print("epoch_no:", epoch_no + 1)
            # epoch_iterator = tqdm(train_dataloader, desc="Iteration")
            for step, batch in enumerate(tqdm(train_dataloader, desc="Current iteration", disable=args['silent'])):
                batch = tuple(t.to(device) for t in batch)

                inputs = self._get_inputs_dict(batch)
                outputs = model(**inputs)

                # model outputs are always tuple in pytorch-transformers (see doc)
                loss = outputs[0]
                if show_running_loss:
                    print("\rRunning loss:", loss[0], end="")

                if args['n_gpu'] > 1:
                    loss = loss.mean()  # mean() to average on multi-gpu parallel training
                if args["gradient_accumulation_steps"] > 1:
                    loss = loss / args["gradient_accumulation_steps"]

                if args["fp16"]:
                    with amp.scale_loss(loss, optimizer) as scaled_loss:
                        scaled_loss.backward()
                    torch.nn.utils.clip_grad_norm_(amp.master_params(optimizer), args["max_grad_norm"])
                else:
                    loss.backward()
                    torch.nn.utils.clip_grad_norm_(model.parameters(), args["max_grad_norm"])

                tr_loss += loss.item()
                if (step + 1) % args["gradient_accumulation_steps"] == 0:
                    optimizer.step()
                    scheduler.step()  # Update learning rate schedule
                    model.zero_grad()
                    global_step += 1

                    if args["logging_steps"] > 0 and global_step % args["logging_steps"] == 0:
                        # Log metrics
                        if args['evaluate_during_training']:
                            # Only evaluate when single GPU otherwise metrics may not average well
                            results, _, _ = self.eval_model(eval_df, verbose=True)
                            for key, value in results.items():
                                tb_writer.add_scalar('eval_{}'.format(key), value, global_step)
                        tb_writer.add_scalar("lr", scheduler.get_lr()[0], global_step)
                        tb_writer.add_scalar("loss", (tr_loss - logging_loss) / args["logging_steps"], global_step)
                        logging_loss = tr_loss

                    if args["save_steps"] > 0 and global_step % args["save_steps"] == 0:
                        # Save model checkpoint
                        output_dir_current = os.path.join(output_dir, "checkpoint-{}".format(global_step))

                        if not os.path.exists(output_dir_current):
                            os.makedirs(output_dir_current)

                        # Take care of distributed/parallel training
                        model_to_save = model.module if hasattr(model, "module") else model
                        model_to_save.save_pretrained(output_dir_current)
                        self._tokenizer.save_pretrained(output_dir_current)

        return global_step, tr_loss / global_step

    def eval_model(self, eval_df, multi_label=False, output_dir=None, verbose=False, **kwargs):
        """
        Evaluates the model on eval_df. Saves results to output_dir.
        Args:
            eval_df: Pandas Dataframe containing at least two columns. If the Dataframe has a header, it should contain
             a 'text' and a 'labels' column. If no header is present,
            the Dataframe should contain at least two columns, with the first column containing the text, and the second
             column containing the label. The model will be evaluated on this Dataframe.
            multi_label: Whether or not there are multiple labels
            output_dir: The directory where model files will be saved. If not given, self.args['output_dir']
             will be used.
            verbose: If verbose, results will be printed to the console on completion of evaluation.
            **kwargs: Additional metrics that should be used. Pass in the metrics as keyword arguments (name of metric:
             function to use). E.g. f1=sklearn.metrics.f1_score.
                        A metric function should take in two parameters. The first parameter will be the true labels,
                         and the second parameter will be the predictions.
        Returns:
            result: Dictionary containing evaluation results. (Matthews correlation coefficient, tp, tn, fp, fn)
            model_outputs: List of model outputs for each row in eval_df
            wrong_preds: List of InputExample objects corresponding to each incorrect prediction by the model
        """

        if not output_dir:
            output_dir = self.args["output_dir"]

        self._move_model_to_device()

        result, model_outputs, wrong_preds = self.evaluate(eval_df, output_dir, multi_label=multi_label, **kwargs)
        self.results.update(result)

        if verbose:
            print(self.results)

        return result, model_outputs, wrong_preds

    def evaluate(self, eval_df, output_dir, multi_label=False, use_topK=False, prefix="", **kwargs):
        """
        Evaluates the model on eval_df.
        Utility function to be used by the eval_model() method. Not intended to be used directly.
        """

        tokenizer = self._tokenizer
        model = self.model
        args = self.args
        device = args['device']
        eval_output_dir = output_dir

        results = {}

        if 'text' in eval_df.columns and 'labels' in eval_df.columns:
            eval_examples = [InputExample(i, text, None, label) for i, (text, label) in
                             enumerate(zip(eval_df['text'], eval_df['labels']))]
        else:
            eval_examples = [InputExample(i, text, None, label) for i, (text, label) in
                             enumerate(zip(eval_df.iloc[:, 0], eval_df.iloc[:, 1]))]

        eval_dataset = self.load_and_cache_examples(eval_examples, evaluate=True)
        if not os.path.exists(eval_output_dir):
            os.makedirs(eval_output_dir)

        eval_sampler = SequentialSampler(eval_dataset)
        eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=args["eval_batch_size"])

        eval_loss = 0.0
        nb_eval_steps = 0
        preds = None
        out_label_ids = None
        model.eval()

        for batch in tqdm(eval_dataloader, disable=args['silent']):
            batch = tuple(t.to(device) for t in batch)

            with torch.no_grad():
                inputs = self._get_inputs_dict(batch)

                outputs = model(**inputs)
                tmp_eval_loss, logits = outputs[:2]

                if multi_label:
                    logits = logits.sigmoid()
                eval_loss += tmp_eval_loss.mean().item()

            nb_eval_steps += 1

            if preds is None:
                preds = logits.detach().cpu().numpy()
                out_label_ids = inputs["labels"].detach().cpu().numpy()
            else:
                preds = np.append(preds, logits.detach().cpu().numpy(), axis=0)
                out_label_ids = np.append(
                    out_label_ids, inputs["labels"].detach().cpu().numpy(), axis=0)

        eval_loss = eval_loss / nb_eval_steps
        model_outputs = preds

        #         print("out_label_ids:", out_label_ids, "preds:", preds)
        #         print("out_label_ids.shape:", out_label_ids.shape, "preds.shape:", preds.shape)

        acc_topk = self.accuracy_topK(preds, out_label_ids, topk=5)
        if use_topK:
            for i, acc_score in enumerate(acc_topk):
                key = "acc_top" + str(i + 1)
                results.update({key: acc_topk[i]})
        else:
            key = "acc_top" + str(1)
            results.update({key: acc_topk[0]})

        if not multi_label:
            preds = np.argmax(preds, axis=1)

        result, wrong = self.compute_metrics(preds, out_label_ids, eval_examples, **kwargs)
        result['eval_loss'] = eval_loss
        results.update(result)

        output_eval_file = os.path.join(eval_output_dir, "eval_results.txt")
        with open(output_eval_file, "w") as writer:
            for key in sorted(result.keys()):
                writer.write("{} = {}\n".format(key, str(result[key])))

        return results, model_outputs, wrong

    def predict(self, to_predict, multi_label=False):
        """
        Performs predictions on a list of text.
        Args:
            multi_label: Whether or not there are multiple labels
            to_predict: A python list of text (str) to be sent to the model for prediction.
        Returns:
            preds: A python list of the predictions (0 or 1) for each text.
            model_outputs: A python list of the raw model outputs for each text.
        """

        tokenizer = self._tokenizer
        model = self.model
        args = self.args
        device = args['device']
        self._move_model_to_device()

        if multi_label:
            eval_examples = [InputExample(i, text, None, [0 for i in range(self.num_labels)]) for i, text in
                             enumerate(to_predict)]
        else:
            eval_examples = [InputExample(i, text, None, 0) for i, text in enumerate(to_predict)]

        eval_dataset = self.load_and_cache_examples(eval_examples, evaluate=True, multi_label=multi_label,
                                                    no_cache=True)

        eval_sampler = SequentialSampler(eval_dataset)
        eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=args["eval_batch_size"])

        eval_loss = 0.0
        nb_eval_steps = 0
        preds = None
        out_label_ids = None

        for batch in tqdm(eval_dataloader, disable=args['silent']):
            model.eval()
            batch = tuple(t.to(device) for t in batch)

            with torch.no_grad():
                inputs = self._get_inputs_dict(batch)
                outputs = model(**inputs)
                tmp_eval_loss, logits = outputs[:2]

                if multi_label:
                    logits = logits.sigmoid()

                eval_loss += tmp_eval_loss.mean().item()

            nb_eval_steps += 1

            if preds is None:
                preds = logits.detach().cpu().numpy()
                out_label_ids = inputs["labels"].detach().cpu().numpy()
            else:
                preds = np.append(preds, logits.detach().cpu().numpy(), axis=0)
                out_label_ids = np.append(out_label_ids, inputs["labels"].detach().cpu().numpy(), axis=0)

        eval_loss = eval_loss / nb_eval_steps
        model_outputs = preds
        if multi_label:
            if isinstance(args['threshold'], list):
                threshold_values = args['threshold']
                preds = [[self._threshold(pred, threshold_values[i]) for i, pred in enumerate(example)] for example in
                         preds]
            else:
                preds = [[self._threshold(pred, args['threshold']) for pred in example] for example in preds]
        else:
            preds = np.argmax(preds, axis=1)

        return preds, model_outputs

    def load_and_cache_examples(self, examples, evaluate=False,
                                no_cache=False, multi_label=False):
        """
        Converts a list of InputExample objects to a TensorDataset containing InputFeatures. Caches the InputFeatures.
        Utility function for train() and eval() methods. Not intended to be used directly.
        """

        process_count = self.args["process_count"]

        tokenizer = self._tokenizer
        output_mode = "classification"
        args = self.args

        if not os.path.isdir(self.args["cache_dir"]):
            os.mkdir(self.args["cache_dir"])

        mode = "dev" if evaluate else "train"
        cached_features_file = os.path.join(args["cache_dir"], "cached_{}_{}_{}_{}_{}".format(mode, args["model_type"],
                                                                                              args["max_seq_length"],
                                                                                              args['num_labels'],
                                                                                              len(examples)))

        if os.path.exists(cached_features_file) and not args["reprocess_input_data"] and not no_cache:
            features = torch.load(cached_features_file)
            print(f"Features loaded from cache at {cached_features_file}")
        else:
            print(f"Converting to features started.")
            features = convert_examples_to_features(
                examples,
                args["max_seq_length"],
                tokenizer,
                output_mode,
                cls_token_at_end=bool(args["model_type"] in ["xlnet"]),
                cls_token=tokenizer.cls_token,
                cls_token_segment_id=2 if args["model_type"] in ["xlnet"] else 0,
                sep_token=tokenizer.sep_token,
                sep_token_extra=bool(args["model_type"] in ["roberta"]),
                pad_on_left=bool(args["model_type"] in ["xlnet"]),
                pad_token=tokenizer.convert_tokens_to_ids([tokenizer.pad_token])[0],
                pad_token_segment_id=4 if args["model_type"] in ["xlnet"] else 0,
                process_count=process_count,
                multi_label=multi_label,
                silent=args['silent'],
                use_multiprocessing=args['use_multiprocessing']
            )

            if not no_cache:
                torch.save(features, cached_features_file)

        all_input_ids = torch.tensor([f.input_ids for f in features], dtype=torch.long)
        all_input_mask = torch.tensor([f.input_mask for f in features], dtype=torch.long)
        all_segment_ids = torch.tensor([f.segment_ids for f in features], dtype=torch.long)
        all_label_ids = None
        if output_mode == "classification":
            print("features:", len(features))
            all_label_ids = torch.tensor([f.label_id for f in features], dtype=torch.long)
        elif output_mode == "regression":
            all_label_ids = torch.tensor([f.label_id for f in features], dtype=torch.float)
        if not all_label_ids:
            raise ValueError("Tensor could not parse label ids")
        dataset = TensorDataset(all_input_ids, all_input_mask, all_segment_ids, all_label_ids)

        return dataset

    def _get_inputs_dict(self, batch):
        inputs = {
            "input_ids": batch[0],
            "attention_mask": batch[1],
            "labels": batch[3]
        }

        # XLM, DistilBERT and RoBERTa don't use segment_ids
        if self.args["model_type"] != "distilbert":
            inputs["token_type_ids"] = batch[2] if self.args["model_type"] in ["bert", "xlnet"] else None

        return inputs

    def _threshold(self, x, threshold):
        if x >= threshold:
            return 1
        return 0

    def compute_metrics(self, preds, labels, eval_examples, multi_label=False, **kwargs):
        """
        Computes the evaluation metrics for the model predictions.
        Args:
            preds: Model predictions
            labels: Ground truth labels
            eval_examples: List of examples on which evaluation was performed
            multi_label: Whether or not there are mulitple labels
            **kwargs: Additional metrics that should be used. Pass in the metrics as keyword arguments (name of metric: function to use). E.g. f1=sklearn.metrics.f1_score.
                        A metric function should take in two parameters. The first parameter will be the true labels, and the second parameter will be the predictions.
        Returns:
            result: Dictionary containing evaluation results. (Matthews correlation coefficient, tp, tn, fp, fn)
            wrong: List of InputExample objects corresponding to each incorrect prediction by the model
        """

        assert len(preds) == len(labels)

        extra_metrics = {}
        for metric, func in kwargs.items():
            extra_metrics[metric] = func(labels, preds)

        mismatched = labels != preds
        wrong = [i for (i, v) in zip(eval_examples, mismatched) if v.any()]

        if multi_label:
            label_ranking_score = label_ranking_average_precision_score(labels, preds)
            return {**{"LRAP": label_ranking_score}, **extra_metrics}, wrong

        mcc = matthews_corrcoef(labels, preds)
        acc = accuracy_score(labels, preds)

        if self.model.num_labels == 2:
            tn, fp, fn, tp = confusion_matrix(labels, preds).ravel()
            return {**{
                "mcc": mcc,
                "tp": tp,
                "tn": tn,
                "fp": fp,
                "fn": fn
            }, **extra_metrics}, wrong

        else:
            return {**{"mcc": mcc, "acc": acc}, **extra_metrics}, wrong

    def _move_model_to_device(self):
        self.model.to(self.args['device'])


def convert_examples_to_features(
        examples,
        max_seq_length,
        tokenizer,
        output_mode,
        cls_token_at_end=False,
        sep_token_extra=False,
        pad_on_left=False,
        cls_token="[CLS]",
        sep_token="[SEP]",
        pad_token=0,
        sequence_a_segment_id=0,
        sequence_b_segment_id=1,
        cls_token_segment_id=1,
        pad_token_segment_id=0,
        mask_padding_with_zero=True,
        process_count=1,
        multi_label=False,
        silent=False,
        use_multiprocessing=True,
        sliding_window=False,
        stride=False
):
    """ Loads a data file into a list of InputBatchs
        cls_token_at_end define the location of the CLS token:
              • False (Default, BERT/XLM pattern): [CLS] + A + [SEP] + B + [SEP]
              • True (XLNet/GPT pattern): A + [SEP] + B + [SEP] + [CLS]
        cls_token_segment_id define the segment id associated to the CLS token (0 for BERT, 2 for XLNet)
    """

    if sliding_window:
        if not stride:
            stride = 0.9
        examples = [(example, max_seq_length, tokenizer, output_mode, cls_token_at_end, cls_token, sep_token,
                     cls_token_segment_id, pad_on_left, pad_token_segment_id, sep_token_extra, multi_label, stride) for
                    example in examples]

        if use_multiprocessing:
            with Pool(process_count) as p:
                features = list(tqdm(p.imap(convert_example_to_feature_sliding_window, examples, chunksize=500),
                                     total=len(examples), disable=silent))
        else:
            features = [convert_example_to_feature_sliding_window(example) for example in
                        tqdm(examples, disable=silent)]
    else:
        examples = [(example, max_seq_length, tokenizer, output_mode, cls_token_at_end, cls_token, sep_token,
                     cls_token_segment_id, pad_on_left, pad_token_segment_id, sep_token_extra, multi_label) for example
                    in examples]

        if use_multiprocessing:
            with Pool(process_count) as p:
                features = list(tqdm(p.imap(convert_examples_to_features, examples, chunksize=500), total=len(examples),
                                     disable=silent))
        else:
            features = [convert_examples_to_features(example) for example in tqdm(examples, disable=silent)]

    return features


def convert_example_to_feature_sliding_window(
        example_row,
        pad_token=0,
        sequence_a_segment_id=0,
        sequence_b_segment_id=1,
        cls_token_segment_id=1,
        pad_token_segment_id=0,
        mask_padding_with_zero=True,
        sep_token_extra=False,
):
    example, max_seq_length, tokenizer, output_mode, cls_token_at_end, cls_token, sep_token, cls_token_segment_id, pad_on_left, pad_token_segment_id, sep_token_extra, multi_label, stride = example_row

    if stride < 1:
        stride = int(max_seq_length * stride)

    bucket_size = max_seq_length - (3 if sep_token_extra else 2)
    token_sets = []

    tokens_a = tokenizer.tokenize(example.text_a)

    special_tokens_count = 3 if sep_token_extra else 2
    if len(tokens_a) > bucket_size:
        token_sets = [tokens_a[i:i + bucket_size] for i in range(0, len(tokens_a), stride)]
    else:
        token_sets.append(tokens_a)

    if example.text_b:
        raise ValueError("Sequence pair tasks not implemented for sliding window tokenization.")

    # The convention in BERT is:
    # (a) For sequence pairs:
    #  tokens:   [CLS] is this jack ##son ##ville ? [SEP] no it is not . [SEP]
    #  type_ids:   0   0  0    0    0     0       0   0   1  1  1  1   1   1
    # (b) For single sequences:
    #  tokens:   [CLS] the dog is hairy . [SEP]
    #  type_ids:   0   0   0   0  0     0   0
    #
    # Where "type_ids" are used to indicate whether this is the first
    # sequence or the second sequence. The embedding vectors for `type=0` and
    # `type=1` were learned during pre-training and are added to the wordpiece
    # embedding vector (and position vector). This is not *strictly* necessary
    # since the [SEP] token unambiguously separates the sequences, but it makes
    # it easier for the model to learn the concept of sequences.
    #
    # For classification tasks, the first vector (corresponding to [CLS]) is
    # used as as the "sentence vector". Note that this only makes sense because
    # the entire model is fine-tuned.

    input_features = []
    for tokens_a in token_sets:
        tokens = tokens_a + [sep_token]
        segment_ids = [sequence_a_segment_id] * len(tokens)

        if cls_token_at_end:
            tokens = tokens + [cls_token]
            segment_ids = segment_ids + [cls_token_segment_id]
        else:
            tokens = [cls_token] + tokens
            segment_ids = [cls_token_segment_id] + segment_ids

        input_ids = tokenizer.convert_tokens_to_ids(tokens)

        # The mask has 1 for real tokens and 0 for padding tokens. Only real
        # tokens are attended to.
        input_mask = [1 if mask_padding_with_zero else 0] * len(input_ids)

        # Zero-pad up to the sequence length.
        padding_length = max_seq_length - len(input_ids)
        if pad_on_left:
            input_ids = ([pad_token] * padding_length) + input_ids
            input_mask = ([0 if mask_padding_with_zero else 1] * padding_length) + input_mask
            segment_ids = ([pad_token_segment_id] * padding_length) + segment_ids
        else:
            input_ids = input_ids + ([pad_token] * padding_length)
            input_mask = input_mask + ([0 if mask_padding_with_zero else 1] * padding_length)
            segment_ids = segment_ids + ([pad_token_segment_id] * padding_length)

        assert len(input_ids) == max_seq_length
        assert len(input_mask) == max_seq_length
        assert len(segment_ids) == max_seq_length

        # if output_mode == "classification":
        #     label_id = label_map[example.label]
        # elif output_mode == "regression":
        #     label_id = float(example.label)
        # else:
        #     raise KeyError(output_mode)

        input_features.append(
            InputFeatures(
                input_ids=input_ids,
                input_mask=input_mask,
                segment_ids=segment_ids,
                label_id=example.label
            )
        )

    return input_features
