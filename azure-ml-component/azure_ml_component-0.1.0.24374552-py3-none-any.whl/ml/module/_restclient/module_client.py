# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Access ModuleClient"""

import json
import uuid
import logging
import os

from contextlib import contextmanager
from requests import Session, Request, HTTPError
from urllib.parse import quote
from html import unescape
from io import BytesIO

from azureml._restclient.workspace_client import WorkspaceClient
from azureml._base_sdk_common import _ClientSessionId
from azureml._base_sdk_common.user_agent import get_user_agent
from azure.ml.component._cli.status_indicator import status_indicator


module_client_logger = logging.getLogger(__name__)


class ServiceError(Exception):
    """General error when interacting with the http server."""

    def __init__(self, message):
        super().__init__(message)


class ModuleServiceError(ServiceError):
    """General error when interacting with the module service."""

    def __init__(self, error_code=None, message=None, http_status_code=None, http_reason=None):
        super().__init__(message)
        self._error_code = error_code
        self._message = message
        self._http_status_code = http_status_code
        self._http_reason = http_reason

    @classmethod
    def from_http_error(cls, e: HTTPError):
        res = e.response
        error_code = None
        message = None
        http_status_code = res.status_code
        http_reason = res.reason

        json = res.json()
        if json:
            dct = json.get('error', None)
            if dct is not None:
                error_code = dct.get('code')
                # Server encodes the error message using XML,
                # e.g `\r\n` will be encoded as `&#xD;&#xA;`.
                # We need to unescape them here.
                message = unescape(dct.get('message'))
        else:
            message = res.text

        # This is for catching conflict error.
        constructor = cls if error_code != 'AzureMLModuleVersionAlreadyExist' else ModuleAlreadyExistsError
        return constructor(
            error_code=error_code,
            message=message,
            http_status_code=http_status_code,
            http_reason=http_reason,
        )

    @property
    def error_code(self):
        return self._error_code

    @property
    def message(self):
        return self._message

    @property
    def http_status_code(self):
        return self._http_status_code

    @property
    def http_reason(self):
        """The reason code returned from http

           e.g. 'Not Found', 'Internal Service Error'.
        """
        return self._http_reason

    @property
    def is_user_error(self):
        return 400 <= self.http_status_code < 500


class ModuleAlreadyExistsError(ModuleServiceError):
    pass


class _HookedBytesIO(object):
    def __init__(self, initial_bytes, on_read_callback=None):
        self._underlying = BytesIO(initial_bytes)
        self._total_len = len(initial_bytes)
        self._cb_on_read = on_read_callback

    def read(self, size=None):
        result = self._underlying.read(size)
        self._on_read()
        return result

    def close(self):
        self._underlying.close()

    @property
    def total_len(self):
        return self._total_len

    @property
    def curr_pos(self):
        return self._underlying.tell()

    def _on_read(self):
        if self._cb_on_read:
            self._cb_on_read(self)


class BaseHttpClient:
    def __init__(self, logger=None):
        if logger:
            self._logger = logger
        elif not self._logger:
            self._logger = module_client_logger

    def _url_open(self, method, url, *, headers=None, dct=None, files=None, stream=False, on_send_progress=None):
        with Session() as session:
            method = method.upper()
            json = dct if dct else None
            if isinstance(files, dict):
                # If contains files, merge `dct` to `files` to make a multi-part request.
                files = self.merge_dct_to_files(dct, files)

            req = Request(method=method, url=url,
                          headers=headers, files=files, json=json)
            prep = session.prepare_request(req)

            request_id = headers.get('x-ms-client-request-id') if headers else None
            self._logger.info('>>> {0} {1} (RequestId: {2})'.format(method, prep.url, request_id))
            self._logger.debug('>>> Headers:')
            for k, v in prep.headers.items():
                if k == 'Authorization':
                    v = '(token hidden)'
                self._logger.debug('... {0}: {1}'.format(k, v))
            if dct:
                self._logger.debug('>>> Data:')
                for k, v in dct.items():
                    self._logger.debug('... {0}: {1}'.format(k, v))
            if files:
                self._logger.debug('>>> Files:')
                for k, v in files.items():
                    self._logger.debug('... {0}: {1}'.format(k, v))

            # The following 2 lines is for debug usage only.
            # self._logger.debug('>>> Body:')
            # self._logger.debug(prep.body)

            if prep.body and isinstance(prep.body, bytes) and on_send_progress:
                prep.body = _HookedBytesIO(prep.body, on_read_callback=on_send_progress)

            res = session.send(prep, stream=stream)

            self._logger.info("<<< {0} {1} (Elapsed {2})".format(res.status_code, res.reason, res.elapsed))

            self._logger.debug('<<< Headers:')
            for k, v in res.headers.items():
                self._logger.debug('... {0}: {1}'.format(k, v))

            if res.status_code >= 300:
                self._logger.debug("<<< {0}".format(res.text))

            res.raise_for_status()
        return res

    def merge_dct_to_files(self, dct=None, files=None):
        return {**dct, **files}

    @status_indicator(action_name="Downloading", indicator_var_name='indicator')
    def download_file(self, url, file_name, indicator=None):
        res = self._url_open("GET", url, stream=True)

        content_len = int(res.headers.get('Content-Length', 0))
        download_len = 0

        self._logger.debug("Create file: {0}".format(file_name))
        with open(file_name, 'wb') as fp:
            # from document, chunk_size=None will read data as it arrives in whatever size the chunks are received.
            # UPDATED: chunk_size could not be None since it will return the whole content as one chunk only
            #          due to the implementation of urllib3, thus the progress bar could not displayed correctly.
            #          Changed to a chunk size of 1024.
            for buf in res.iter_content(chunk_size=1024):
                fp.write(buf)
                download_len += len(buf)
                if indicator:
                    indicator.update(message="Downloading", total_val=content_len, value=download_len)
        self._logger.debug("Download complete.")


class BaseModuleClient(WorkspaceClient, BaseHttpClient):
    """A client to communicate with the studio core services, which manages the modules."""

    def __init__(self, service_context, *, parent_logger=None, **kwargs):
        """
        Constructor of the class.
        """
        super(BaseModuleClient, self).__init__(service_context, _parent_logger=parent_logger, **kwargs)

    def get_rest_client(self, user_agent=None):
        """get service rest client"""
        return self._service_context._get_designer_restclient(user_agent=user_agent)

    @property
    def _base_url(self):
        cluster_address = self.get_cluster_url()
        cluster_address = os.environ.get('MODULE_CLUSTER_ADDRESS', default=cluster_address)
        # Module api does not contain the following part in url, so remove them.
        workspace_address = self.get_workspace_uri_path().replace('/providers/Microsoft.MachineLearningServices', '')

        return cluster_address + '/module/v1.0' + workspace_address

    def generate_headers(self):
        headers = self.auth.get_authentication_header()
        headers.update({
            'User-Agent': get_user_agent(),
            'x-ms-client-session-id': _ClientSessionId,
            'x-ms-client-request-id': str(uuid.uuid4()),
        })
        return headers

    def error_wrapper(self, e: HTTPError):
        error = ModuleServiceError.from_http_error(e)
        if isinstance(error, ModuleAlreadyExistsError):
            return error

        if error.is_user_error:
            text = error.message
        else:
            text = '{0} {1}: {2}'.format(error.http_status_code, error.http_reason, error.message)
            request_id = e.response.headers.get('x-ms-client-request-id')
            if request_id:
                text = '{text} (RequestId: {request_id})'.format(text=text, request_id=request_id)

        return ServiceError(text)

    def _send_request(self, method, url, *, dct=None, files=None, query_params=None, on_send_progress=None,
                      headers=None):
        default_headers = self.generate_headers()
        if headers is not None:
            headers.update(default_headers)
        else:
            headers = default_headers
        full_url = self._base_url if url is None else '{0}/{1}'.format(self._base_url, url)
        if query_params:
            query_string = '&'.join("%s=%s" % (key, quote(val, safe='')) for key, val in query_params.items())
            full_url = '{0}?{1}'.format(full_url, query_string)
        try:
            res = self._url_open(method, full_url, headers=headers, dct=dct, files=files,
                                 on_send_progress=on_send_progress)
            return res.text
        except HTTPError as e:
            res = e.response
            wrapped = self.error_wrapper(e)
            raise e if wrapped is e else wrapped
        except BaseException as e:
            raise ServiceError("Got error {0}: '{1}' while performing {2} {3}"
                               .format(e.__class__.__name__, e, method, full_url)) from e

    def merge_dct_to_files(self, dct=None, files=None):
        dct = dct or {}
        # Must set to None otherwise server-side will fail to get the data.
        filename_for_dct = None
        merged_dct = {'properties': (filename_for_dct, json.dumps(dct))}
        return {**files, **merged_dct}

    def post(self, url=None, dct=None, files=None, query_params=None, on_send_progress=None):
        return self._send_request('POST', url, dct=dct, files=files, query_params=query_params,
                                  on_send_progress=on_send_progress)

    def put(self, url=None, dct=None, files=None):
        return self._send_request('PUT', url, dct=dct, files=files)

    def patch(self, url=None, dct=None, files=None):
        return self._send_request('PATCH', url, dct=dct, files=files)

    def get(self, url='', query_params=None, headers=None):
        return self._send_request('GET', url, query_params=query_params, headers=headers)


class ModuleSourcePayload:

    def __init__(self, source):
        self._source = source

    @contextmanager
    def open(self, spec_only=False):
        from azure.ml.module._module import ModuleSourceType, ModuleWorkingMechanism
        if self._source.source_type == ModuleSourceType.Local:
            snapshot = self._source.snapshot
            zip_file = snapshot.create_spec_snapshot() if spec_only else snapshot.create_snapshot()
            # Always hard code ModuleWorkingMechanism to 'OutputToDataset' per SMT requirements
            with open(zip_file, 'rb') as f:
                self._data = {
                    'ModuleSourceType': self._source.source_type.value,
                    'YamlFile': self._source.spec_file,
                    'ModuleWorkingMechanism': ModuleWorkingMechanism.OutputToDataset.value,
                }
                self._files = {'SnapshotSourceZipFile': f}
                yield self
        elif self._source.source_type == ModuleSourceType.GithubFile:
            self._data = {
                'ModuleSourceType': self._source._source_type.value,
                'YamlFile': self._source._spec_file,
                'ModuleWorkingMechanism': ModuleWorkingMechanism.OutputToDataset.value,
            }
            self._files = {}
            yield self
        elif self._source.source_type == ModuleSourceType.DevopsArtifacts:
            self._data = {
                'ModuleSourceType': self._source._source_type.value,
                'YamlFile': self._source._spec_file,
                'DevopsArtifactsZipUrl': self._source._package_zip,
                'ModuleWorkingMechanism': ModuleWorkingMechanism.OutputToDataset.value,
            }
            self._files = {}
            yield self

    @property
    def data(self):
        return self._data

    @property
    def files(self):
        return self._files


class ModuleClient(BaseModuleClient):
    """Registry to register module to specific workspace, used for custom modules."""

    DEFAULT_NAMESPACE_PLACEHOLDER = '-'

    def _format_url(self, url, *, module_name=None, namespace=None):
        base_url = ''
        if module_name:
            if namespace is None:
                namespace = self.DEFAULT_NAMESPACE_PLACEHOLDER
            # Currently we use quote to avoid problem of '/'
            base_url = base_url + 'namespaces/' + quote(namespace, safe="") + \
                '/modules/' + quote(module_name, safe="") + '/'

        result_url = base_url + url if url else base_url

        return result_url

    @status_indicator('Retrieving')
    def list_modules(self, include_disabled=False):
        return self._get_modules_with_pagination(include_disabled=include_disabled)

    def _get_modules_with_pagination(self, include_disabled=False, headers=None):
        query_params = {'activeOnly': 'false'} if include_disabled else None
        res = json.loads(self.get(query_params=query_params, headers=headers))
        modules = res.get('value')
        if res.get('continuationToken'):
            continuation_header = {'continuationToken': res.get('continuationToken')}
            modules += self._get_modules_with_pagination(include_disabled=include_disabled,
                                                         headers=continuation_header)
        return modules

    def _get_module(self, module_name, *, namespace=None, version=None):
        url = self._format_url(url='', module_name=module_name, namespace=namespace)
        query_params = {'version': version} if version else None
        return json.loads(self.get(url, query_params=query_params))

    @status_indicator('Retrieving')
    def get_module(self, module_name, *, namespace=None, version=None):
        return self._get_module(module_name, namespace=namespace, version=version)

    @status_indicator('Validating')
    def validate_module(self, module_source):
        parsed_module = self._parse_module(module_source)
        entry = parsed_module.get('entry', '')
        if module_source.is_invalid_entry(entry):
            msg = "Entry file '%s' doesn't exist in source directory." % entry
            raise ServiceError(msg)
        return parsed_module

    def _parse_module(self, module_source):
        url = self._format_url('parse')
        with ModuleSourcePayload(module_source).open(spec_only=True) as payload:
            result = self.post(url, dct=payload.data, files=payload.files)
            return json.loads(result)

    @status_indicator('Registering', indicator_var_name="indicator")
    def _create_or_upgrade_module(self, module_source, *, set_as_default=False, overwrite_module_version=None,
                                  indicator=None):
        def on_send_progress_callback(body):
            if 0 <= body.curr_pos / body.total_len < 1:
                indicator.update(message="Uploading", total_val=body.total_len, value=body.curr_pos)
            else:
                indicator.update("Registering")

        with ModuleSourcePayload(module_source).open() as payload:
            query = {
                'upgradeIfExists': 'true',
                'SetAsDefaultVersion': str(set_as_default),
            }
            if overwrite_module_version:
                query.update({'overwriteModuleVersion': overwrite_module_version})
            result = self.post(dct=payload.data, files=payload.files, query_params=query,
                               on_send_progress=on_send_progress_callback if indicator else None)
            result_dct = json.loads(result)

            if not result_dct.get('isDefaultModuleVersion'):
                version = result_dct.get('moduleVersion')
                default_version = result_dct.get('defaultVersion')
                # TODO: module -> component here
                self._logger.warning(
                    'Registered new version %s, but the module default version kept to be %s.\n'
                    'Use "az ml module set-default-version" or "az ml module register --set-as-default-version" '
                    'to set default version.', version, default_version)
            return result_dct

    def create_or_upgrade_module(self, module_source, *, set_as_default=False, overwrite_module_version=None):
        if module_source.is_local_source():
            self.validate_module(module_source)
        return self._create_or_upgrade_module(module_source, set_as_default=set_as_default,
                                              overwrite_module_version=overwrite_module_version)

    @status_indicator('Updating')
    def _patch_module(self, module_name, update_type, namespace=None, data=None):
        data = {} if data is None else data
        data = {**data, **{'ModuleUpdateOperationType': update_type}}
        url = self._format_url(url='', module_name=module_name, namespace=namespace)
        patched_result = json.loads(self.patch(url=url, dct=data))
        # The PATCH api will not return full data of the updated module,
        # so we do a GET operation here.
        module_name = patched_result.get('moduleName')
        namespace = patched_result.get('namespace')
        return self._get_module(module_name=module_name, namespace=namespace)

    def set_module_default_version(self, module_name, version, namespace=None):
        data = {
            'ModuleVersion': version,
        }
        return self._patch_module(module_name, update_type='SetDefaultVersion', namespace=namespace, data=data)

    def enable_module(self, module_name, namespace=None):
        return self._patch_module(module_name, update_type='EnableModule', namespace=namespace)

    def disable_module(self, module_name, namespace=None):
        return self._patch_module(module_name, update_type='DisableModule', namespace=namespace)

    @status_indicator('Retrieving')
    def get_snapshot_url(self, module_name, namespace=None, version=None):
        url = self._format_url(url='snapshotUrl', module_name=module_name, namespace=namespace)
        # The response is currently a string, so do not need to decode by json
        query_params = {'version': version} if version else None
        return self.get(url, query_params=query_params)

    @status_indicator('Retrieving')
    def get_module_yaml(self, module_name, namespace=None, version=None):
        url = self._format_url(url='yaml', module_name=module_name, namespace=namespace)
        # The response is currently a string, so do not need to decode by json
        query_params = {'version': version} if version else None
        return self.get(url, query_params=query_params)
