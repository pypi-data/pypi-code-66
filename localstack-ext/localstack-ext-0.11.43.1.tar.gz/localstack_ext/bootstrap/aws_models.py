from localstack.utils.aws import aws_models
kumIf=super
kumId=None
kumIV=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  kumIf(LambdaLayer,self).__init__(arn)
  self.cwd=kumId
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.kumIV.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,kumIV,env=kumId):
  kumIf(RDSDatabase,self).__init__(kumIV,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,kumIV,env=kumId):
  kumIf(RDSCluster,self).__init__(kumIV,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,kumIV,env=kumId):
  kumIf(AppSyncAPI,self).__init__(kumIV,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,kumIV,env=kumId):
  kumIf(AmplifyApp,self).__init__(kumIV,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,kumIV,env=kumId):
  kumIf(ElastiCacheCluster,self).__init__(kumIV,env=env)
class TransferServer(BaseComponent):
 def __init__(self,kumIV,env=kumId):
  kumIf(TransferServer,self).__init__(kumIV,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,kumIV,env=kumId):
  kumIf(CloudFrontDistribution,self).__init__(kumIV,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,kumIV,env=kumId):
  kumIf(CodeCommitRepository,self).__init__(kumIV,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
