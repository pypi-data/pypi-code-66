#!/usr/bin/env python
"""
Unpack a tar or tar.gz archive into a directory.

usage: %prog archive_source dest_dir
    --[url|file] source type, either a URL or a file.
"""

import math
import optparse
import os
import tarfile
import tempfile
from base64 import b64decode

import requests

# Set max size of archive/file that will be handled to be 100 GB. This is
# arbitrary and should be adjusted as needed.
MAX_SIZE = 100 * math.pow(2, 30)


def url_to_file(url, dest_file):
    """
    Transfer a file from a remote URL to a temporary file.
    """
    url_reader = requests.get(url, stream=True)
    assert url_reader.ok, "History import failed, server returned '%s'" % url_reader.reason
    CHUNK = 10 * 1024  # 10k
    total = 0
    with open(dest_file, 'wb') as fp:
        for chunk in url_reader.iter_content(chunk_size=CHUNK):
            if chunk:
                fp.write(chunk)
                total += CHUNK
                if total > MAX_SIZE:
                    break
    return dest_file


def check_archive(archive_file, dest_dir):
    """
    Ensure that a tar archive has no absolute paths or relative paths outside
    the archive.
    """
    with tarfile.open(archive_file, mode='r') as archive_fp:
        for arc_path in archive_fp.getnames():
            assert os.path.normpath(
                os.path.join(
                    dest_dir,
                    arc_path
                )).startswith(dest_dir.rstrip(os.sep) + os.sep), \
                "Archive member would extract outside target directory: %s" % arc_path
    return True


def unpack_archive(archive_file, dest_dir):
    """
    Unpack a tar and/or gzipped archive into a destination directory.
    """
    archive_fp = tarfile.open(archive_file, mode='r')
    archive_fp.extractall(path=dest_dir)
    archive_fp.close()


def main(options, args):
    is_url = bool(options.is_url)
    is_file = bool(options.is_file)
    archive_source, dest_dir = args

    if options.is_b64encoded:
        archive_source = b64decode(archive_source).decode('utf-8')
        dest_dir = b64decode(dest_dir).decode('utf-8')

    # Get archive from URL.
    if is_url:
        archive_file = url_to_file(archive_source, tempfile.NamedTemporaryFile(dir=dest_dir).name)
    elif is_file:
        archive_file = archive_source

    # Unpack archive.
    check_archive(archive_file, dest_dir)
    unpack_archive(archive_file, dest_dir)


if __name__ == "__main__":
    # Parse command line.
    parser = optparse.OptionParser()
    parser.add_option('-U', '--url', dest='is_url', action="store_true", help='Source is a URL.')
    parser.add_option('-F', '--file', dest='is_file', action="store_true", help='Source is a file.')
    parser.add_option('-e', '--encoded', dest='is_b64encoded', action="store_true", default=False, help='Source and destination dir values are base64 encoded.')
    (options, args) = parser.parse_args()
    main(options, args)
