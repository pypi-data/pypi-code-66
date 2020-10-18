from localstack.utils.aws import aws_models
bTvrN=super
bTvrq=None
bTvrJ=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  bTvrN(LambdaLayer,self).__init__(arn)
  self.cwd=bTvrq
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.bTvrJ.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,bTvrJ,env=bTvrq):
  bTvrN(RDSDatabase,self).__init__(bTvrJ,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,bTvrJ,env=bTvrq):
  bTvrN(RDSCluster,self).__init__(bTvrJ,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,bTvrJ,env=bTvrq):
  bTvrN(AppSyncAPI,self).__init__(bTvrJ,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,bTvrJ,env=bTvrq):
  bTvrN(AmplifyApp,self).__init__(bTvrJ,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,bTvrJ,env=bTvrq):
  bTvrN(ElastiCacheCluster,self).__init__(bTvrJ,env=env)
class TransferServer(BaseComponent):
 def __init__(self,bTvrJ,env=bTvrq):
  bTvrN(TransferServer,self).__init__(bTvrJ,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,bTvrJ,env=bTvrq):
  bTvrN(CloudFrontDistribution,self).__init__(bTvrJ,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,bTvrJ,env=bTvrq):
  bTvrN(CodeCommitRepository,self).__init__(bTvrJ,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
