# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from enum import Enum
import sys
import inspect
import importlib
from azure.ml.component._restclients.exceptions import ComponentServiceError
from azureml.exceptions._azureml_exception import UserErrorException


class ErrorCategory(Enum):
    # This error indicates that the user provided data is incorrect and causes backend 40x exception
    MTUserError = 'MTUserError'
    SDKUserError = 'SDKUserError'  # This error indicates that the user provided parameter doesn't pass validation
    CustomerUserError = 'CustomerUserError'  # This error indicates that the user's code has errors

    MTError = 'MTError'  # This error indicates that backend has some problems
    InternalSDKError = 'InternalSDKError'  # This error indicates that our package has some problems
    ExternalSDKError = 'ExternalSDKError'  # This error indicates that some dependent packages has problems


def _is_func(frame, module, func_name):
    if frame is None:
        return False
    code = frame.f_code
    mod = importlib.import_module(module)
    return code.co_filename == inspect.getfile(mod) and code.co_name == func_name


def _is_dsl_pipeline_customer_code_error():
    """Check whether the error is raised by customer code in dsl.pipeline"""
    _, _, traceback = sys.exc_info()
    if traceback is None:
        return False
    while traceback.tb_next is not None:
        traceback = traceback.tb_next
    last_frame = traceback.tb_frame.f_back
    module, func_name = 'azure.ml.component.dsl.pipeline', 'construct_sub_pipeline'
    # Return True if the last frame of the traceback frame is construcing sub pipeline.
    return _is_func(last_frame, module, func_name)


def get_error_category(e: Exception):
    if isinstance(e, UserErrorException):
        return ErrorCategory.SDKUserError
    if _is_dsl_pipeline_customer_code_error():
        return ErrorCategory.CustomerUserError
    if isinstance(e, ComponentServiceError):
        if str(e.http_status_code).startswith('40'):
            # Currently all the 400/401/403/404s are treated as UserErrors.
            # Maybe it could be refined in the future according to more detailed information.
            return ErrorCategory.MTUserError
        return ErrorCategory.MTError
    return ErrorCategory.InternalSDKError
