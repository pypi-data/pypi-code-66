import io
import json
import logging
import math
import sys
import threading
import time
import copy
from pathlib import Path

import boto3
from PIL import Image
from tqdm import tqdm

from ..api import API
from ..common import (
    annotation_status_str_to_int, project_type_int_to_str,
    project_type_str_to_int, user_role_int_to_str, user_role_str_to_int
)
from ..exceptions import (
    SABaseException, SAExistingProjectNameException,
    SANonExistingProjectNameException
)
from .annotation_classes import (
    create_annotation_classes_from_classes_json, search_annotation_classes,
    get_annotation_classes_id_to_name, get_annotation_classes_name_to_id,
    fill_class_and_attribute_ids, fill_class_and_attribute_names
)
from .project import get_project_metadata
from .users import get_team_contributor_metadata

logger = logging.getLogger("superannotate-python-sdk")

_api = API.get_instance()
_NUM_THREADS = 10

_RESIZE_CONFIG = {2: 4_000_000, 1: 100_000_000}  # 1: vector 2: pixel


def create_project(project_name, project_description, project_type):
    """Create a new project in the team.

    :param project_name: the new project's name
    :type project_name: str
    :param project_description: the new project's description
    :type project_description: str
    :param project_type: the new project type, Vector or Pixel.
    :type project_type: str

    :return: dict object metadata the new project
    :rtype: dict
    """
    try:
        get_project_metadata(project_name)
    except SANonExistingProjectNameException:
        pass
    else:
        raise SAExistingProjectNameException(
            0, "Project with name " + project_name +
            " already exists. Please use unique names for projects to use with SDK."
        )
    project_type = project_type_str_to_int(project_type)
    data = {
        "team_id": str(_api.team_id),
        "name": project_name,
        "description": project_description,
        "status": 0,
        "type": project_type
    }
    response = _api.send_request(
        req_type='POST', path='/project', json_req=data
    )
    if not response.ok:
        raise SABaseException(
            response.status_code, "Couldn't create project " + response.text
        )
    res = response.json()
    logger.info(
        "Created project %s (ID %s) with type %s", res["name"], res["id"],
        project_type_int_to_str(res["type"])
    )
    return res


def create_project_like_project(
    project_name,
    from_project,
    project_description=None,
    copy_annotation_classes=True,
    copy_settings=True,
    copy_workflow=True,
    copy_project_contributors=False
):
    """Create a new project in the team using annotation classes and settings from from_project.

    :param project_name: new project's name
    :type project_name: str
    :param from_project: the name or metadata of the project being used for duplication
    :type from_project: str or dict
    :param project_description: the new project's description. If None, from_project's
                                description will be used
    :type project_description: str
    :param copy_annotation_classes: enables copying annotation classes
    :type copy_annotation_classes: bool
    :param copy_settings: enables copying project settings
    :type copy_settings: bool
    :param copy_workflow: enables copying project workflow
    :type copy_workflow: bool
    :param copy_project_contributors: enables copying project contributors
    :type copy_project_contributors: bool

    :return: dict object metadata of the new project
    :rtype: dict
    """
    try:
        get_project_metadata(project_name)
    except SANonExistingProjectNameException:
        pass
    else:
        raise SAExistingProjectNameException(
            0, "Project with name " + project_name +
            " already exists. Please use unique names for projects to use with SDK."
        )
    if not isinstance(from_project, dict):
        from_project = get_project_metadata(from_project)
    if project_description is None:
        project_description = from_project["description"]
    data = {
        "team_id": str(_api.team_id),
        "name": project_name,
        "description": project_description,
        "status": 0,
        "type": from_project["type"]
    }
    response = _api.send_request(
        req_type='POST', path='/project', json_req=data
    )
    if not response.ok:
        raise SABaseException(
            response.status_code, "Couldn't create project " + response.text
        )
    res = response.json()
    logger.info(
        "Created project %s (ID %s) with type %s", res["name"], res["id"],
        project_type_int_to_str(res["type"])
    )
    if copy_settings:
        set_project_settings(res, get_project_settings(from_project))
    if copy_annotation_classes:
        create_annotation_classes_from_classes_json(
            res, search_annotation_classes(from_project, return_metadata=True)
        )
        if copy_workflow:
            set_project_workflow(res, get_project_workflow(from_project))
    if copy_project_contributors:
        for user in from_project["users"]:
            share_project(
                res, user["user_id"], user_role_int_to_str(user["user_role"])
            )

    return res


def delete_project(project):
    """Deletes the project

    :param project: project name or metadata of the project to be deleted
    :type project: str or dict
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    team_id, project_id = project["team_id"], project["id"]
    params = {"team_id": team_id}
    response = _api.send_request(
        req_type='DELETE', path=f'/project/{project_id}', params=params
    )
    if not response.ok:
        raise SABaseException(
            response.status_code, "Couldn't delete project " + response.text
        )
    logger.info("Successfully deleted project %s.", project["name"])


def rename_project(project, new_name):
    """Renames the project

    :param project: project name or metadata of the project to be deleted
    :type project: str or dict
    :param new_name: project's new name
    :type new_name: str
    """
    try:
        get_project_metadata(new_name)
    except SANonExistingProjectNameException:
        pass
    else:
        raise SAExistingProjectNameException(
            0, "Project with name " + new_name +
            " already exists. Please use unique names for projects to use with SDK."
        )
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    team_id, project_id = project["team_id"], project["id"]
    params = {"team_id": team_id}
    json_req = {"name": new_name}
    response = _api.send_request(
        req_type='PUT',
        path=f'/project/{project_id}',
        params=params,
        json_req=json_req
    )
    if not response.ok:
        raise SABaseException(
            response.status_code, "Couldn't rename project " + response.text
        )
    logger.info(
        "Successfully renamed project %s to %s.", project["name"], new_name
    )


def get_project_image_count(project):
    """Returns number of images in the project.

    :param project: project name or metadata of the project
    :type project: str or dict

    :return: number of images in the project
    :rtype: int
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    team_id, project_id = project["team_id"], project["id"]
    params = {'team_id': team_id}
    response = _api.send_request(
        req_type='GET',
        path=f'/reporting/project/{project_id}/overview',
        params=params
    )
    if not response.ok:
        raise SABaseException(
            response.status_code,
            "Couldn't get project image count " + response.text
        )
    return response.json()["total_images"]


def upload_images_from_folder_to_project(
    project,
    folder_path,
    extensions=None,
    annotation_status="NotStarted",
    from_s3_bucket=None,
    exclude_file_patterns=None,
    recursive_subfolders=False,
    image_quality_in_editor=None
):
    """Uploads all images with given extensions from folder_path to the project.
    Sets status of all the uploaded images to set_status if it is not None.

    :param project: project name or metadata of the project to upload images_to
    :type project: str or dict
    :param folder_path: from which folder to upload the images
    :type folder_path: Pathlike (str or Path)
    :param extensions: list of filename extensions to include from folder, if None, then "jpg" and "png" are included
    :type extensions: list of str
    :param annotation_status: value to set the annotation statuses of the uploaded images NotStarted InProgress QualityCheck Returned Completed Skipped
    :type annotation_status: str
    :param from_s3_bucket: AWS S3 bucket to use. If None then folder_path is in local filesystem
    :type from_s3_bucket: str
    :param exclude_file_patterns: filename patterns to exclude from uploading,
                                 default value is to exclude SuperAnnotate pixel project
                                 annotation mask output file pattern. If None,
                                 SuperAnnotate related ["___save.png", "___fuse.png"]
                                 will bet set as default exclude_file_patterns.
    :type exclude_file_patterns: list of strs
    :param recursive_subfolders: enable recursive subfolder parsing
    :type recursive_subfolders: bool
    :param image_quality_in_editor: image quality (in percents) that will be seen in SuperAnnotate web annotation editor. If None default value will be used.
    :type image_quality_in_editor: int

    :return: uploaded and not-uploaded images' filepaths
    :rtype: tuple of list of strs
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    if recursive_subfolders:
        logger.warning(
            "When using recursive subfolder parsing same name images in different subfolders will overwrite each other."
        )
    if exclude_file_patterns is None:
        exclude_file_patterns = ["___save.png", "___fuse.png"]
    if extensions is None:
        extensions = ["jpg", "png"]
    elif not isinstance(extensions, list):
        raise SABaseException(
            0,
            "extensions should be a list in upload_images_from_folder_to_project"
        )

    logger.info(
        "Uploading all images with extensions %s from %s to project %s. Excluded file patterns are: %s.",
        extensions, folder_path, project["name"], exclude_file_patterns
    )
    if from_s3_bucket is None:
        paths = []
        for extension in extensions:
            if not recursive_subfolders:
                paths += list(Path(folder_path).glob(f'*.{extension}'))
            else:
                paths += list(Path(folder_path).rglob(f'*.{extension}'))
    else:
        s3_client = boto3.client('s3')
        paginator = s3_client.get_paginator('list_objects_v2')
        response_iterator = paginator.paginate(
            Bucket=from_s3_bucket, Prefix=folder_path
        )

        paths = []
        for response in response_iterator:
            for object_data in response['Contents']:
                key = object_data['Key']
                if not recursive_subfolders and '/' in key[len(folder_path) +
                                                           1:]:
                    continue
                for extension in extensions:
                    if key.endswith(f'.{extension}'):
                        paths.append(key)
                        break
    filtered_paths = []
    for path in paths:
        not_in_exclude_list = [
            x not in Path(path).name for x in exclude_file_patterns
        ]
        if all(not_in_exclude_list):
            filtered_paths.append(path)

    return upload_images_to_project(
        project, filtered_paths, annotation_status, from_s3_bucket,
        image_quality_in_editor
    )


def get_image_array_to_upload(
    byte_io_orig, project_type, image_quality_in_editor
):
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(byte_io_orig)
    im = im.convert("RGB")
    width, height = im.size
    max_size = _RESIZE_CONFIG[project_type]
    if (width * height) > max_size:
        im_format = im.format
        logger.warning("One of the images is being resized to smaller size.")
        max_size_root = math.sqrt(max_size)
        nwidth = math.floor(max_size_root * math.sqrt(width / height))
        nheight = math.floor(max_size_root * math.sqrt(height / width))
        im = im.resize((nwidth, nheight))
        byte_io_orig = io.BytesIO()
        im.save(byte_io_orig, im_format, subsampling=0, quality=100)

    byte_io_lores = io.BytesIO()
    im.save(
        byte_io_lores,
        'JPEG',
        subsampling=0 if image_quality_in_editor > 60 else 2,
        quality=image_quality_in_editor
    )

    byte_io_huge = io.BytesIO()
    hsize = int(height * 600.0 / width)
    im.resize((600, hsize), Image.ANTIALIAS).save(byte_io_huge, 'JPEG')

    byte_io_thumbs = io.BytesIO()
    thumbnail_size = (128, 96)
    background = Image.new('RGB', thumbnail_size, "black")
    im.thumbnail(thumbnail_size)
    (w, h) = im.size
    background.paste(
        im, ((thumbnail_size[0] - w) // 2, (thumbnail_size[1] - h) // 2)
    )
    im = background
    im.save(byte_io_thumbs, 'JPEG')

    byte_io_thumbs.seek(0)
    byte_io_lores.seek(0)
    byte_io_huge.seek(0)
    byte_io_orig.seek(0)

    return byte_io_orig, byte_io_lores, byte_io_huge, byte_io_thumbs


def __upload_images_to_aws_thread(
    res,
    img_paths,
    project,
    annotation_status,
    prefix,
    thread_id,
    chunksize,
    couldnt_upload,
    uploaded,
    image_quality_in_editor,
    from_s3_bucket=None,
):
    project_type = project["type"]
    len_img_paths = len(img_paths)
    start_index = thread_id * chunksize
    end_index = start_index + chunksize
    if from_s3_bucket is not None:
        from_session = boto3.Session()
        from_s3 = from_session.resource('s3')
    if start_index >= len_img_paths:
        return
    s3_session = boto3.Session(
        aws_access_key_id=res['accessKeyId'],
        aws_secret_access_key=res['secretAccessKey'],
        aws_session_token=res['sessionToken']
    )
    s3_resource = s3_session.resource('s3')
    bucket = s3_resource.Bucket(res["bucket"])
    prefix = res['filePath']
    uploaded_imgs = []
    for i in range(start_index, end_index):
        if i >= len_img_paths:
            break
        path = img_paths[i]
        key = prefix + f'{Path(path).name}'
        if from_s3_bucket is not None:
            file = io.BytesIO()
            from_s3_object = from_s3.Object(from_s3_bucket, path)
            from_s3_object.download_fileobj(file)
        else:
            with open(path, "rb") as f:
                file = io.BytesIO(f.read())
        try:
            orig_image, lores_image, huge_image, thumbnail_image = get_image_array_to_upload(
                file, project_type, image_quality_in_editor
            )
            bucket.put_object(Body=orig_image, Key=key)
            bucket.put_object(Body=lores_image, Key=key + '___lores.jpg')
            bucket.put_object(Body=huge_image, Key=key + '___huge.jpg')
            bucket.put_object(Body=thumbnail_image, Key=key + '___thumb.jpg')
        except Exception as e:
            logger.warning("Unable to upload to data server %s.", e)
            couldnt_upload[thread_id].append(path)
        else:
            uploaded[thread_id].append(path)
            uploaded_imgs.append(path)
            if len(uploaded_imgs) >= 100:
                __create_image(
                    uploaded_imgs, project, annotation_status, prefix
                )
                uploaded_imgs = []
    __create_image(uploaded_imgs, project, annotation_status, prefix)


def __create_image(img_paths, project, annotation_status, remote_dir):
    # print("Creating images ", len(img_paths))
    if len(img_paths) == 0:
        return
    team_id, project_id = project["team_id"], project["id"]
    data = {
        "project_id": str(project_id),
        "team_id": str(team_id),
        "images": [],
        "annotation_status": annotation_status
    }
    for img_path in img_paths:
        img_name = Path(img_path).name
        remote_path = remote_dir + f"{img_name}"
        data["images"].append({"name": img_name, "path": remote_path})

    response = _api.send_request(
        req_type='POST', path='/image/ext-create', json_req=data
    )
    if not response.ok:
        raise SABaseException(
            response.status_code, "Couldn't ext-create image " + response.text
        )


def upload_images_to_project(
    project,
    img_paths,
    annotation_status="NotStarted",
    from_s3_bucket=None,
    image_quality_in_editor=None
):
    """Uploads all images given in list of path objects in img_paths to the project.
    Sets status of all the uploaded images to set_status if it is not None.

    :param project: project name or metadata of the project to upload images to
    :type project: str or dict
    :param img_paths: list of Pathlike (str or Path) objects to upload
    :type img_paths: list
    :param annotation_status: value to set the annotation statuses of the uploaded images NotStarted InProgress QualityCheck Returned Completed Skipped
    :type annotation_status: str
    :param from_s3_bucket: AWS S3 bucket to use. If None then folder_path is in local filesystem
    :type from_s3_bucket: str
    :param image_quality_in_editor: image quality (in percents) that will be seen in SuperAnnotate web annotation editor. If None default value will be used.
    :type image_quality_in_editor: int

    :return: uploaded and not-uploaded images' filepaths
    :rtype: tuple of list of strs
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    annotation_status = annotation_status_str_to_int(annotation_status)
    if image_quality_in_editor is None:
        image_quality_in_editor = _get_project_default_image_quality_in_editor(
            project
        )
    team_id, project_id = project["team_id"], project["id"]
    len_img_paths = len(img_paths)
    logger.info(
        "Uploading %s images to project %s.", len_img_paths, project["name"]
    )
    if len_img_paths == 0:
        return
    params = {
        'team_id': team_id,
    }
    uploaded = []
    for _ in range(_NUM_THREADS):
        uploaded.append([])
    couldnt_upload = []
    for _ in range(_NUM_THREADS):
        couldnt_upload.append([])
    finish_event = threading.Event()
    chunksize = int(math.ceil(len(img_paths) / _NUM_THREADS))
    tqdm_thread = threading.Thread(
        target=__tqdm_thread_image_upload,
        args=(len_img_paths, uploaded, couldnt_upload, finish_event)
    )
    tqdm_thread.start()
    response = _api.send_request(
        req_type='GET',
        path=f'/project/{project_id}/sdkImageUploadToken',
        params=params
    )
    if response.ok:
        res = response.json()
        prefix = res['filePath']
    else:
        raise SABaseException(
            response.status_code, "Couldn't get upload token " + response.text
        )

    threads = []
    for thread_id in range(_NUM_THREADS):
        t = threading.Thread(
            target=__upload_images_to_aws_thread,
            args=(
                res, img_paths, project, annotation_status, prefix, thread_id,
                chunksize, couldnt_upload, uploaded, image_quality_in_editor,
                from_s3_bucket
            )
        )
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    finish_event.set()
    tqdm_thread.join()
    list_of_not_uploaded = []
    for couldnt_upload_thread in couldnt_upload:
        for file in couldnt_upload_thread:
            logger.warning("Couldn't upload image %s", file)
            list_of_not_uploaded.append(str(file))
    list_of_uploaded = []
    for upload_thread in uploaded:
        for file in upload_thread:
            list_of_uploaded.append(str(file))

    return (list_of_uploaded, list_of_not_uploaded)


def __upload_annotations_thread(
    team_id, project_id, project_type, anns_filenames, folder_path,
    annotation_classes_dict, thread_id, chunksize, num_uploaded, from_s3_bucket,
    actually_uploaded
):
    NUM_TO_SEND = 500
    len_anns = len(anns_filenames)
    start_index = thread_id * chunksize
    if start_index >= len_anns:
        return
    end_index = min(start_index + chunksize, len_anns)

    postfix_json = '___objects.json' if project_type == 1 else '___pixel.json'
    len_postfix_json = len(postfix_json)
    postfix_mask = '___save.png'
    if from_s3_bucket is not None:
        from_session = boto3.Session()
        from_s3 = from_session.resource('s3')

    for i in range(start_index, end_index, NUM_TO_SEND):
        data = {"project_id": project_id, "team_id": team_id, "names": []}
        for j in range(i, i + NUM_TO_SEND):
            if j >= end_index:
                break
            image_name = anns_filenames[j][:-len_postfix_json]
            data["names"].append(image_name)
        response = _api.send_request(
            req_type='POST',
            path='/images/getAnnotationsPathsAndTokens',
            json_req=data
        )
        res = response.json()
        if len(res["images"]) != len(data["names"]):
            logger.warning("Couldn't find all the images for annotation JSONs.")
        aws_creds = res["creds"]
        s3_session = boto3.Session(
            aws_access_key_id=aws_creds['accessKeyId'],
            aws_secret_access_key=aws_creds['secretAccessKey'],
            aws_session_token=aws_creds['sessionToken']
        )
        s3_resource = s3_session.resource('s3')
        bucket = s3_resource.Bucket(aws_creds["bucket"])

        for image_name, image_path in res['images'].items():
            json_filename = image_name + postfix_json
            if from_s3_bucket is None:
                annotation_json = json.load(
                    open(Path(folder_path) / json_filename)
                )
            else:
                file = io.BytesIO()
                from_s3_object = from_s3.Object(
                    from_s3_bucket, folder_path + json_filename
                )
                from_s3_object.download_fileobj(file)
                file.seek(0)
                annotation_json = json.load(file)

            fill_class_and_attribute_ids(
                annotation_json, annotation_classes_dict
            )
            bucket.put_object(
                Key=image_path + postfix_json, Body=json.dumps(annotation_json)
            )
            if project_type != 1:
                mask_filename = image_name + postfix_mask
                if from_s3_bucket is None:
                    with open(Path(folder_path) / mask_filename, 'rb') as fin:
                        file = io.BytesIO(fin.read())
                else:
                    file = io.BytesIO()
                    from_s3_object = from_s3.Object(
                        from_s3_bucket, folder_path + mask_filename
                    )
                    from_s3_object.download_fileobj(file)
                    file.seek(0)
                bucket.put_object(Key=image_path + postfix_mask, Body=file)
            num_uploaded[thread_id] += 1
            actually_uploaded[thread_id].append(
                Path(folder_path) / json_filename
            )


def upload_annotations_from_folder_to_project(
    project, folder_path, from_s3_bucket=None, recursive_subfolders=False
):
    """Finds and uploads all JSON files in the folder_path as annotations to the project.

    WARNING: The JSON files should follow specific naming convention. For Vector
    projects they should be named "<image_filename>___objects.json" (e.g., if
    image is cats.jpg the annotation filename should be cats.jpg___objects.json), for Pixel projects
    JSON file should be named "<image_filename>___pixel.json" and also second mask
    image file should be present with the name "<image_name>___save.png". In both cases
    image with <image_name> should be already present on the platform.

    WARNING: Existing annotations will be overwritten.

    :param project: project name or metadata of the project to upload annotations to
    :type project: str or dict
    :param folder_path: from which folder to upload the annotations
    :type folder_path: Pathlike (str or Path)
    :param from_s3_bucket: AWS S3 bucket to use. If None then folder_path is in local filesystem
    :type from_s3_bucket: str
    :param recursive_subfolders: enable recursive subfolder parsing
    :type recursive_subfolders: bool

    :return: paths to annotations uploaded
    :rtype: list of strs
    """
    if recursive_subfolders:
        logger.warning(
            "When using recursive subfolder parsing same name annotations in different subfolders will overwrite each other."
        )

    logger.warning(
        "The JSON files should follow specific naming convention. For Vector projects they should be named '<image_name>___objects.json', for Pixel projects JSON file should be names '<image_name>___pixel.json' and also second mask image file should be present with the name '<image_name>___save.png'. In both cases image with <image_name> should be already present on the platform."
    )

    logger.warning("Existing annotations will be overwritten.")
    if not isinstance(project, dict):
        project = get_project_metadata(project)

    return _upload_annotations_from_folder_to_project(
        project, folder_path, from_s3_bucket, recursive_subfolders
    )


def _upload_annotations_from_folder_to_project(
    project, folder_path, from_s3_bucket=None, recursive_subfolders=False
):
    return_result = []
    if from_s3_bucket is not None:
        if not folder_path.endswith('/'):
            folder_path = folder_path + '/'
    if recursive_subfolders:
        if from_s3_bucket is None:
            for path in Path(folder_path).glob('*'):
                if path.is_dir():
                    return_result += _upload_annotations_from_folder_to_project(
                        project, path, from_s3_bucket, recursive_subfolders
                    )
        else:
            s3_client = boto3.client('s3')
            result = s3_client.list_objects(
                Bucket=from_s3_bucket, Prefix=folder_path, Delimiter='/'
            )
            results = result.get('CommonPrefixes')
            if results is not None:
                for o in results:
                    return_result += _upload_annotations_from_folder_to_project(
                        project, o.get('Prefix'), from_s3_bucket,
                        recursive_subfolders
                    )

    team_id, project_id, project_type = project["team_id"], project[
        "id"], project["type"]
    logger.info(
        "Uploading all annotations from %s to project %s.", folder_path,
        project["name"]
    )

    annotations_paths = []
    annotations_filenames = []
    if from_s3_bucket is None:
        for path in Path(folder_path).glob('*.json'):
            if path.name.endswith('___objects.json'
                                 ) or path.name.endswith('___pixel.json'):
                annotations_paths.append(path)
                annotations_filenames.append(path.name)
    else:
        s3_client = boto3.client('s3')
        paginator = s3_client.get_paginator('list_objects_v2')
        response_iterator = paginator.paginate(
            Bucket=from_s3_bucket, Prefix=folder_path
        )

        for response in response_iterator:
            for object_data in response['Contents']:
                key = object_data['Key']
                if '/' in key[len(folder_path) + 1:]:
                    continue
                if key.endswith('___objects.json'
                               ) or key.endswith('___pixel.json'):
                    annotations_paths.append(key)
                    annotations_filenames.append(Path(key).name)

    len_annotations_paths = len(annotations_paths)
    logger.info(
        "Uploading %s annotations to project %s.", len_annotations_paths,
        project["name"]
    )
    if len_annotations_paths == 0:
        return return_result
    num_uploaded = [0] * _NUM_THREADS
    actually_uploaded = []
    for _ in range(_NUM_THREADS):
        actually_uploaded.append([])
    finish_event = threading.Event()
    tqdm_thread = threading.Thread(
        target=__tqdm_thread,
        args=(len_annotations_paths, num_uploaded, finish_event)
    )
    tqdm_thread.start()

    annotation_classes = search_annotation_classes(
        project, return_metadata=True
    )
    annotation_classes_dict = get_annotation_classes_name_to_id(
        annotation_classes
    )
    chunksize = int(math.ceil(len_annotations_paths / _NUM_THREADS))
    threads = []
    for thread_id in range(_NUM_THREADS):
        t = threading.Thread(
            target=__upload_annotations_thread,
            args=(
                team_id, project_id, project_type, annotations_filenames,
                folder_path, annotation_classes_dict, thread_id, chunksize,
                num_uploaded, from_s3_bucket, actually_uploaded
            )
        )
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    finish_event.set()
    tqdm_thread.join()
    logger.info("Number of annotations uploaded %s.", sum(num_uploaded))

    for ac_upl in actually_uploaded:
        return_result += [str(p) for p in ac_upl]
    return return_result


def __upload_preannotations_thread(
    aws_creds, project_type, preannotations_filenames, folder_path,
    annotation_classes_dict, thread_id, chunksize, num_uploaded,
    already_uploaded, from_s3_bucket
):
    len_preanns = len(preannotations_filenames)
    start_index = thread_id * chunksize
    if start_index >= len_preanns:
        return
    end_index = min(start_index + chunksize, len_preanns)
    s3_session = boto3.Session(
        aws_access_key_id=aws_creds['accessKeyId'],
        aws_secret_access_key=aws_creds['secretAccessKey'],
        aws_session_token=aws_creds['sessionToken']
    )
    s3_resource = s3_session.resource('s3')
    bucket = s3_resource.Bucket(aws_creds["bucket"])

    postfix_json = '___objects.json' if project_type == 1 else '___pixel.json'
    len_postfix_json = len(postfix_json)
    postfix_mask = '___save.png'
    if from_s3_bucket is not None:
        from_session = boto3.Session()
        from_s3 = from_session.resource('s3')

    for i in range(start_index, end_index):
        if already_uploaded[i]:
            continue
        json_filename = preannotations_filenames[i]
        if from_s3_bucket is None:
            annotation_json = json.load(open(Path(folder_path) / json_filename))
        else:
            file = io.BytesIO()
            from_s3_object = from_s3.Object(
                from_s3_bucket, folder_path + json_filename
            )
            from_s3_object.download_fileobj(file)
            file.seek(0)
            annotation_json = json.load(file)

        fill_class_and_attribute_ids(annotation_json, annotation_classes_dict)
        bucket.put_object(
            Key=aws_creds["filePath"] + f"/{json_filename}",
            Body=json.dumps(annotation_json)
        )
        if project_type != 1:
            mask_filename = json_filename[:-len_postfix_json] + postfix_mask
            if from_s3_bucket is None:
                with open(Path(folder_path) / mask_filename, 'rb') as fin:
                    file = io.BytesIO(fin.read())
            else:
                file = io.BytesIO()
                from_s3_object = from_s3.Object(
                    from_s3_bucket, folder_path + mask_filename
                )
                from_s3_object.download_fileobj(file)
                file.seek(0)
            bucket.put_object(
                Key=aws_creds['filePath'] + f'/{mask_filename}', Body=file
            )
        num_uploaded[thread_id] += 1
        already_uploaded[i] = True


def __tqdm_thread(total_num, current_nums, finish_event):
    with tqdm(total=total_num) as pbar:
        while True:
            finished = finish_event.wait(5)
            if not finished:
                pbar.update(sum(current_nums) - pbar.n)
            else:
                pbar.update(total_num - pbar.n)
                break


def __tqdm_thread_image_upload(
    total_num, uploaded, couldnt_upload, finish_event
):
    with tqdm(total=total_num) as pbar:
        while True:
            finished = finish_event.wait(5)
            if not finished:
                sum_all = 0
                for i in couldnt_upload:
                    sum_all += len(i)
                for i in uploaded:
                    sum_all += len(i)
                pbar.update(sum_all - pbar.n)
            else:
                pbar.update(total_num - pbar.n)
                break


def upload_preannotations_from_folder_to_project(
    project, folder_path, from_s3_bucket=None, recursive_subfolders=False
):
    """Finds and uploads all JSON files in the folder_path as pre-annotations to the project.

    WARNING: The JSON files should follow specific naming convention. For Vector
    projects they should be named "<image_filename>___objects.json" (e.g., if
    image is cats.jpg the annotation filename should be cats.jpg___objects.json), for Pixel projects
    JSON file should be named "<image_filename>___pixel.json" and also second mask
    image file should be present with the name "<image_name>___save.png". In both cases
    image with <image_name> should be already present on the platform.

    WARNING: Existing pre-annotations will be overwritten.

    :param project: project name or metadata of the project to upload pre-annotations to
    :type project: str or dict
    :param folder_path: from which folder to upload the pre-annotations
    :type folder_path: Pathlike (str or Path)
    :param from_s3_bucket: AWS S3 bucket to use. If None then folder_path is in local filesystem
    :type from_s3_bucket: str
    :param recursive_subfolders: enable recursive subfolder parsing
    :type recursive_subfolders: bool

    :return: paths to pre-annotations uploaded
    :rtype: list of strs
    """
    if recursive_subfolders:
        logger.warning(
            "When using recursive subfolder parsing same name pre-annotations in different subfolders will overwrite each other."
        )
    logger.warning(
        "The JSON files should follow specific naming convention. For Vector projects they should be named '<image_name>___objects.json', for Pixel projects JSON file should be names '<image_name>___pixel.json' and also second mask image file should be present with the name '<image_name>___save.png'. In both cases image with <image_name> should be already present on the platform."
    )

    logger.warning(
        "Identically named existing pre-annotations will be overwritten."
    )
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    return _upload_preannotations_from_folder_to_project(
        project, folder_path, from_s3_bucket, recursive_subfolders
    )


def _upload_preannotations_from_folder_to_project(
    project, folder_path, from_s3_bucket=None, recursive_subfolders=False
):
    return_result = []
    if from_s3_bucket is not None:
        if not folder_path.endswith('/'):
            folder_path = folder_path + '/'
    if recursive_subfolders:
        if from_s3_bucket is None:
            for path in Path(folder_path).glob('*'):
                if path.is_dir():
                    return_result += _upload_preannotations_from_folder_to_project(
                        project, path, from_s3_bucket, recursive_subfolders
                    )
        else:
            s3_client = boto3.client('s3')
            result = s3_client.list_objects(
                Bucket=from_s3_bucket, Prefix=folder_path, Delimiter='/'
            )
            results = result.get('CommonPrefixes')
            if results is not None:
                for o in results:
                    return_result += _upload_preannotations_from_folder_to_project(
                        project, o.get('Prefix'), from_s3_bucket,
                        recursive_subfolders
                    )

    team_id, project_id, project_type = project["team_id"], project[
        "id"], project["type"]
    logger.info(
        "Uploading all preannotations from %s to project %s.", folder_path,
        project["name"]
    )

    preannotations_paths = []
    preannotations_filenames = []
    if from_s3_bucket is None:
        for path in Path(folder_path).glob('*.json'):
            if path.name.endswith('___objects.json'
                                 ) or path.name.endswith('___pixel.json'):
                preannotations_paths.append(path)
                preannotations_filenames.append(path.name)
    else:
        s3_client = boto3.client('s3')
        paginator = s3_client.get_paginator('list_objects_v2')
        response_iterator = paginator.paginate(
            Bucket=from_s3_bucket, Prefix=folder_path
        )

        for response in response_iterator:
            for object_data in response['Contents']:
                key = object_data['Key']
                if '/' in key[len(folder_path) + 1:]:
                    continue
                if key.endswith('___objects.json'
                               ) or key.endswith('___pixel.json'):
                    preannotations_paths.append(key)
                    preannotations_filenames.append(Path(key).name)

    len_preannotations_paths = len(preannotations_paths)
    logger.info(
        "Uploading %s preannotations to project %s.", len_preannotations_paths,
        project["name"]
    )
    if len_preannotations_paths == 0:
        return return_result
    params = {'team_id': team_id, 'creds_only': True, 'type': project_type}
    num_uploaded = [0] * _NUM_THREADS
    already_uploaded = [False] * len_preannotations_paths
    chunksize = int(math.ceil(len_preannotations_paths / _NUM_THREADS))
    finish_event = threading.Event()
    tqdm_thread = threading.Thread(
        target=__tqdm_thread,
        args=(len_preannotations_paths, num_uploaded, finish_event)
    )
    tqdm_thread.start()
    annotation_classes = search_annotation_classes(
        project, return_metadata=True
    )
    annotation_classes_dict = get_annotation_classes_name_to_id(
        annotation_classes
    )
    while True:
        if sum(num_uploaded) == len_preannotations_paths:
            break
        response = _api.send_request(
            req_type='GET',
            path=f'/project/{project_id}/preannotation',
            params=params
        )
        if not response.ok:
            raise SABaseException(response.status_code, response.text)
        aws_creds = response.json()

        threads = []
        for thread_id in range(_NUM_THREADS):
            t = threading.Thread(
                target=__upload_preannotations_thread,
                args=(
                    aws_creds, project_type, preannotations_filenames,
                    folder_path, annotation_classes_dict, thread_id, chunksize,
                    num_uploaded, already_uploaded, from_s3_bucket
                )
            )
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    finish_event.set()
    tqdm_thread.join()
    logger.info("Number of preannotations uploaded %s.", sum(num_uploaded))
    return return_result + [str(p) for p in preannotations_paths]


def share_project(project, user, user_role):
    """Share project with user.

    :param project: project name or metadata of the project
    :type project: str or dict
    :param user: user email or metadata of the user to share project with
    :type user: str or dict
    :param user_role: user role to apply, one of Admin , Annotator , QA , Customer , Viewer
    :type user_role: str
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    if not isinstance(user, dict):
        user = get_team_contributor_metadata(user)
    user_role = user_role_str_to_int(user_role)
    team_id, project_id = project["team_id"], project["id"]
    user_id = user["id"]
    json_req = {"user_id": user_id, "user_role": user_role}
    params = {'team_id': team_id}
    response = _api.send_request(
        req_type='POST',
        path=f'/project/{project_id}/share',
        params=params,
        json_req=json_req
    )
    if not response.ok:
        raise SABaseException(response.status_code, response.text)
    logger.info(
        "Shared project %s with user %s and role %s", project["name"],
        user["email"], user_role_int_to_str(user_role)
    )


def unshare_project(project, user):
    """Unshare (remove) user from project.

    :param project: project name or metadata of the project
    :type project: str or dict
    :param user: user email or metadata of the user to unshare project
    :type user: str or dict
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    if not isinstance(user, dict):
        user = get_team_contributor_metadata(user)
    team_id, project_id = project["team_id"], project["id"]
    user_id = user["id"]
    json_req = {"user_id": user_id}
    params = {'team_id': team_id}
    response = _api.send_request(
        req_type='DELETE',
        path=f'/project/{project_id}/share',
        params=params,
        json_req=json_req
    )
    if not response.ok:
        raise SABaseException(response.status_code, response.text)
    logger.info("Unshared project %s from user ID %s", project["name"], user_id)


def upload_images_from_s3_bucket_to_project(
    project,
    accessKeyId,
    secretAccessKey,
    bucket_name,
    folder_path,
    image_quality_in_editor=None
):
    """Uploads all images from AWS S3 bucket to the project.

    :param project: project name or metadata of the project to upload images to
    :type project: str or dict
    :param accessKeyId: AWS S3 access key ID
    :type accessKeyId: str
    :param secretAccessKey: AWS S3 secret access key
    :type secretAccessKey: str
    :param bucket_name: AWS S3 bucket
    :type bucket_name: str
    :param folder_path: from which folder to upload the images
    :type folder_path: str
    :param image_quality_in_editor: image quality (in percents) that will be seen in SuperAnnotate web annotation editor, if None default value will be used
    :type image_quality_in_editor: int
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    if image_quality_in_editor is not None:
        old_quality = _get_project_default_image_quality_in_editor(project)
        _set_project_default_image_quality_in_editor(
            project, image_quality_in_editor
        )
    team_id, project_id = project["team_id"], project["id"]
    params = {
        "team_id": team_id,
    }
    data = {
        "accessKeyID": accessKeyId,
        "secretAccessKey": secretAccessKey,
        "bucketName": bucket_name,
        "folderName": folder_path
    }
    response = _api.send_request(
        req_type='POST',
        path=f'/project/{project_id}/get-image-s3-access-point',
        params=params,
        json_req=data
    )
    if not response.ok:
        raise SABaseException(
            response.status_code,
            "Couldn't upload to project from S3 " + response.text
        )
    logger.info("Waiting for S3 upload to finish.")
    while True:
        time.sleep(5)
        res = _get_upload_from_s3_bucket_to_project_status(project)
        if res["progress"] == '2':
            break
        if res["progress"] != "1":
            raise SABaseException(
                response.status_code,
                "Couldn't upload to project from S3 " + response.text
            )
    if image_quality_in_editor is not None:
        _set_project_default_image_quality_in_editor(project, old_quality)


def _get_upload_from_s3_bucket_to_project_status(project):
    team_id, project_id = project["team_id"], project["id"]
    params = {
        "team_id": team_id,
    }
    response = _api.send_request(
        req_type='GET',
        path=f'/project/{project_id}/getS3UploadStatus',
        params=params
    )
    if not response.ok:
        raise SABaseException(
            response.status_code,
            "Couldn't get upload to project from S3 status " + response.text
        )
    return response.json()


def get_project_workflow(project):
    """Gets project's workflow.

    Return value example: [{ "step" : <step_num>, "className" : <annotation_class>, "tool" : <tool_num>, ...},...]

    :param project: project name or metadata
    :type project: str or dict

    :return: project workflow
    :rtype: list of dicts
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    team_id, project_id = project["team_id"], project["id"]
    params = {
        "team_id": team_id,
    }
    response = _api.send_request(
        req_type='GET', path=f'/project/{project_id}/workflow', params=params
    )
    if not response.ok:
        raise SABaseException(
            response.status_code,
            "Couldn't get project workflow " + response.text
        )
    res = response.json()
    annotation_classes = search_annotation_classes(
        project, return_metadata=True
    )
    for r in res:
        if "class_id" not in r:
            continue
        found_classid = False
        for a_class in annotation_classes:
            if a_class["id"] == r["class_id"]:
                found_classid = True
                r["className"] = a_class["name"]
                del r["class_id"]
                break
        if not found_classid:
            raise SABaseException(0, "Couldn't find class_id in workflow")
    return res


def set_project_workflow(project, new_workflow):
    """Sets project's workflow.

    new_workflow example: [{ "step" : <step_num>, "className" : <annotation_class>, "tool" : <tool_num>, ...},...]

    :param project: project name or metadata
    :type project: str or dict
    :param project: new workflow list of dicts
    :type project: list of dicts

    :return: updated part of project's workflow
    :rtype: list of dicts
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    if not isinstance(new_workflow, list):
        raise SABaseException(
            0, "Set project setting new_workflow should be a list"
        )
    team_id, project_id = project["team_id"], project["id"]

    params = {
        "team_id": team_id,
    }
    annotation_classes = search_annotation_classes(
        project, return_metadata=True
    )

    new_list = copy.deepcopy(new_workflow)
    for step in new_list:
        if "id" in step:
            del step["id"]
        if "className" in step:
            found = False
            for an_class in annotation_classes:
                if an_class["name"] == step["className"]:
                    step["class_id"] = an_class["id"]
                    del step["className"]
                    found = True
                    break
            if not found:
                raise SABaseException(
                    0, "Annotation class not found in set_project_workflow."
                )

    json_req = {"steps": new_list}
    response = _api.send_request(
        req_type='POST',
        path=f'/project/{project_id}/workflow',
        params=params,
        json_req=json_req
    )
    if not response.ok:
        raise SABaseException(
            response.status_code,
            "Couldn't set project workflow " + response.text
        )
    res = response.json()
    return res


def get_project_settings(project):
    """Gets project's settings.

    Return value example: [{ "attribute" : "Brightness", "value" : 10, ...},...]

    :param project: project name or metadata
    :type project: str or dict

    :return: project settings
    :rtype: list of dicts
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    team_id, project_id = project["team_id"], project["id"]
    params = {
        "team_id": team_id,
    }
    response = _api.send_request(
        req_type='GET', path=f'/project/{project_id}/settings', params=params
    )
    if not response.ok:
        raise SABaseException(
            response.status_code,
            "Couldn't get project settings " + response.text
        )
    return response.json()


def set_project_settings(project, new_settings):
    """Sets project's settings.

    New settings format example: [{ "attribute" : "Brightness", "value" : 10, ...},...]

    :param project: project name or metadata
    :type project: str or dict
    :param project: new settings list of dicts
    :type project: list of dicts

    :return: updated part of project's settings
    :rtype: list of dicts
    """
    if not isinstance(project, dict):
        project = get_project_metadata(project)
    if not isinstance(new_settings, list):
        raise SABaseException(
            0, "Set project setting new_settings should be a list"
        )
    team_id, project_id = project["team_id"], project["id"]

    params = {
        "team_id": team_id,
    }
    current_settings = get_project_settings(project)

    id_conv = {}
    for setting in current_settings:
        if "attribute" in setting:
            id_conv[setting["attribute"]] = setting["id"]

    new_list = []
    for new_setting in new_settings:
        if "attribute" in new_setting and new_setting["attribute"] in id_conv:
            new_list.append(
                {
                    "attribute": new_setting["attribute"],
                    "id": id_conv[new_setting["attribute"]],
                    "value": new_setting["value"]
                }
            )
    json_req = {"settings": new_list}
    response = _api.send_request(
        req_type='PUT',
        path=f'/project/{project_id}/settings',
        params=params,
        json_req=json_req
    )
    if not response.ok:
        raise SABaseException(
            response.status_code,
            "Couldn't set project settings " + response.text
        )
    return response.json()


def _get_project_default_image_quality_in_editor(project):
    for setting in get_project_settings(project):
        if "attribute" in setting and setting["attribute"] == "ImageQuality":
            return setting["value"]
    return 60
    # raise SABaseException(
    #     response.status_code,
    #     "Couldn't get project default image quality " + response.text
    # )


def _set_project_default_image_quality_in_editor(project, quality):
    set_project_settings(
        project, {
            "attribute": "ImageQuality",
            "value": quality
        }
    )
