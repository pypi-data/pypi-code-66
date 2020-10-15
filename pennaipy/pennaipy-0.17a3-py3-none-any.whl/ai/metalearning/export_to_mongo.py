# first, we need to construct a dataset that has each parameter as a feature. to do this we have to deconstruct
#the 'parameter' column into new columns.
import pandas as pd
import dask.dataframe as dd
import json
import pymongo
from bson.objectid import ObjectId
import string
import urllib.request, urllib.parse
import json
from datetime import datetime
from tqdm import tqdm
import os
pd.options.mode.chained_assignment = None
#limit number of records we'll process
max_records = 5000000000;
#
baseURL=os.environ['FGLab'] + '/api';
print(baseURL);
datasetsURL=baseURL + '/datasets'
algorithmsURL=baseURL + '/projects'
datasetsURL=baseURL + '/datasets'
apiDict = {'apikey':os.environ['apikey']}
apiParams = json.dumps(
    apiDict
    ).encode('utf8')
#
print('loading api datasets into dictionary...')
req = urllib.request.Request(datasetsURL, data=apiParams,
  headers={'content-type': 'application/json'})
r = urllib.request.urlopen(req)
datasets = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
datasets_dict = {}
for dataset in datasets:
     name =  dataset['name'].lower();
     _id = dataset['_id'];
     files = dataset['files'];
     datasets_dict[name] =  {'_id':_id,'files':files};
#
print('loading api algorithms into dictionary...')
req = urllib.request.Request(algorithmsURL, data=apiParams,
  headers={'content-type': 'application/json'})
r = urllib.request.urlopen(req)
algorithms = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
algorithm_names = {}
for algorithm in algorithms:
     name =  algorithm['name'].lower();
     _id = algorithm['_id'];
     algorithm_names[name.lower()] =  _id;
#
print('loading pmlb results data...')
#data = pd.read_csv('sklearn-benchmark5-data-edited.tsv.gz', sep='\t',
data = pd.read_csv('sklearn-benchmark5-data-short.tsv.gz', sep='\t',
                   names=['dataset',
                         'classifier',
                         'parameters',
                         'accuracy',
                         'macrof1',
                         'bal_accuracy']).fillna('')


print('formatting records for import...')
records = json.loads(data.T.to_json()).values()
ret_records = []
for record in records:
#split parameters into individual fields
  parameters= record['parameters'].split(",");
  nested_parameters = {}
  for parameter in parameters:
    psplit = parameter.split("=")
    if(len(psplit) > 1):
      nested_parameters[psplit[0]] = psplit[1];
# 
  algorithm_name = record['classifier']
  if(algorithm_name.lower() in algorithm_names):
    new_record = {}
    dataset_name = record['dataset']
    if(dataset_name.lower() in datasets_dict):
      dataset_id = ObjectId(datasets_dict[dataset_name.lower()]['_id'])
      dataset_files = datasets_dict[dataset_name.lower()]['files']
      new_record['_dataset_id'] = dataset_id;
      new_record['_files'] = dataset_files;
    #
    algorithm_id = ObjectId(algorithm_names[algorithm_name.lower()])
    new_record['_project_id'] = algorithm_id
    new_record['_options'] = nested_parameters;
    scores = {}
    scores['accuracy_score'] = record['accuracy']
    scores['balanced_accuracy'] = record['bal_accuracy']
    new_record['_scores'] = scores;
    new_record['_macrof1'] = record['macrof1']
    new_record['_started'] = datetime.now()
    new_record['_finished'] = datetime.now()
    new_record['_status'] = 'success'
    new_record['_files'] = []
    ret_records.append(new_record);
  if(len(ret_records) >= max_records):
    break
    
#print(ret_records);
#
client = pymongo.MongoClient()
db = client.FGLab
db.experiments.insert(ret_records)
#for record_dict in ret_records:
#  post_params = json.dumps(
#    {**record_dict, **apiDict}
#    ).encode('utf8')
#  print(post_params);
  
