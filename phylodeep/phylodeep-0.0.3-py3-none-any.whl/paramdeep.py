
import pandas as pd

from phylodeep import FULL, SUMSTATS, BD, BDEI, BDSS
from phylodeep.encoding import encode_into_summary_statistics, encode_into_most_recent
from phylodeep.model_load import model_scale_load_ffnn, model_load_cnn
from phylodeep.tree_utilities import *


prediction_method_options = [FULL, SUMSTATS]
param_model_options = [BD, BDEI, BDSS]


def paramdeep(tree_file, proba_sampling, model=BD, vector_representation=FULL, **kvargs):
    """
    Provides model selection between selected models for given tree.
    :param tree_file: path to a file with dated trees (in newick format)
    :type tree_file: str
    :param proba_sampling: presumed sampling probability for all input trees, value between 0.01 and 1
    :type proba_sampling: float
    :param model: option to choose, you can choose 'BD' (basic birth-death model with incomplete sampling BD), 'BDEI'
    (BD with exposed class) or 'BDSS' (BD with 'superspreading' individuals).
    :type model: str
    :param vector_representation: option to choose between 'FFNN_SUMSTATS' to select a network trained on summary
    statistics or 'CNN_FULL_TREE' to select a network trained on full tree representation, by default, we use
    'CNN_FULL_TREE'
    :type vector_representation: str
    :return: pd.df, predicted parameter values or model selection
    """
    # check options
    if proba_sampling > 1 or proba_sampling < 0.01:
        raise ValueError('Incorrect value of \'sampling probability\' parameter')
    if model not in param_model_options:
        raise ValueError('Incorrect value of \'model\' option.')
    if vector_representation not in prediction_method_options:
        raise ValueError('Incorrect value of \'prediction_method\' option.')

    # read trees
    tree = read_tree_file(tree_file)

    # check tree size
    tree_size = check_tree_size(tree)

    # encode the trees
    if vector_representation == SUMSTATS:
        encoded_tree, rescale_factor = encode_into_summary_statistics(tree, proba_sampling)
    elif vector_representation == FULL:
        encoded_tree, rescale_factor = encode_into_most_recent(tree, proba_sampling)

    # load model
    if vector_representation == SUMSTATS:
        model, scaler = model_scale_load_ffnn(tree_size, model)
    elif vector_representation == FULL:
        model = model_load_cnn(tree_size, model)

    # predict values:
    if vector_representation == SUMSTATS:
        encoded_tree = scaler.transform(encoded_tree)
        predictions = pd.DataFrame(model.predict(encoded_tree))
    elif vector_representation == FULL:
        predictions = pd.DataFrame(model.predict(encoded_tree))

    # annotate predictions:
    predictions = annotator(predictions, model)
    # if inferred paramater values: rescale back the rates
    predictions = rescaler(predictions, rescale_factor)
    return predictions


def main():
    """
    Entry point, calling :py:func:`phylodeep.paramdeep`  with command-line arguments.
    :return: void
    """
    import argparse

    parser = argparse.ArgumentParser(description="Parameter inference for phylodynamics based on deep learning.",
                                     prog='paramdeep')

    tree_group = parser.add_argument_group('tree-related arguments')
    tree_group.add_argument('-t', '--tree', help="input tree(s) in newick format (must be rooted).",
                            type=str, required=True)
    tree_group.add_argument('-p', '--proba_sampling', help="presumed sampling probability for removed tips. Must be "
                                                           "between 0.01 and 1",
                            type=float, required=True)

    prediction_group = parser.add_argument_group('neural-network-prediction arguments')
    prediction_group.add_argument('-m', '--model', choices=[BD, BDEI, BDSS],
                                  required=True, type=str, default=None,
                                  help="Choose one of the models to be inferred for the tree. For parameter inference,"
                                       " you can choose either BD (basic birth-death with incomplete sampling), "
                                       " BDEI (BD with exposed-infectious) or BDSS (BD with superspreading "
                                       "individuals).")

    prediction_group.add_argument('-v', '--vector_representation', choices=[FULL, SUMSTATS], required=False, type=str,
                                  default=FULL,
                                  help="Choose neural networks: either FULL: CNN trained on full tree representation or"
                                       "SUMSTATS: FFNN trained on summary statistics. By default set to FULL.")

    output_group = parser.add_argument_group('output')
    output_group.add_argument('-o', '--output', required=True, type=str, help="The name of output file.")

    params = parser.parse_args()

    inference = paramdeep(**vars(params))

    inference.to_csv(params.output)


if '__main__' == __name__:
    main()
