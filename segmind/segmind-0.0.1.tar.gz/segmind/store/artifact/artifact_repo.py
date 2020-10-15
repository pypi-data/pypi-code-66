import os
import posixpath
import tempfile
from abc import ABCMeta, abstractmethod

from segmind.exceptions import MlflowException
from segmind.protos.errorcodes_pb2 import (INVALID_PARAMETER_VALUE,
                                           RESOURCE_DOES_NOT_EXIST)
from segmind.utils.validation import bad_path_message, path_not_unique


class ArtifactRepository:
    """Abstract artifact repo that defines how to upload (log) and download
    potentially large artifacts from different storage backends."""

    __metaclass__ = ABCMeta

    def __init__(self, artifact_uri):
        self.artifact_uri = artifact_uri

    @abstractmethod
    def log_artifact(self, local_file, artifact_path=None):
        """Log a local file as an artifact, optionally taking an
        ``artifact_path`` to place it in within the run's artifacts. Run
        artifacts can be organized into directories, so you can place the
        artifact in a directory this way.

        Args:
            local_file: Path to artifact to log
            artifact_path: Directory within the run's artifact directory in
                        which to log the artifact.
        """

    @abstractmethod
    def log_artifacts(self, local_dir, artifact_path=None):
        """Log the files in the specified local directory as artifacts,
        optionally taking an ``artifact_path`` to place them in within the
        run's artifacts.

        Args:
        local_dir: Directory of local artifacts to log
        artifact_path: Directory within the run's artifact directory in which
                    to log the artifacts
        """

    @abstractmethod
    def list_artifacts(self, path):
        """Return all the artifacts for this run_id directly under path. If
        path is a file, returns an empty list. Will error if path is neither a
        file nor directory.

        :param path: Relative source path that contains desired artifacts

        :return: List of artifacts as FileInfo listed directly under path.
        """

    def _is_directory(self, artifact_path):
        listing = self.list_artifacts(artifact_path)
        return len(listing) > 0

    def download_artifacts(self, artifact_path, dst_path=None):
        """Download an artifact file or directory to a local directory if
        applicable, and return a local path for it. The caller is responsible
        for managing the lifecycle of the downloaded artifacts.

        Args:
        artifact_path: Relative source path to the desired artifacts.
        dst_path: Absolute path of the local filesystem destination directory
                to which to download the specified artifacts. This directory
                must already exist. If unspecified, the artifacts will either
                be downloaded to a new uniquely-named directory on the local
                filesystem or will be returned directly in the case of the
                LocalArtifactRepository.

        :return: Absolute path of the local filesystem location containing the
                desired artifacts.
        """

        if dst_path is None:
            dst_path = tempfile.mkdtemp()
        dst_path = os.path.abspath(dst_path)
        if not os.path.exists(dst_path):
            raise MlflowException(
                message=(
                    'The destination path for downloaded artifacts does not' +
                    f' exist! Destination path: {dst_path}'),
                error_code=RESOURCE_DOES_NOT_EXIST)
        elif not os.path.isdir(dst_path):
            raise MlflowException(
                message=(f'The destination path for downloaded artifacts must\
                be a directory! Destination path: {dst_path}'),
                error_code=INVALID_PARAMETER_VALUE)

        def download_file(fullpath):
            dirpath, _ = posixpath.split(fullpath)
            local_dir_path = os.path.join(dst_path, dirpath)
            local_file_path = os.path.join(dst_path, fullpath)
            if not os.path.exists(local_dir_path):
                os.makedirs(local_dir_path)
            self._download_file(
                remote_file_path=fullpath, local_path=local_file_path)
            return local_file_path

        def download_artifact_dir(dir_path):
            local_dir = os.path.join(dst_path, dir_path)
            dir_content = [
                file_info for file_info in self.list_artifacts(dir_path)
                if file_info.path != '.' and file_info.path != dir_path
            ]
            if not dir_content:  # empty dir
                if not os.path.exists(local_dir):
                    os.makedirs(local_dir)
            else:
                for file_info in dir_content:
                    if file_info.is_dir:
                        download_artifact_dir(dir_path=file_info.path)
                    else:
                        download_file(file_info.path)
            return local_dir

        if not os.path.exists(dst_path):
            raise MlflowException(
                message=(
                    'The destination path for downloaded artifacts does not' +
                    f' exist! Destination path: {dst_path}'),
                error_code=RESOURCE_DOES_NOT_EXIST)
        elif not os.path.isdir(dst_path):
            raise MlflowException(
                message=(f'The destination path for downloaded artifacts must\
                must be a directory! Destination path: {dst_path}'),
                error_code=INVALID_PARAMETER_VALUE)

        # Check if the artifacts points to a directory
        if self._is_directory(artifact_path):
            return download_artifact_dir(artifact_path)
        else:
            return download_file(artifact_path)

    @abstractmethod
    def _download_file(self, remote_file_path, local_path):
        """Download the file at the specified relative remote path and saves it
        at the specified local path.

        Args:
        remote_file_path: Source path to the remote file, relative to the root
                        directory of the artifact repository.
        local_path: The path to which to save the downloaded file.
        """


def verify_artifact_path(artifact_path):
    if artifact_path and path_not_unique(artifact_path):
        raise MlflowException(f"Invalid artifact path: '{artifact_path}'.\
         {bad_path_message(artifact_path)}")
