import os
import base64
from bizai.framework.services.impl.executors.newrequestsvc import NewRequestStepExecutor
from bizai.framework.services.impl.requestmanagersvc import RequestManagerImpl

from bizai.framework.utils import cosutils, db2utils

"""Class dedicated to Invoker"""


class Invoker:

    """command method"""

    def set_manager(self, manager):
        self._manager = manager

    """execute method"""

    def run(self, **input):
        self._manager.process(**input)


"""main method"""
# python -m bizai.framework.services.impl.invokersvc
if __name__ == "__main__":

    file = "/Users/arun.wagle@ibm.com/Personal/Projects/Projects/BizAI/bizai-content/content/test/20191219184246514442000000_Freehold Management Company - Ironshore Quote.pdf"
    filename, file_type = os.path.splitext(file)
    file_name = os.path.basename(file)
    in_file = open(file, "rb")
    data = in_file.read()
    # print(data)
    base64_encoded_file_bytes = base64.b64encode(data)

    # tmp_output_filename_key = None
    bucket_name = "bizai-contracts"
    # file_bytes = base64.b64decode(base64_encoded_file_bytes)
    # tmp_output_filename_key = 'client_id_1/tmp/{}'.format(file_name)

    # bucket_name = "bizai-contracts"
    # return_val = cosutils.save_file(
    #     bucket_name, tmp_output_filename_key, file_bytes)

    param = {
        "client": {
            "client_id": 1,
            "client_engagement_id": 1,
            "user_id": "vikas.swami92@gmail.com"
        },
        "request": {
            "execution_flow": "Training",
            "request_type": "RT_NER_PROCESS"
        },
        "object_storage": {
            "bucket_name": bucket_name,
            "file_name": file_name,
            "base64_encoded_file_bytes": base64_encoded_file_bytes
        }

    }
   
    """create StepExecutor object"""
    step_executor = NewRequestStepExecutor()
    request_manager = RequestManagerImpl(step_executor)

    invoker = Invoker()
    invoker.set_manager(request_manager)
    invoker.run(**param)
