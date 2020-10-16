# ==========================
# AWS CONSTANTS
# ==========================
import os

ENV = 'prod'
ROLE = 'arn:aws:iam::485206745971:role/service-role/AmazonSageMaker-ExecutionRole-20190528T144422'
ACCOUNT = '485206745971'
REGION = 'eu-north-1'
BUCKET = f'sb-data-sc-{ENV}'

# Absolute path to folder with model params
PARAMS_FOLDER = f'{os.path.dirname(os.path.abspath(__file__))}/params'

# Absolute path to folder with queries for both training the model or prediction
QUERY_FOLDER = f'{os.path.dirname(os.path.abspath(__file__))}/query'

# Model paths
INPUT_TRAIN_PATH_FMT = '{MODEL_NAME}/input_data/train'
INPUT_PREDICT_PATH_FMT = '{MODEL_NAME}/input_data/predict'
OUTPUT_PATH_FMT = '{MODEL_NAME}/output_data'
MODEL_PATH_FMT = '{MODEL_NAME}/model'

# Query Paths
MODEL_INPUT_DATA_TEMPLATE_QUERY = f'{QUERY_FOLDER}'+'/{MODEL_NAME}_model_input_template_query.sql'
PREDICT_INPUT_DATA_TEMPLATE_QUERY = f'{QUERY_FOLDER}'+'/{MODEL_NAME}_predict_template_query.sql'
