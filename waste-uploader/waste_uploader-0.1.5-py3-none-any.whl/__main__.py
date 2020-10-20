import requests
import json
import ast
import logging
import os
import sys
import ntpath
from aws_requests_auth.aws_auth import AWSRequestsAuth
from time import time
from collections import namedtuple
from urllib.parse import urlencode
from waste_uploader.data.bundle import Bundle, BundleSchema

# [init logging]
log = logging.getLogger("logger")
logging.basicConfig(level=logging.INFO)

ALL_VARS = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'PROJECT', 'STAGE', 'PLATFORM', 'VERSION', 'BUILD_NUM',
            'RELEASE_NOTES', 'FILE_PATH', 'BUNDLE_ID']

SLACK_VARS = ['SLACK_URL', 'APP_ICON_URL']

API_GATEWAY_HOST = 'vcgdkujh6d.execute-api.eu-central-1.amazonaws.com'
API_GATEWAY_URL = "https://" + API_GATEWAY_HOST

UploadReq = namedtuple('UploadReq', 'upload_url data file_hash')


def check_variables(env_vars):
    check_result = 'success'
    for i in env_vars:
        if i not in os.environ:
            log.info("Please pass " + i + " as environment variable")
            check_result = 'failed'
    return check_result


def aws_auth():
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    auth = AWSRequestsAuth(aws_access_key=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                           aws_host=API_GATEWAY_HOST,
                           aws_region='eu-central-1',
                           aws_service='execute-api')
    log.info("auth successful")
    return auth


def request_upload(auth, custom_name, file_name, bundle: Bundle) -> UploadReq:
    request_upload_url = f'{API_GATEWAY_URL}/prod/upload?project={bundle.project}&platform={bundle.platform}'
    payload = {'custom_name': custom_name, 'file_name': file_name}
    req = requests.post(request_upload_url, verify=True, auth=auth, json=payload)
    if req.status_code == 200:
        json_data = req.json()
        json_data['file_hash'] = json_data['file_hash'].strip('"')
        upload_req = UploadReq(**json_data)
        log.info("upload url successfully requested")
        return upload_req
    else:
        log.info(f'problem with requesting upload url, status code: {req.status_code}')
        raise RuntimeError("upload_url api send non-200 code, check api, lambda or permissions")


def upload(upload_req: UploadReq, file_path):
    files = {'file': open(file_path, 'rb')}
    http_response = requests.post(upload_req.upload_url, data=upload_req.data, files=files)
    if http_response.status_code != 204:
        log.info(f'problem with requesting upload url, status code: {http_response.status_code}')
        raise RuntimeError("upload finished with non-204 code, so it looks like something went wrong")


def distribute(auth, custom_name, file_name, bundle: Bundle, file_hash):
    bundle_sch = BundleSchema()
    params = bundle_sch.dump(bundle)
    del(params['release_notes'])
    del(params['file_path'])
    params.update({
        'file_hash': file_hash
    })
    payload = {'release_notes': bundle.release_notes, 'custom_name': custom_name, 'file_name': file_name }
    try:
        req = requests.post(f'{API_GATEWAY_URL}/prod/distribute', verify=True, json=payload, auth=auth, params=params)
        response_dict2 = req.json()
        check = response_dict2['message']
        logging.info(f'Commit upload status check: {check}')
        if check != "passed":
            log.error(f'distribute status: {check}')
            raise RuntimeError('release distribution failed, check lambda error log')
        elif check == "passed":
            log.info("release distributed")
        return check
    except Exception as e:
        log.exception(f'There is exception during distributing binary: {e}')
        log.info("problem with release distribution")


def notify(auth, bundle: Bundle, file_hash):
    slack_url = os.environ['SLACK_URL']
    app_icon_url = os.environ['APP_ICON_URL']
    notify_url = API_GATEWAY_URL + "/prod/" + "notify"
    bundle_sch = BundleSchema()
    payload = bundle_sch.dump(bundle)
    payload.update({
        'slack_url': slack_url,
        'app_icon_url': app_icon_url,
        'file_hash': file_hash
    })
    n = requests.post(notify_url, verify=True, json=payload, auth=auth)
    result = n.json()['status']
    if result == "ok":
        log.info("slack alert sent")
    else:
        log.info(f'problem with slack alert, details: {result}')

# [START run]


def main():
    start = time()
    check_result = check_variables(ALL_VARS)
    if check_result == 'success':
        env_data = {k.lower(): v for k, v in os.environ.items()}
        bundle_sch = BundleSchema()
        bundle = bundle_sch.load(env_data)
        auth = aws_auth()
        file_path = os.environ['FILE_PATH']
        custom_name = 'false'
        file_name = 'nothing'
        if 'CUSTOM_NAME' in os.environ:
            custom_name = os.environ['CUSTOM_NAME']
            file_name = ntpath.basename(file_path)
        upload_req = request_upload(auth, custom_name, file_name, bundle)
        upload(upload_req, file_path)
        distribute(auth, custom_name, file_name, bundle, upload_req.file_hash)
        slack_check_result = check_variables(SLACK_VARS)
        if slack_check_result == 'success':
            notify(auth, bundle, upload_req.file_hash)
        else:
            log.info("slack alert is not sent because not all required variables are set")
        logging.info(time() - start)
        download_url = ""
        if bundle.platform == 'ios':
            download_url = f'https://wasted.mpgames.rocks/prep_ios_link/{upload_req.file_hash}'
        elif bundle.platform == 'android':
            download_url = f'https://wasted.mpgames.rocks/download/{upload_req.file_hash}.apk'
        print(json.dumps({'download_url': download_url}))
    else:
        logging.info(time() - start)
        raise RuntimeError("set variable(s) above and try again")


if __name__ == "__main__":
    main()
# [END run]
