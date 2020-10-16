import datetime
import copy
import json
import urllib.request
from NCMB.NCMBSignature import NCMBSignature
import NCMB.Client

class NCMBRequest:
  NCMB = None
  def post(self, class_name, data):
    # Create data
    return self.exec("POST", class_name, {}, data)
  def put(self, class_name, data, objectId):
    # Update data
    return self.exec("PUT", class_name, {}, data, objectId)

  def exec(self, method, class_name, queries, data, objectId = None):
    time = datetime.datetime.now().isoformat()
    # Generate signature
    sig = NCMBSignature.create(method, time, class_name, queries, objectId)
    headers = {
      'X-NCMB-Signature': sig,
      'Content-Type': 'application/json'
    }
    headers[NCMB.Client.NCMB.applicationKeyName] = self.NCMB.applicationKey
    headers[NCMB.Client.NCMB.timestampName] = time
    if self.NCMB.sessionToken is not None:
      headers[NCMB.Client.NCMB.sessionTokenHeader] = self.NCMB.sessionToken
    url = self.NCMB.url(class_name, queries, objectId)
    res = self.fetch(method, url, headers, data)
    if 'code' in res:
      raise Exception(res.error)
    if method == 'DELETE' and res == '':
      return {}
    return res
  def data(self, data):
    data = copy.copy(data)
    for key in ['createData', 'updateDate', 'objectId']:
      if key in data.keys():
        data.pop(key)
    return data
  def fetch(self, method, url, headers, data):
    if method in ['POST', 'PUT']:
      data = self.data(data)
    try:
      req = urllib.request.Request(url, data=json.dumps(data, separators=(',', ':')).encode(), method=method, headers=headers)
      with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
      return json.loads(e.read())
