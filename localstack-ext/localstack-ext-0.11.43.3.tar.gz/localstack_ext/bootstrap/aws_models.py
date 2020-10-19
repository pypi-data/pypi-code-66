from localstack.utils.aws import aws_models
lCJps=super
lCJpe=None
lCJpX=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  lCJps(LambdaLayer,self).__init__(arn)
  self.cwd=lCJpe
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.lCJpX.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,lCJpX,env=lCJpe):
  lCJps(RDSDatabase,self).__init__(lCJpX,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,lCJpX,env=lCJpe):
  lCJps(RDSCluster,self).__init__(lCJpX,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,lCJpX,env=lCJpe):
  lCJps(AppSyncAPI,self).__init__(lCJpX,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,lCJpX,env=lCJpe):
  lCJps(AmplifyApp,self).__init__(lCJpX,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,lCJpX,env=lCJpe):
  lCJps(ElastiCacheCluster,self).__init__(lCJpX,env=env)
class TransferServer(BaseComponent):
 def __init__(self,lCJpX,env=lCJpe):
  lCJps(TransferServer,self).__init__(lCJpX,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,lCJpX,env=lCJpe):
  lCJps(CloudFrontDistribution,self).__init__(lCJpX,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,lCJpX,env=lCJpe):
  lCJps(CodeCommitRepository,self).__init__(lCJpX,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
