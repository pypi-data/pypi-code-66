from bizai.framework.constants.persistencevolumeenum import PersistenceVolumeEnum

from bizai.framework.persistence.impl.ibmcospersistence import IBMCOSPersistenceVolume
from bizai.framework.persistence.impl.db2persistence import DB2PersistenceVolume


class PersistenceSvc():

    def __init__(self):
        self._persistence = {}

    def get_persistence(self, config):
        persistence = None
        return persistence

    def register_builder(self, key=None, persistence_volume_inst=None):
        if key == PersistenceVolumeEnum.IBM_COS:
            self._persistence[key]  = IBMCOSPersistenceVolume()
        elif key == PersistenceVolumeEnum.DB2:
            self._persistence[key]  = DB2PersistenceVolume()   
        # Custom persistence volume 
        elif persistence_volume_inst is not None:
            self._persistence[key]  = persistence_volume_inst                  

    def create_connection(self, key, **config):
        print("create_connection::key::", key)
        persistence_volume_inst = self._persistence.get(key)
        if not persistence_volume_inst:
            raise ValueError(key)

        # connect to the volume persistence
        persistence_volume_inst(**config)


    def get(self, key):
        print("key::", key)
        persistence_volume_inst = self._persistence.get(key)
        if not persistence_volume_inst:
            raise ValueError(key)
        return persistence_volume_inst

# python -m bizai.framework.services.impl.persistencesvc
if __name__ == "__main__":

    # cos_config = {
    #     "IBM_COS_API_KEY_ID": "25RdJDYL1Xlj0RvWGKRDCW7Xrn1esbA2yDtxyYGxOMym",
    #     "IBM_COS_RESOURCE_CRN": "crn:v1:bluemix:public:cloud-object-storage:global:a/f45d02f7085c3cbf06ee8aeb2d38bcd4:ada9b6a7-33d5-43a5-aaa3-f876776a32f8::",
    #     "IBM_COS_AUTH_ENDPOINT": "https://iam.ng.bluemix.net/oidc/token",
    #     "IBM_COS_SIGNATURE_VERSION": "oauth",
    #     "IBM_COS_ENDPOINT": "https://s3.us-south.cloud-object-storage.appdomain.cloud"
    # }

    # persistence_controller = PersistenceController()
    # persistence_controller.register_builder(
    #     "IBM_COS", IBMCOSPersistenceVolume())
    # persistence_controller.create("IBM_COS", **cos_config)


    SSL_DSN = "PORT=50001;PROTOCOL=TCPIP;UID=bluadmin;PWD=H1_8dZY@YOuHF9BHmT7ZWhdBdQX@k;Security=SSL;"
    db_config = {
        "DATABASE": "BLUDB",
        "HOSTNAME": "db2w-tiggaci.us-east.db2w.cloud.ibm.com",
        "PORT": 50001,
        "PROTOCOL": "TCPIP",
        "UID": "bluadmin",
        "PASSWORD": "H1_8dZY@YOuHF9BHmT7ZWhdBdQX@k",
        "SECURITY": "SSL"
    }

    persistence_controller = PersistenceController()
    persistence_controller.register_builder(
        "DB2", DB2PersistenceVolume())
    persistence_controller.create("DB2", **db_config)
    
