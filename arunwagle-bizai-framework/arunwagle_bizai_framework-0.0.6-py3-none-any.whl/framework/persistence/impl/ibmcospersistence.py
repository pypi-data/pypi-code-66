
import ibm_boto3
from ibm_botocore.client import Config
from ibm_botocore.exceptions import ClientError

from bizai.framework.decorators.validate import validate_input
from bizai.framework.persistence.persistencevolume import FilePersistenceVolume


class IBMCOSPersistenceVolume (FilePersistenceVolume):

    schema_connect = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Schema for connect",
        "type": "object",
        "properties": {
                "IBM_COS_API_KEY_ID": {type:"string"},
                "IBM_COS_RESOURCE_CRN": {type:"string"},
                "IBM_COS_AUTH_ENDPOINT": {type:"string"},
                "IBM_COS_SIGNATURE_VERSION": {type:"string"},
                "IBM_COS_ENDPOINT": {type:"string"}
        },
        "required": [ "IBM_COS_API_KEY_ID","IBM_COS_RESOURCE_CRN","IBM_COS_AUTH_ENDPOINT", "IBM_COS_SIGNATURE_VERSION","IBM_COS_ENDPOINT"]
    }

    def __call__(self, **config):
        print("IBMCOSBuilder:Calling __call__::{}".format(self._instance))
        if not self._instance:
            self.connect(**config)

        print("IBMCOSBuilder:Calling __call__::self._instance::", self._instance)

    @validate_input(schema=schema_connect)
    def connect(self, **config):
        print("IBMCOSBuilder:Calling connect")

        ibm_api_key_id = config.get("IBM_COS_API_KEY_ID")
        ibm_service_instance_id = config.get("IBM_COS_RESOURCE_CRN")
        ibm_auth_endpoint = config.get("IBM_COS_AUTH_ENDPOINT")
        signature_version = config.get("IBM_COS_SIGNATURE_VERSION")
        ibm_endpoint_url = config.get("IBM_COS_ENDPOINT")

        self._instance = ibm_boto3.resource("s3", ibm_api_key_id=ibm_api_key_id,
                                            ibm_service_instance_id=ibm_service_instance_id,
                                            ibm_auth_endpoint=ibm_auth_endpoint,
                                            config=Config(
                                                signature_version=signature_version),
                                            endpoint_url=ibm_endpoint_url)

    """save method"""

    def save(self):
        print("IBMCOSBuilder:Calling save::", self._instance)

    """get method"""

    def get(self):
        print("IBMCOSBuilder:Calling get")

    """list method"""

    def list(self):
        print("IBMCOSBuilder:Calling list")

    """delete method"""

    def delete(self):
        print("IBMCOSBuilder:Calling delete")
