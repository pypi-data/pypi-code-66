from localstack.utils.aws import aws_models
ThaFE=super
ThaFD=None
ThaFe=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ThaFE(LambdaLayer,self).__init__(arn)
  self.cwd=ThaFD
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.ThaFe.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,ThaFe,env=ThaFD):
  ThaFE(RDSDatabase,self).__init__(ThaFe,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,ThaFe,env=ThaFD):
  ThaFE(RDSCluster,self).__init__(ThaFe,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,ThaFe,env=ThaFD):
  ThaFE(AppSyncAPI,self).__init__(ThaFe,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,ThaFe,env=ThaFD):
  ThaFE(AmplifyApp,self).__init__(ThaFe,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,ThaFe,env=ThaFD):
  ThaFE(ElastiCacheCluster,self).__init__(ThaFe,env=env)
class TransferServer(BaseComponent):
 def __init__(self,ThaFe,env=ThaFD):
  ThaFE(TransferServer,self).__init__(ThaFe,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,ThaFe,env=ThaFD):
  ThaFE(CloudFrontDistribution,self).__init__(ThaFe,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,ThaFe,env=ThaFD):
  ThaFE(CodeCommitRepository,self).__init__(ThaFe,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
