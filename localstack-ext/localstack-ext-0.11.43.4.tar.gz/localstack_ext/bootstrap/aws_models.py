from localstack.utils.aws import aws_models
bAmqp=super
bAmqF=None
bAmqz=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  bAmqp(LambdaLayer,self).__init__(arn)
  self.cwd=bAmqF
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.bAmqz.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,bAmqz,env=bAmqF):
  bAmqp(RDSDatabase,self).__init__(bAmqz,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,bAmqz,env=bAmqF):
  bAmqp(RDSCluster,self).__init__(bAmqz,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,bAmqz,env=bAmqF):
  bAmqp(AppSyncAPI,self).__init__(bAmqz,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,bAmqz,env=bAmqF):
  bAmqp(AmplifyApp,self).__init__(bAmqz,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,bAmqz,env=bAmqF):
  bAmqp(ElastiCacheCluster,self).__init__(bAmqz,env=env)
class TransferServer(BaseComponent):
 def __init__(self,bAmqz,env=bAmqF):
  bAmqp(TransferServer,self).__init__(bAmqz,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,bAmqz,env=bAmqF):
  bAmqp(CloudFrontDistribution,self).__init__(bAmqz,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,bAmqz,env=bAmqF):
  bAmqp(CodeCommitRepository,self).__init__(bAmqz,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
