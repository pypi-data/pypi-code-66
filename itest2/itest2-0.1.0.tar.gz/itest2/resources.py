# -*- coding: utf-8 -*-

import json
import os


class Resources(object):
    """
    Resource management methods.
    Get a resource file path from a given resources directory by filename.
    example:
        schema_files = Resources("../resources/schema",".json")
    """

    def __init__(self, base_path=".", ext=""):
        """Initialize resources with base path and extension
        example:
             schema_files = Resources("../resources/schema",".json")
        :param base_path: the resources base path, defaults to "."
        :type base_path: str, optional
        :param ext: the resources file extension, defaults to ""
        :type ext: str, optional
        :raises ValueError: the base path is not existed.
        """
        base_path = os.path.abspath(base_path)
        if not os.path.isdir(base_path):
            raise ValueError(f"Invalid path : {base_path}")
        self.base_path = base_path
        if ext.startswith("."):
            self.ext = ext
        else:
            self.ext = "." + ext

    def get_path(self, filename: str,
                 ext: str = None,
                 check_exists: bool = False) -> str:
        """Get resource file path from a given resource's directory by filename.
        example:
            schemas_files.get_path("events", ext="", check_exists=True)
            schemas_files.get_path("events")
        :param filename: resource file name
        :type filename: str
        :param ext: resource name,
            if not given, use the class ext, defaults to None
        :type ext: str, optional
        :param check_exists: check if the resource file exists,
            defaults to False
        :type check_exists: bool, optional
        :raises FileNotFoundError: resource not exists
        :return: resource file absolute path
        :rtype: str
        """
        ext = ext if ext is not None else self.ext
        abspath = os.path.join(self.base_path, f"{filename}{ext}")
        if check_exists and not os.path.isfile(abspath):
            raise FileNotFoundError(f"Invalid file : {abspath}")
        return abspath

    def get_json(self, filename: str, ext: str = None) -> str:
        """Get a resource file path from a given resources directory by filename.
        example:
            schema_files.get_json("events.json","")
            schema_files.get_json("events")
        :param filename: resource file name
        :type filename: str
        :param ext: resource name,
            if not given use the class ext, defaults to None
        :type ext: str, optional
        :return: resource file absolute path
        :rtype: str
        """
        abspath = self.get_path(filename, check_exists=True)
        with open(abspath, 'r', encoding='utf-8') as f:
            json_content = json.load(f)
        return json_content
