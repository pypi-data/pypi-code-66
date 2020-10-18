from bizai.framework.services.bizaimanager import BizaiManager

"""Class dedicated to Command Implementation"""


class RequestManagerImpl(BizaiManager):

    """constructor method"""

    def __init__(self, step_executor):
        print("RequestManagerImpl::init")
        self._step_executor = step_executor
    
    """process method"""

    def process(self, **input):
        # print("RequestManagerImpl::process::self._input ", input)
        self._step_executor.execute(**input)
        