import os
efTJp=Exception
efTJs=False
efTJP=str
efTJI=int
efTJY=range
efTJh=len
efTJl=object
efTJo=True
import re
import glob
import json
import base64
import logging
import pyaes
from localstack import config as localstack_config
from localstack.utils.common import(safe_requests as requests,load_file,save_file,to_str,to_bytes,parallelize,get_or_create_file,now_utc,str_insert,str_remove)
from localstack_ext import config
from localstack_ext.config import PROTECTED_FOLDERS,ROOT_FOLDER
from localstack_ext.constants import VERSION
ENV_PREPARED={}
MAX_KEY_CACHE_DURATION_SECS=60*60*24
LOG=logging.getLogger(__name__)
def read_api_key():
 key=os.environ.get('LOCALSTACK_API_KEY')
 if key:
  return key
 raise efTJp('Unable to retrieve API key. Please configure $LOCALSTACK_API_KEY in your environment')
def fetch_key():
 api_key=read_api_key()
 if api_key=='test':
  return 'test'
 data={'api_key':api_key,'version':VERSION}
 try:
  logging.getLogger('py.warnings').setLevel(logging.ERROR)
  result=requests.post('%s/activate'%config.API_URL,json.dumps(data),verify=efTJs)
  key_base64=json.loads(result.content)['key']
  cache_key_locally(key_base64)
 except efTJp:
  key_base64=load_cached_key()
 finally:
  logging.getLogger('py.warnings').setLevel(logging.WARNING)
 decoded_key=to_str(base64.b64decode(key_base64))
 return decoded_key
def cache_key_locally(key_b64):
 content=get_or_create_file(localstack_config.CONFIG_FILE_PATH)
 configs=json.loads(to_str(content))
 timestamp=efTJP(efTJI(now_utc()))
 key_raw=to_str(base64.b64decode(key_b64))
 for i in efTJY(efTJh(timestamp)):
  key_raw=str_insert(key_raw,i*2,timestamp[i])
 key_b64=to_str(base64.b64encode(to_bytes(key_raw)))
 configs['cached_key']={'timestamp':efTJI(timestamp),'key':key_b64}
 save_file(localstack_config.CONFIG_FILE_PATH,json.dumps(configs))
 return configs
def load_cached_key():
 content=get_or_create_file(localstack_config.CONFIG_FILE_PATH)
 configs=json.loads(to_str(content))
 cached_key=configs['cached_key']
 now=now_utc()
 if(now-cached_key['timestamp'])>MAX_KEY_CACHE_DURATION_SECS:
  raise efTJp('Cached key expired')
 timestamp=efTJP(cached_key['timestamp'])
 key_raw=to_str(base64.b64decode(cached_key['key']))
 for i in efTJY(efTJh(timestamp)):
  assert key_raw[i]==timestamp[i]
  key_raw=str_remove(key_raw,i)
 key_b64=to_str(base64.b64encode(to_bytes(key_raw)))
 return key_b64
def generate_aes_cipher(key):
 key=to_bytes(key)
 return pyaes.AESModeOfOperationCBC(key,iv='\0'*16)
def decrypt_file(source,target,key):
 cipher=generate_aes_cipher(key)
 raw=load_file(source,mode='rb')
 decrypter=pyaes.Decrypter(cipher)
 decrypted=decrypter.feed(raw)
 decrypted+=decrypter.feed()
 decrypted=decrypted.partition(b'\0')[0]
 decrypted=to_str(decrypted)
 save_file(target,content=decrypted)
def decrypt_files(key):
 files=[]
 for folder in PROTECTED_FOLDERS:
  for subpath in('*.py.enc','**/*.py.enc'):
   for f in glob.glob('%s/localstack_ext/%s/%s'%(ROOT_FOLDER,folder,subpath)):
    files.append(f)
 def _decrypt(f):
  target=f[:-4]
  if not os.path.exists(target):
   decrypt_file(f,target,key)
 parallelize(_decrypt,files)
def cleanup_environment():
 excepted_files=r'.*/services/((edge)|(dns_server)|(__init__))\.py'
 for folder in PROTECTED_FOLDERS:
  for subpath in('*.py.enc','**/*.py.enc'):
   for f in glob.glob('%s/localstack_ext/%s/%s'%(ROOT_FOLDER,folder,subpath)):
    target=f[:-4]
    if not re.match(excepted_files,target):
     for delete_file in(target,'%sc'%target):
      if os.path.exists(delete_file):
       os.remove(delete_file)
def prepare_environment():
 class OnClose(efTJl):
  def __exit__(self,*args,**kwargs):
   if not ENV_PREPARED.get('finalized'):
    cleanup_environment()
   ENV_PREPARED['finalized']=efTJo
  def __enter__(self,*args,**kwargs):
   pass
 if not ENV_PREPARED.get('finalized'):
  try:
   key=fetch_key()
   if key!='test':
    decrypt_files(key)
    LOG.info('Successfully activated API key')
  except efTJp:
   pass
 return OnClose()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
