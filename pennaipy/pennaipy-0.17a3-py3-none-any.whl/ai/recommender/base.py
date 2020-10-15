"""
Recommender system for Penn AI.
"""
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(module)s: %(levelname)s: %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
import numpy as np
import os
import pdb
import pickle
import gzip
import random
import hashlib
import copy
from pandas.util import hash_pandas_object
import pandas as pd

# implementing metaclass __repr__ for more human readable
# names for generated tests in test_recommender.py
class MC(type):
    def __repr__(self):
        return self.__qualname__

class BaseRecommender(object, metaclass=MC):
    """Base recommender for PennAI

    The BaseRecommender is not intended to be used directly; it is a skeleton class
    defining the interface for future recommenders within the PennAI project.

    Parameters
    ----------
    ml_type: str, 'classifier' or 'regressor'
        Recommending classifiers or regressors. Used to determine ML options.

    metric: str (default: accuracy for classifiers, mse for regressors)
        The metric by which to assess performance on the datasets.

    ml_p: DataFrame (default: None)
        Contains all valid ML parameter combos, with columns 'algorithm' and
        'parameters'

    knowledgebase_results: Pandas DataFrame or None
        Initial knowledgebase results data.
        If not None and not loading a serialized recommender, the recommender
        will initialize and train on this data.
        If loading a serialized recommender, this is the knowlegebase that
        accompanies it.

    knowledgebase_metafeatures: Pandas DataFrame or None
        Initial knowledgebase metafeatures data.
        If loading a serialized recommender, this is the knowlegebase that
        accompanies it.

    serialized_rec_directory: string or None
        Name of the directory to save/load a serialized recommender.
        Default directory is "."

    serialized_rec_filename: string or None
        Name of the file to save/load a serialized recommender.
        If the filename is not provided, the default filename based on the
        recommender type, and metric, and knowledgebase used.

    load_serialized_rec: str, "always", "never", "if_exists"
        Whether to attempt to load a serialized recommender:
            "if_exists" - If a serialized recomender exsists at the specified
            path, load it.
            "always" - Always load a serialized recommender.  Throw an
            exception if no serialized recommender exists.
            "never" - Never load a serialized recommender.

    """

    def __init__(self,
            ml_type='classifier',
            metric=None,
            ml_p=None,
            random_state=None,
            knowledgebase_results=None,
            knowledgebase_metafeatures=None,
            load_serialized_rec="if_exists",
            serialized_rec_directory=None,
            serialized_rec_filename=None):

        """Initialize recommendation system."""
        if ml_type not in ['classifier', 'regressor']:
            raise ValueError('ml_type must be "classifier" or "regressor"')

        if load_serialized_rec not in ["always", "never", "if_exists"]:
            raise ValueError('load_serialized_rec must be "always", "never" or'
                    ' "if_exists"')

        self.random_state = random_state
        if self.random_state is not None:
            random.seed(self.random_state)
            np.random.seed(self.random_state)

        logger.info('self.random_state: ' + str(self.random_state))

        self.ml_type = ml_type

        if metric is None:
            self.metric='bal_accuracy' if self.ml_type=='classifier' else 'mse'
        else:
            self.metric = metric

        # maintain a set of dataset-algorithm-parameter combinations that have
        # already been evaluated
        self.trained_dataset_models = set()
        # hash table for parameter options
        self.hash_2_param = {}

        # get ml+p combos (note: this triggers a property in base recommender)
        # self.ml_htable = {}
        self.ml_p = ml_p

        # generate the serialized recommender path
        self.serialized_rec_path = self._generate_serialized_rec_path(
            serialized_rec_filename,
            serialized_rec_directory
            )


        # train an empty recommender, either using the provided kb or
        # loading a serialized rec from file
        self._train_empty_rec(
            ml_type,
            metric,
            ml_p,
            random_state,
            knowledgebase_results,
            knowledgebase_metafeatures,
            load_serialized_rec,
            serialized_rec_directory,
            serialized_rec_filename)


    def _train_empty_rec(self,
            ml_type,
            metric,
            ml_p,
            random_state,
            knowledgebase_results,
            knowledgebase_metafeatures,
            load_serialized_rec,
            serialized_rec_directory,
            serialized_rec_filename):

        # load serialized rec, or initialize from the given
        # knowledgebase
        logger.info(f"load_serialized_rec='{load_serialized_rec}'")

        if load_serialized_rec == "always":
            if not os.path.exists(self.serialized_rec_path):
                raise ValueError(f"load_serialized_rec='{load_serialized_rec}'"
                        " but cannot load serialized recommender:"
                        " '{self.serialized_rec_path}'")
            self.load(self.serialized_rec_path, knowledgebase_results)

        elif load_serialized_rec == "if_exists":
            if os.path.exists(self.serialized_rec_path):
                logger.info(f"Loading serialized recommender:"
                        " {self.serialized_rec_path}")
                self.load(self.serialized_rec_path, knowledgebase_results)
            else:
                logger.warn(f"Not loading serialized recommender, file does "
                        "not exist: {self.serialized_rec_path}")
                if knowledgebase_results is not None:
                    logger.info(f"Initializing new recommender from provided "
                            "knowledgebase")
                    self.update(knowledgebase_results,
                            knowledgebase_metafeatures, source='knowledgebase')

        else:
            logger.info(f"Not loading serialized recommender.")
            if knowledgebase_results is not None:
                logger.info(f"Initializing new recommender from provided "
                        "knowledgebase")
                self.update(knowledgebase_results, knowledgebase_metafeatures,
                        source='knowledgebase')


    def _default_serialized_rec_filename(self):
        """Generate the default name of the serialized instance of this
        recommender
        """

        # Hardcoading the informal kb descriptor for now, this should be changed.
        return (
            self.__class__.__name__
            + '_' + self.ml_type
            + '_' + self.metric
            + '_pmlb_20200821'
            +'.pkl.gz')


    def _generate_serialized_rec_path(self,
        serialized_rec_filename=None,
        serialized_rec_directory=None):
        """ Generate the path to save/load serialized recommender

        Parameters
        ----------
        serialized_rec_filename
        serialized_rec_directory
        """

        # dynamic default values
        serialized_rec_directory = serialized_rec_directory or "."
        serialized_rec_filename = serialized_rec_filename or \
                self._default_serialized_rec_filename()

        return os.path.join(serialized_rec_directory, serialized_rec_filename)


    def update(self, results_data, results_mf=None, source='pennai'):
        """Update ML / Parameter recommendations.

        Parameters
        ----------
        results_data: DataFrame
            columns corresponding to:
            'algorithm'
            'parameters'
            self.metric

        results_mf: DataFrame, optional
            columns corresponding to metafeatures of each dataset in
            results_data.

        source: string
            if 'pennai', will update tally of trained dataset models
        """
        assert(results_data is not None), "results_data cannot be None"

        if results_data.isna().values.any():
            logger.warning('There are NaNs in results_data.')
            #logger.warning(str(results_data))
            logger.warning(results_data.head())
            logger.error('Dropping NaN results.')
            results_data.dropna(inplace=True)

        # update parameter hash table
        logger.info('updating hash_2_param...')
        self.hash_2_param.update(
                {self._hash_simple_dict(x):x
                for x in results_data['parameters'].values})
        param_2_hash = {frozenset(v.items()):k
                for k,v in self.hash_2_param.items()}
        # store parameter_hash variable in results_data
        logger.info('storing parameter hash...')
        results_data['parameter_hash'] = results_data['parameters'].apply(
                lambda x: param_2_hash[frozenset(x.items())])

        # update results list
        if source == 'pennai':
            self._update_trained_dataset_models_from_df(results_data)

    def _hash_simple_dict(self, x):
        """Provides sha256 hash for a dictionary with hashable items."""
        hasher = hashlib.sha256()
        hasher.update(repr(tuple(sorted(x.items()))).encode())
        return hasher.hexdigest()

    def recommend(self, dataset_id=None, n_recs=1, dataset_mf=None):
        """Return a model and parameter values expected to do best on dataset.

        Parameters
        ----------

        dataset_id: string
            ID of the dataset for which the recommender is generating
            recommendations.
        n_recs: int (default: 1), optional
            Return a list of length n_recs in order of estimators and parameters
            expected to do best.
        dataset_mf: DataFrame
            metafeatures of the dataset represented by dataset_id
        """
        # self.dataset_id_to_hash.update(
        #         {dataset_id:dataset_mf['_id'].values[0]})

    def load(self, filename=None, knowledgebase=None):
        """Load a saved recommender state.

        :param filename: string or None
            Name of file to load
        :param knowledgebase: string or None
            DataFrame with columns corresponding to:
                'dataset'
                'algorithm'
                'parameters'
                self.metric
        """
        if filename is None:
            fn = self.serialized_rec_path
        else:
            fn = filename

        if os.path.isfile(fn):
            logger.info('loading recommender ' + fn + ' from file')
            f = gzip.open(fn, 'rb')
            tmp_dict = pickle.load(f)
            f.close()

            #logger.debug(f"rec keys: {tmp_dict.keys()}")

            # check if parameters match, if not throw warning/error
            for k,v in tmp_dict.items():
                if k in self.__dict__.keys():
                    try:
                        if self.__dict__[k] != tmp_dict[k]:
                            logger.warn(k+' changing from '
                                    + str(self.__dict__[k])[:20] + '... to '
                                        + str(tmp_dict[k])[:20] + '...')
                    except:
                        pass
                else:
                    logger.warn('adding ' + k+'=' + str(tmp_dict[k])[:20]
                            + '...')
            logger.info('updating internal state')

            # check ml_p hashes
            rowHashes = hash_pandas_object(self.ml_p.apply(str)).values
            newHash = hashlib.sha256(rowHashes).hexdigest()
            if 'ml_p_hash' in tmp_dict.keys():
                if newHash == tmp_dict['ml_p_hash']:
                    logger.info('ml_p hashes match')
                else:
                    error_msg = ('the ml_p hash from the pickle is different. '
                        'This likely means the algorithm configurations have '
                        'changed since this recommender was saved. You should '
                        'update and save a new one.')
                    logger.error(error_msg)

                    # debugging
                    if ('_ml_p' in tmp_dict):
                        pd.testing.assert_frame_equal(self.ml_p, tmp_dict['_ml_p'])
                    else:
                        logger.error(f"Pickle does not contain _ml_p for debugging.")
                        logger.error(f"Keys: {tmp_dict.keys()}")

                    raise ValueError(error_msg)
                del tmp_dict['ml_p_hash']

            # update self with loaded pickle
            self.__dict__.update(tmp_dict)
            return True
        else:
            logger.warning('Could not load filename '+ fn)
            return False


    def save(self, filename=None):
        """Save the current recommender.

        :param filename: string or None
            Name of file to load
        """
        if filename is None:
            fn = self.serialized_rec_path
        else:
            fn = filename
        if os.path.isfile(fn):
            logger.warning('overwriting ' + fn)

        save_dict = copy.deepcopy(self.__dict__)

        # remove results_df to save space. this gets loaded by load() fn.
        if 'results_df' in save_dict.keys():
            logger.debug('deleting save_dict[results_df]:'
                    +str(save_dict['results_df'].head()))
            rowHashes = hash_pandas_object(save_dict['results_df']).values
            save_dict['results_df_hash'] = hashlib.sha256(
                    rowHashes).hexdigest()
            del save_dict['results_df']

        # remove ml_p to save space
        rowHashes = hash_pandas_object(save_dict['_ml_p'].apply(str)).values
        save_dict['ml_p_hash'] = hashlib.sha256(rowHashes).hexdigest()
        del save_dict['_ml_p']
        del save_dict['mlp_combos']

        logger.info('saving recommender as ' + fn)
        f = gzip.open(fn, 'wb')
        pickle.dump(save_dict, f, 2)
        f.close()

    def update_and_save(self, results_data, results_mf=None, source='pennai',
            filename=None):
        """runs self.update() and self.save.

        Parameters
        ----------
        results_data: DataFrame
            columns corresponding to:
            'algorithm'
            'parameters'
            self.metric

        results_mf: DataFrame, optional
            columns corresponding to metafeatures of each dataset in
            results_data.

        source: string
            if 'pennai', will update tally of trained dataset models
        """
        self.update(results_data, results_mf, source)
        self.save(filename)

    @property
    def ml_p(self):
        logger.debug('getting ml_p')
        return self._ml_p

    @ml_p.setter
    def ml_p(self, value):
        logger.debug('setting ml_p')
        if value is not None:
            #filter out SVC (temporary)
            self._ml_p = value[['algorithm','parameters']]
            logger.debug('setting hash table')
            # maintain a parameter hash table for parameter settings
            # if 'alg_name' not in value.columns:
            #     self._ml_p['alg_name'] = self._ml_p['algorithm']

            self.hash_2_param = {
                    self._hash_simple_dict(x):x
                    for x in self._ml_p['parameters'].values}
            param_2_hash = {frozenset(v.items()):k
                    for k,v in self.hash_2_param.items()}
            # machine learning - parameter combinations
            self.mlp_combos = (self._ml_p['algorithm']+'|'+
                               self._ml_p['parameters'].apply(lambda x:
                                   param_2_hash[frozenset(x.items())]))
            # filter out duplicates
            self.mlp_combos = self.mlp_combos.drop_duplicates()
            # # set ml_htable
            # if 'alg_name' in value.columns:
            #     self.ml_htable = {
            #             k:v for v,k in zip(value['alg_name'].unique(),
            #             value['algorithm'].unique())
            #             }
        else:
            logger.warning('value of ml_p is None')
        logger.debug('param_2_hash:{} objects'.format(len(param_2_hash)))

    def _update_trained_dataset_models_from_df(self, results_data):
        '''stores the trained_dataset_models to aid in filtering repeats.'''
        results_data.loc[:, 'dataset-algorithm-parameters'] = (
                                       results_data['_id'].values + '|' +
                                       results_data['algorithm'].values + '|' +
                                       results_data['parameter_hash'].values)

        for i,phash in enumerate(results_data['parameter_hash'].values):
            if phash not in self.hash_2_param.keys():
                logger.error(phash
                        +' not in self.hash_2_param. parameter values: '
                        + str(results_data['parameters'].values[i]))
        # get unique dataset / parameter / classifier combos in results_data
        d_ml_p = results_data['dataset-algorithm-parameters'].unique()
        self.trained_dataset_models.update(d_ml_p)

    def _update_trained_dataset_models_from_rec(self, dataset_id, ml_rec,
            phash_rec):
        '''update the recommender's memory with the new algorithm-parameter
        combos that it recommended'''
        if dataset_id is not None:
            # datahash = self.dataset_id_to_hash[dataset_id]
            self.trained_dataset_models.update(
                                    ['|'.join([dataset_id, ml, p])
                                    for ml, p in zip(ml_rec, phash_rec)])
