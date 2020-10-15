# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import requests
from ibm_watson_machine_learning.utils import SPACES_DETAILS_TYPE, INSTANCE_DETAILS_TYPE, MEMBER_DETAILS_TYPE,DATA_ASSETS_DETAILS_TYPE, STR_TYPE, STR_TYPE_NAME, docstring_parameter, meta_props_str_conv, str_type_conv, get_file_from_cos
from ibm_watson_machine_learning.metanames import VolumeMetaNames
from ibm_watson_machine_learning.wml_resource import WMLResource
from ibm_watson_machine_learning.wml_client_error import WMLClientError, ApiRequestFailure
import os

_DEFAULT_LIST_LENGTH = 50


class Volume(WMLResource):
    """
    Store and manage your scripts assets.

    """
    ConfigurationMetaNames = VolumeMetaNames()
    """MetaNames for script Assets creation."""

    def __init__(self, client):
        WMLResource.__init__(self, __name__, client)
        self._ICP = client.ICP

    @docstring_parameter({'str_type': STR_TYPE_NAME})
    def get_details(self, volume_name):
        """
            Get Volume  details.

            **Parameters**

            .. important::
                #. **volume_name**: Unique name  of the volume\n
                   **type**: str\n

            **Output**

            .. important::
                **returns**: Metadata of the volume details \n
                **return type**: dict\n

            **Example**

             >>> volume_details = client.volumes.get_details(volume_name)

        """
        Volume._validate_type(volume_name, u'volume_name', STR_TYPE, True)


        if not self._ICP:
            response = requests.get(self._href_definitions.volume_href(volume_name),
                                    headers=self._client._get_zen_headers())
        else:
            response = requests.get(self._href_definitions.volume_href(volume_name),
                                      headers=self._client._get_zen_headers(), verify=False)
        if response.status_code == 200:
            return response

        else:
            raise WMLClientError("Failed to Get the volume details. Try again.")

        #     response = self._get_required_element_from_response(self._handle_response(200, u'get asset details', response))
        #
        #     if not self._client.CLOUD_PLATFORM_SPACES and not self._client.ICP_PLATFORM_SPACES:
        #         return response
        #     else:
        #
        #         entity = response[u'entity']
        #
        #         try:
        #             del entity[u'script'][u'ml_version']
        #         except KeyError:
        #             pass
        #
        #         final_response = {
        #             "metadata": response[u'metadata'],
        #             "entity": entity
        #         }
        #
        #         return final_response
        #
        # else:
        #     return self._handle_response(200, u'get asset details', response)

    @docstring_parameter({'str_type': STR_TYPE_NAME})
    def create(self, meta_props):
        """
                Creates a Volume asset.

                **Parameters**

                .. important::
                   #. **meta_props**:  Name to be given to the Volume asset\n

                      **type**: dict\n

                **Output**

                .. important::

                    **returns**: metadata of the created volume details\n
                    **return type**: dict\n

                **Example**
                Provision new PVC volume :
                 >>> metadata = {
                 >>>        client.volumes.ConfigurationMetaNamess.NAME: 'volume-for-wml-test',
                 >>>        client.volumes.ConfigurationMetaNames.NAMESPACE: 'wmldev2',
                 >>>        client.volumes.ConfigurationMetaNames.STORAGE_CLASS: 'nfs-client'
                 >>>        client.volumes.ConfigurationMetaNames.STORAGE_SIZE: "2G"
                 >>>    }
                 >>>
                 >>> asset_details = client.scripts.store(meta_props=metadata)

               Provision a Existing PVC volume:

                 >>> metadata = {
                 >>>        client.volumes.ConfigurationMetaNamess.NAME: 'volume-for-wml-test',
                 >>>        client.volumes.ConfigurationMetaNames.NAMESPACE: 'wmldev2',
                 >>>        client.volumes.ConfigurationMetaNames.EXISTING_PVC_NAME: 'volume-for-wml-test'
                 >>>    }
                 >>>
                 >>> asset_details = client.scripts.store(meta_props=metadata)

        """
        if not self._client.CLOUD_PLATFORM_SPACES and not self._client.ICP_PLATFORM_SPACES:
            raise WMLClientError("Failed to create volume. It is supported only for CP4D 3.5")

        volume_meta = self.ConfigurationMetaNames._generate_resource_metadata(
            meta_props,
            with_validation=True,
            client=self._client
        )

        create_meta = {}
        if self.ConfigurationMetaNames.EXISTING_PVC_NAME in meta_props and \
            meta_props[self.ConfigurationMetaNames.EXISTING_PVC_NAME] is not None:
            if self.ConfigurationMetaNames.STORAGE_CLASS in meta_props and \
                    meta_props[self.ConfigurationMetaNames.STORAGE_CLASS] is not None:
                raise WMLClientError("Failed while creating volume. Either provide EXISTING_PVC_NAME to create a volume using existing volume or"
                                     "provide STORAGE_CLASS and STORAGE_SIZE for new volume creation")
            else:
                create_meta.update({ "existing_pvc_name": meta_props[self.ConfigurationMetaNames.EXISTING_PVC_NAME]})
        else:
            if self.ConfigurationMetaNames.STORAGE_CLASS in meta_props and \
               meta_props[self.ConfigurationMetaNames.STORAGE_CLASS] is not None:
               if self.ConfigurationMetaNames.STORAGE_SIZE in meta_props and \
                       meta_props[self.ConfigurationMetaNames.STORAGE_SIZE] is not None:
                   create_meta.update({"storageClass": meta_props[self.ConfigurationMetaNames.STORAGE_CLASS]})
                   create_meta.update({"storageSize": meta_props[self.ConfigurationMetaNames.STORAGE_SIZE]})
               else:
                   raise WMLClientError("Failed to create volume. Missing input STORAGE_SIZE" )

        if meta_props[self.ConfigurationMetaNames.EXISTING_PVC_NAME] is not None:
            input_meta = {
                "addon_type":"volumes",
                "addon_version":"-",
                "create_arguments":{
                    "metadata":create_meta
                },
                "namespace":meta_props[self.ConfigurationMetaNames.NAMESPACE],
                "display_name":meta_props[self.ConfigurationMetaNames.NAME]
            }
        else:
            input_meta = {
                "addon_type": "volumes",
                "addon_version": "-",
                "create_arguments": {
                    "metadata": create_meta
                },
                "namespace": meta_props[self.ConfigurationMetaNames.NAMESPACE],
                "display_name": meta_props[self.ConfigurationMetaNames.NAME]
            }
        creation_response = {}
        try:
            if self._client.CLOUD_PLATFORM_SPACES:
                creation_response = requests.post(
                    self._href_definitions.volumes_href(),
                    headers=self._client._get_zen_headers(),
                    json=input_meta
                )

            else:
                creation_response = requests.post(self._href_definitions.volumes_href(),
                        headers=self._client._get_headers(zen=True),
                        json=input_meta,
                        verify=False
                    )
            if creation_response.status_code == 200:
                volume_id_details = creation_response.json()
                import copy
                volume_details = copy.deepcopy(input_meta)
                volume_details.update(volume_id_details)
                return volume_details
            else:
                print(creation_response.status_code, creation_response.text)
        except Exception as e:
            print("Exception: ", {e})
            raise WMLClientError("Failed to create a volume. Try again.")



    def start(self, name):
        if not self._client.ICP_PLATFORM_SPACES and not self._client.CLOUD_PLATFORM_SPACES:
            raise WMLClientError("Volume APIs are not supported. It is supported only for CP4D 3.5")
        start_url = self._href_definitions.volume_service_href(name)
        # Start the volume  service
        start_data = {}
        try:
            if not self._ICP:
                start_data = {}
                creation_response = requests.post(
                    start_url,
                    headers=self._client._get_headers(zen=True),
                    json=start_data
                )
            else:
                creation_response = requests.post(
                   start_url,
                    headers=self._client._get_headers(zen=True),
                    json=start_data,
                    verify=False
                )
            if creation_response.status_code == 200:
                print("Volume Service started")
            elif creation_response.status_code == 500:
                print("Failed to start the volume. Make sure volume is in running with status RUNNING or UNKNOW and then re-try")
            else:
                print(creation_response.status_code, creation_response.text)
        except Exception as e:
            print("Exception:" + {e})
            raise WMLClientError("Failed to start the file to  volume. Try again.")

    def upload_file(self, name,  file_path):

        if not self._client.ICP_PLATFORM_SPACES and not self._client.CLOUD_PLATFORM_SPACES:
            raise WMLClientError("Volume APIs are not supported. It is supported only for CP4D 3.5")
        filename = file_path.split('/')[-1]
        upload_url = self._href_definitions.volume_upload_href(name) + 'wml-client/'+ filename
        # Start the volume  service
        files = {'file': open(file_path, 'rb')}
        if not self._ICP:
            files = {'file': open(file_path, 'rb')}
            upload_response = requests.put(
                upload_url,
                headers=self._client._get_headers(zen=True),
                file=files
                )
        else:
            upload_response = requests.put(
                upload_url,
                headers=self._client._get_headers(zen=True),
                file=files,
                verify=False
            )
        if upload_response.status_code == 200:
            print(u'Successfully uploaded file to the Volume : \'{}\''.format(name))
        else:
            raise WMLClientError("Failed to upload the file to  volume. Try again.")


    def list(self):
        """
           List stored scripts. If limit is set to None there will be only first 50 records shown.

           **Parameters**

           .. important::
                #. **limit**:  limit number of fetched records\n
                   **type**: int\n

           **Output**

           .. important::
                This method only prints the list of all script in a table format.\n
                **return type**: None\n

           **Example**

            >>> client.script.list()
        """

        href = self._href_definitions.volumes_href()
        params = {}
        params.update({'addon_type': 'volumes'})
        if not self._ICP:
            response = requests.get(href, params=params, headers=self._client._get_headers(zen=True))
        else:
            response = requests.get(href, params=params, headers=self._client._get_headers(zen=True), verify=False)
        self._handle_response(200, u'list assets', response)
        asset_details = self._handle_response(200, u'list volumes', response)
        return asset_details
        # space_values = [
        #     (m[u'metadata'][u'name'], m[u'metadata'][u'asset_type'], m["metadata"]["asset_id"]) for
        #     m in asset_details]
        #
        # self._list(space_values, [u'NAME', u'ASSET_TYPE', u'ASSET_ID'], None, _DEFAULT_LIST_LENGTH)

    # @docstring_parameter({'str_type': STR_TYPE_NAME})
    # def download(self, asset_uid, filename, rev_uid=None):
    #     """
    #         Download the content of a script asset.
    #
    #         **Parameters**
    #
    #         .. important::
    #              #. **asset_uid**:  The Unique Id of the script asset to be downloaded\n
    #                 **type**: str\n
    #
    #              #. **filename**:  filename to be used for the downloaded file\n
    #                 **type**: str\n
    #
    #              #. **rev_uid**:  Revision id\n
    #                 **type**: str\n
    #
    #         **Output**
    #
    #              **returns**: Path to the downloaded asset content\n
    #              **return type**: str\n
    #
    #         **Example**
    #
    #          >>> client.script.download(asset_uid,"script_file.zip")
    #
    #      """
    #     if rev_uid is not None and self._client.ICP_30 is None and not self._client.CLOUD_PLATFORM_SPACES and not self._client.ICP_PLATFORM_SPACES:
    #         raise WMLClientError(u'Not applicable for this release')
    #
    #     Script._validate_type(asset_uid, u'asset_uid', STR_TYPE, True)
    #     Script._validate_type(rev_uid, u'rev_uid', int, False)
    #
    #     params = self._client._params()
    #
    #     if rev_uid is not None:
    #         params.update({'revision_id': rev_uid})
    #
    #     import urllib
    #     if not self._ICP:
    #         asset_response = requests.get(self._href_definitions.get_asset_href(asset_uid),
    #                                       params=params,
    #                                       headers=self._client._get_headers())
    #     else:
    #         asset_response = requests.get(self._href_definitions.get_data_asset_href(asset_uid),
    #                                       params=params,
    #                                       headers=self._client._get_headers(), verify=False)
    #     asset_details = self._handle_response(200, u'get assets', asset_response)
    #
    #     if self._WSD:
    #         attachment_url = asset_details['attachments'][0]['object_key']
    #         artifact_content_url = self._href_definitions.get_wsd_model_attachment_href() + \
    #                                urllib.parse.quote('script/' + attachment_url, safe='')
    #
    #         r = requests.get(artifact_content_url, params=self._client._params(), headers=self._client._get_headers(),
    #                          stream=True, verify=False)
    #         if r.status_code != 200:
    #             raise ApiRequestFailure(u'Failure during {}.'.format("downloading data asset"), r)
    #
    #         downloaded_asset = r.content
    #         try:
    #             with open(filename, 'wb') as f:
    #                 f.write(downloaded_asset)
    #             print(u'Successfully saved data asset content to file: \'{}\''.format(filename))
    #             return os.getcwd() + "/" + filename
    #         except IOError as e:
    #             raise WMLClientError(u'Saving data asset with artifact_url: \'{}\'  to local file failed.'.format(filename), e)
    #     else:
    #         attachment_id = asset_details["attachments"][0]["id"]
    #         if not self._ICP:
    #             response = requests.get(self._href_definitions.get_attachment_href(asset_uid,attachment_id), params=params,
    #                                     headers=self._client._get_headers())
    #         else:
    #             response = requests.get(self._href_definitions.get_attachment_href(asset_uid,attachment_id), params=params,
    #                                       headers=self._client._get_headers(), verify=False)
    #         if response.status_code == 200:
    #             attachment_signed_url = response.json()["url"]
    #             if 'connection_id' in asset_details["attachments"][0]:
    #                 if not self._ICP:
    #                     att_response = requests.get(attachment_signed_url)
    #                 else:
    #                     att_response = requests.get(attachment_signed_url,
    #                                                 verify=False)
    #             else:
    #                 if not self._ICP:
    #                     att_response = requests.get(attachment_signed_url)
    #                 else:
    #                     att_response = requests.get(self._wml_credentials["url"]+attachment_signed_url,
    #                                             verify=False)
    #             if att_response.status_code != 200:
    #                 raise ApiRequestFailure(u'Failure during {}.'.format("downloading asset"), att_response)
    #
    #             downloaded_asset = att_response.content
    #             try:
    #                 with open(filename, 'wb') as f:
    #                     f.write(downloaded_asset)
    #                 print(u'Successfully saved data asset content to file: \'{}\''.format(filename))
    #                 return os.getcwd() + "/" + filename
    #             except IOError as e:
    #                 raise WMLClientError(u'Saving asset with artifact_url to local file: \'{}\' failed.'.format(filename), e)
    #         else:
    #             raise WMLClientError("Failed while downloading the asset " + asset_uid)

    @staticmethod
    @docstring_parameter({'str_type': STR_TYPE_NAME})
    def get_id(volume_details):
        """
                Get Unique Id of stored volume details.

                **Parameters**

                .. important::

                   #. **asset_details**:  Metadata of the stored volume details\n
                      **type**: dict\n

                **Output**

                .. important::

                    **returns**: Unique Id of stored volume asset\n
                    **return type**: str\n

                **Example**

                     >>> volume_uid = client.volumes.get_id(volume_details)

        """

        Volume._validate_type(volume_details, u'asset_details', object, True)

        return WMLResource._get_required_element_from_dict(volume_details, u'volume_assets_details',
                                                           [u'id'])

    @staticmethod
    @docstring_parameter({'str_type': STR_TYPE_NAME})
    def get_name(volume_details):
        """
                Get Unique Id  of stored script asset. This method is deprecated. Use 'get_id(asset_details)' instead

                **Parameters**

                .. important::

                   #. **asset_details**:  Metadata of the stored script asset\n
                      **type**: dict\n
                      **type**: dict\n

                **Output**

                .. important::

                    **returns**: Unique Id of stored script asset\n
                    **return type**: str\n

                **Example**

                 >>> asset_uid = client.script.get_uid(asset_details)

        """
        Volume._validate_type(volume_details, u'asset_details', object, True)
        return WMLResource._get_required_element_from_dict(volume_details, u'volume_assets_details',
                                                           [u'display_name'])

    @docstring_parameter({'str_type': STR_TYPE_NAME})
    def delete(self, volume_name):
        """
            Delete a volume.

            **Parameters**

            .. important::
                #. **volume_name**:  Unique name of the volume
                   **type**: str\n

            **Output**

            .. important::
                **returns**: status ("SUCCESS" or "FAILED")\n
                **return type**: str\n

            **Example**

             >>> client.volumes.delete(volume_name)

        """
        Volume._validate_type(volume_name, u'asset_uid', STR_TYPE, True)
        if (not self._client.CLOUD_PLATFORM_SPACES and not self._client.ICP_PLATFORM_SPACES):
            raise WMLClientError(u'Volume API is not supported.')

        if not self._ICP:
            response = requests.delete(self._href_definitions.volume_service_href(volume_name),
                                       headers=self._client._get_headers(zen=True))
        else:
            response = requests.delete(self._href_definitions.volume_service_href(volume_name),
                                      headers=self._client._get_headers(zen=True), verify=False)
        if response.status_code == 204 :
            print("Successfully started volume service.")
        else:
             print(response.status_code,response.text)



   #
   #  @docstring_parameter({'str_type': STR_TYPE_NAME})
   #  def _delete(self, asset_uid):
   #      Script._validate_type(asset_uid, u'asset_uid', STR_TYPE, True)
   #
   #      if not self._ICP:
   #          response = requests.delete(self._href_definitions.get_asset_href(asset_uid), params=self._client._params(),
   #                                     headers=self._client._get_headers())
   #      else:
   #          response = requests.delete(self._href_definitions.get_asset_href(asset_uid), params=self._client._params(),
   #                                     headers=self._client._get_headers(), verify=False)
   #
   #