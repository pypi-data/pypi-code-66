import io
import json
import mimetypes
import os
from base64 import decodebytes

from minio import Minio
from nbformat import from_dict
from notebook.services.contents.manager import ContentsManager
from notebook.services.contents.filemanager import FileContentsManager
from traitlets import HasTraits

from NoteBookForMinio.models import base_model, base_directory_model


class MinioManagerMixin(HasTraits):
    def __init__(self, *args, **kwargs):
        super(MinioManagerMixin, self).__init__(*args, **kwargs)


class mFile():
    BUFFERSIZE = 1024

    def __init__(self, path, MManager):
        '''
        :param path: absolutePath
        '''
        self.path = path
        self.client = MManager
        self.buffer = ""
        self.pre = b""
        self.bufferstream = io.BytesIO(b'')
        self.offset = 0
        self.size = self.client.get_file_stat(path).size
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            del self
        else:
            print("[Exit %s]: Exited with exception raised." % self.handle)
        return False
    def read(self, bufferSize=None):
        if self.offset == self.size:
            return b''
        if not bufferSize:
            try:
                data = self.client.get_content_v2(self.path, self.offset)
            except Exception as e:
                print(e)
        else:
            try:
                data = self.client.get_content_v2(self.path, self.offset, bufferSize)
            except Exception as e:
                print(e)
        self.offset += len(data)
        return data

    def readline(self):
        while True:
            data = self.bufferstream.readline()
            if len(data) == 0:
                if self.offset == self.size:
                    temp = self.pre
                    self.pre = b''
                    return temp
                self.reload()
                continue
            if data.endswith(b'\n'):
                temp = self.pre
                self.pre = b''
                return temp + data
            else:
                self.pre += data

    def reload(self):
        self.buffer = self.client.get_content_v2(self.path, self.offset, self.BUFFERSIZE)
        self.offset += len(self.buffer)
        self.bufferstream = io.BytesIO(self.buffer)


def mopen(path):
    '''
    :param path: absolutePath
    '''
    return mFile(path, MinioContentsManager())


class MinioContentsManager(MinioManagerMixin, ContentsManager):
    bucket = "user"

    def __init__(self, *args, **kwargs):
        super(MinioContentsManager, self).__init__(*args, **kwargs)
        envs = os.environ
        self.user_id = envs.get("user_id")
        self.hostport = envs.get("hostport")
        access_key = envs.get("access_key")
        secret_key = envs.get("secret_key")
        self.minioClinet = Minio(self.hostport, access_key=access_key, secret_key=secret_key, secure=False)

    # Basic ContentsManager API.
    def get_path(self, path):
        path = path.strip('/')
        if path == '':
            file_path = "volume-{}".format(self.user_id)
        else:
            file_path = "volume-{}/{}".format(self.user_id, path)
        return file_path

    def dir_exists(self, path=''):
        path = self.get_path(path)
        stat = self.minioClinet.list_objects(self.bucket, path)
        lists = [x for x in stat]
        if lists and lists[0].is_dir:
            return True
        else:
            return False

    def file_exists(self, path):
        path = self.get_path(path)
        stat = self.minioClinet.list_objects(self.bucket, path)
        lists = [x for x in stat]
        if lists and not lists[0].is_dir:
            return True
        else:
            return False

    def guess_type(self, path, allow_directory=True):
        """
        Guess the type of a file.

        If allow_directory is False, don't consider the possibility that the
        file is a directory.
        """
        self.log.info('path:%s'.format(path))
        if path.endswith('.ipynb'):
            return 'notebook'
        elif allow_directory and self.dir_exists(path):
            return 'directory'
        else:
            return 'file'

    def get(self, path, content=True, type=None, format=None):
        print(path)
        self.log.error(
            u'path&content&type:%r. %s  %s',
            path, content, type
        )
        path = path.strip('/')
        if type is None:
            type = self.guess_type(path)
        self.log.error(
            u'type:%s',
            type
        )
        try:
            fn = {
                'notebook': self._get_notebook,
                'directory': self._get_directory,
                'file': self._get_file,
            }[type]
        except KeyError:
            raise ValueError("Unknown type passed: '{}'".format(type))

        try:
            return fn(path=path, content=content, format=format)
        except Exception as e:
            self.log.error(
                u'Corrupted file encountered at path %r. %s',
                path, e, exc_info=True,
            )
            self.do_500("Unable to read stored content at path %r." % path)

    def save(self, model, path):
        self.log.error(
            u'path and model %r. %s',
            path, model, exc_info=True,
        )
        if 'type' not in model:
            raise AssertionError(400, u'No model type provided')
        if 'content' not in model and model['type'] != 'directory':
            raise AssertionError(400, u'No file content provided')

        path = path.strip('/')

        if model['type'] not in ('file', 'directory', 'notebook'):
            raise AssertionError("Unhandled contents type: %s" % model['type'])
        try:
            if model['type'] == 'notebook':
                validation_message = self._save_notebook(model, path)
            elif model['type'] == 'file':
                validation_message = self._save_file(model, path)
            else:
                validation_message = self._save_directory(path)
        except Exception as e:
            raise e
        # TODO: Consider not round-tripping to the database again here.
        model = self.get(path, type=model['type'], content=False)
        if validation_message is not None:
            model['message'] = validation_message
        return model

    def rename_file(self, old_path, path):
        """
        Rename object from old_path to path.

        NOTE: This method is unfortunately named on the base class. It actually
              moves files and directories as well.
        """

        try:
            if self.file_exists(old_path):
                self._rename_file(old_path, path)
            elif self.dir_exists(old_path):
                self._rename_directory(old_path, path)
            else:
                raise AssertionError("")
        except Exception as e:
            raise e

    def delete_file(self, path):
        """
        Delete object corresponding to path.
        """
        if self.file_exists(path):
            self._delete_non_directory(path)
        elif self.dir_exists(path):
            self._delete_directory(path)
        else:
            raise AssertionError("Error!")

    def is_hidden(self, path):
        return False

    def get_content(self, path):
        path = self.get_path(path)
        content = self.minioClinet.get_object(self.bucket, path)
        return content.data.decode()

    def get_content_v2(self, path, offset, length=None):
        path = self.get_path(path)
        content = self.minioClinet.get_partial_object(self.bucket, path, offset=offset, length=length)
        return content.data

    def get_file_stat(self, path):
        path = self.get_path(path)
        stat = self.minioClinet.stat_object(self.bucket, path)
        return stat

    def _get_notebook(self, path, content, format=True):
        model = base_model(path)
        Vol_path = self.get_path(path)
        stat = self.minioClinet.list_objects(self.bucket, Vol_path)
        lists = [x for x in stat]
        model['type'] = 'notebook'
        model['last_modified'] = model['created'] = lists[0].last_modified
        if content:
            content = self.get_content(path)
            # self.mark_trusted_cells(json.loads(content), path)
            model['content'] = json.loads(content)
            model['format'] = 'json'
            # self.validate_notebook_model(model)
        return model

    def _get_directory(self, path, content, format=True):
        model = base_directory_model(path)
        if content:
            model['format'] = 'json'
            Vol_path = self.get_path(path)
            stat = self.minioClinet.list_objects(self.bucket, Vol_path + '/')
            list_dir = [x for x in stat]
            content_list = []
            for item in list_dir:
                if item.is_dir:
                    type = "directory"
                    item.object_name = item.object_name[:-1]
                else:
                    type = self.guess_type(item.object_name)
                fn = {
                    'notebook': self._get_notebook,
                    'directory': self._get_directory,
                    'file': self._get_file,
                }[type]
                item_model = fn(item.object_name.split('/', 1)[1], False)
                content_list.append(item_model)
            model['content'] = content_list
        return model

    def _get_file(self, path, content, format=True):
        self.log.error(
            u'path&content:%r. %s',
            path, content
        )
        model = base_model(path)
        model['type'] = 'file'
        Vol_path = self.get_path(path)
        stat = self.minioClinet.list_objects(self.bucket, Vol_path)
        lists = [x for x in stat]
        model['last_modified'] = model['created'] = lists[0].last_modified
        if content:
            mimetype = mimetypes.guess_type(path)[0]
            model['mimetype'], model['format'] = (mimetype, 'text') if mimetype else ("base64", "base64")
            model['content'] = self.get_content(path)
        return model

    def _save_notebook(self, model, path):
        """
        Save a notebook.

        Returns a validation message.
        """

        nb_contents = from_dict(model['content'])
        self.check_and_sign(nb_contents, path)
        vol_path = self.get_path(path)
        nb = json.dumps(nb_contents).encode()
        self.minioClinet.put_object(bucket_name=self.bucket, object_name=vol_path,
                                    data=io.BytesIO(nb), length=len(nb))
        self.validate_notebook_model(model)
        return model.get('message')

    def _save_file(self, model, path):
        """
        Save a non-notebook file.
        """
        if model.get('format') == 'text':
            bcontent = model['content'].encode('utf8')
        else:
            b64_bytes = model['content'].encode('ascii')
            bcontent = decodebytes(b64_bytes)
        vol_path = self.get_path(path)
        self.minioClinet.put_object(bucket_name=self.bucket, object_name=vol_path,
                                    data=io.BytesIO(bcontent), length=len(bcontent))
        return None

    def _save_directory(self, path):
        """
        'Save' a directory.
        """
        vol_path = self.get_path(path)
        stat = self.minioClinet.list_objects(self.bucket, vol_path)
        lists = [x for x in stat]
        if not lists:
            self.minioClinet.put_object(bucket_name=self.bucket, object_name=vol_path + '/.ignore',
                                        data=io.BytesIO(b''), length=len(b''))
            return None
        else:
            raise AssertionError("Directory %r already exists", path)

    def _delete_non_directory(self, path):
        vol_path = self.get_path(path)
        self.minioClinet.remove_object(self.bucket, vol_path)

    def _delete_directory(self, path):
        vol_path = self.get_path(path)
        lists = [x.object_name for x in self.minioClinet.list_objects_v2(self.bucket, vol_path, recursive=True)]
        for error in self.minioClinet.remove_objects(self.bucket, lists):
            print(error)

    def _rename_file(self, old, new):
        val_old = self.get_path(old)
        val_new = self.get_path(new)
        self.minioClinet.copy_object(self.bucket, val_new, f"/{self.bucket}/{val_old}")
        self.minioClinet.remove_object(self.bucket, val_old)

    def _rename_directory(self, old, new):
        vol_path = self.get_path(old)
        old = old.strip('/')
        new = new.strip('/')

        def replacepath(path, old, new):
            a, b = path.split('/', 1)
            b = b.replace(old, new, 1)
            return a + '/' + b

        lists = [x.object_name for x in self.minioClinet.list_objects_v2(self.bucket, vol_path, recursive=True)]
        for x in lists:
            self.minioClinet.copy_object(self.bucket, replacepath(x, old, new), f"/{self.bucket}/{x}")
            self.minioClinet.remove_object(self.bucket, x)
