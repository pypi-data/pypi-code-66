# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import yaml
import benchexec
from pathlib import Path
from coveriteam.util import (
    is_url,
    download_if_needed,
    unzip,
    create_cache_directories,
    get_ARCHIVE_DOWNLOAD_PATH,
)
import coveriteam.util as util
import re
from coveriteam.language import CoVeriLangException
import os


class ActorDefinitionLoader(yaml.SafeLoader):
    def __init__(self, stream):

        self._root = Path(stream.name).parent
        super(ActorDefinitionLoader, self).__init__(stream)

    def include(self, node):

        filename = self._root / self.construct_scalar(node)
        with filename.open("r") as f:
            d = yaml.load(f, ActorDefinitionLoader)  # noqa S506
            return dict_merge(d, {"imported_file": filename})

    @staticmethod
    def load_config(path):
        with open(path, "r") as f:
            try:
                d = yaml.load(f, ActorDefinitionLoader)  # noqa S506
            except yaml.YAMLError as e:
                msg = "Actor config yaml file {} is invalid: {}".format(path, e)
                raise CoVeriLangException(msg, 203)

            return d

    @staticmethod
    def resolve_includes(d):
        # Check if "imports" exist
        imports = d.pop("imports", None)
        if not imports:
            return d

        if not isinstance(imports, list):
            imports = [imports]

        di = {}
        for i in imports:
            i.pop("imported_file", None)
            di = dict_merge(ActorDefinitionLoader.resolve_includes(i), di)
        return dict_merge(di, d)

    @staticmethod
    def collect_included_files(d):
        f = d.pop("imported_file", None)
        f = [] if f is None else [str(f)]
        # Check if "imports" exist
        imports = d.pop("imports", None)
        if not imports:
            return f

        if not isinstance(imports, list):
            imports = [imports]

        fs = []
        for i in imports:
            fs += ActorDefinitionLoader.collect_included_files(i)
        return fs + f


class ActorConfig:
    def __init__(self, path):
        ActorDefinitionLoader.add_constructor("!include", ActorDefinitionLoader.include)
        create_cache_directories()
        self.path = path
        self.get_actor_config()
        self.actor_name = self._config["actor_name"]
        self.archive_location = self._config["archive"]["location"]
        self.options = self._config["options"]
        self.reslim = self._config["resourcelimits"]
        check_policy_compliance(self)
        # Keeping this path as str instead of Path because it is going to be used with string paths mostly.
        self.tool_dir = str(self.__install_if_needed())
        self.__resolve_tool_info_module()

    def get_actor_config(self):
        self._config = ActorDefinitionLoader.load_config(self.path)
        self._config = ActorDefinitionLoader.resolve_includes(self._config)
        self.__check_actor_definition_integrity()
        self.__sanitize_yaml_dict()

    def __check_actor_definition_integrity(self):
        # check if the essential tags are present.
        # Essentiality of tags can be defined in a schema.
        essential_tags = [
            "toolinfo_module",
            "resourcelimits",
            "actor_name",
            "archive",
            "format_version",
        ]
        diff = essential_tags - self._config.keys()
        if diff:
            msg = (
                "The following tags are missing in the actor config YAML: \n"
                + "\n".join(diff)
            )
            raise CoVeriLangException(msg, 200)

    def __sanitize_yaml_dict(self):
        # translate resource limits
        reslim = self._config.get("resourcelimits", None)
        if reslim:
            reslim["memlimit"] = benchexec.util.parse_memory_value(reslim["memlimit"])
            reslim["timelimit"] = benchexec.util.parse_timespan_value(
                reslim["timelimit"]
            )
            self._config["resourcelimits"] = reslim

    def __install_if_needed(self):
        archive_name = self.archive_location.rpartition("/")[2]
        if not archive_name:
            archive_name = self.actor_name + ".zip"

        archive = get_ARCHIVE_DOWNLOAD_PATH() / archive_name
        self.archive_name = archive_name
        downloaded = download_if_needed(self.archive_location, archive)

        target_dir = util.get_INSTALL_DIR() / self.actor_name
        # Check if the directory already exists and doesn't need to be updated.
        if not downloaded and target_dir.is_dir():
            return target_dir

        print("Installing the actor: " + self.actor_name + "......")
        unzip(archive, target_dir)
        return target_dir

    def __resolve_tool_info_module(self):
        """
        1. Check if it is a URL.
        2. If a URL then download it and save it to the TI cache.
        3. Infer the module name and return it.
        """
        ti = self._config["toolinfo_module"]
        if is_url(ti):
            filename = util.get_TOOL_INFO_DOWNLOAD_PATH() / ti.rpartition("/")[2]
            download_if_needed(ti, filename)
            ti = filename.name

        if ti.endswith(".py"):
            ti = ti.rpartition(".")[0]

        self.tool_name = ti


def dict_merge(d1, d2):
    # Supposed to update but not overwrite. Instead update.
    for k in d2.keys():
        if k in d1.keys() and isinstance(d1[k], dict) and isinstance(d2[k], dict):
            if isinstance(d1[k], dict) and isinstance(d2[k], dict):
                d1[k] = dict_merge(d1[k], d2[k])
            elif isinstance(d1[k], dict) or isinstance(d2[k], dict):
                # TODO this could be and XOR
                # We raise an error when one of the values is a dict, but not the other.
                msg = "YAML file could not be parsed. Clash in the tag: %r" % k
                raise CoVeriLangException(msg, 201)
            else:
                d1[k] = d2[k]
        else:
            d1[k] = d2[k]

    return d1


def load_policy(policy_file):
    if not policy_file:
        if os.getenv("COVERITEAM_POLICY"):
            policy_file = os.getenv("COVERITEAM_POLICY")
        else:
            return {}

    with open(policy_file, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            msg = "Failed to load policy from: {} Error is: {}".format(policy_file, e)
            raise CoVeriLangException(msg, 202)


def check_policy_compliance_allowed_locations(allowed_locations, archive_location):
    # Expression to match nothing.
    e = "a^"
    for loc in allowed_locations:
        e = "%s|(%s)" % (e, re.escape(loc))
    if not re.compile(e).match(archive_location):
        msg = "Not allowed to download from the url: %s" % archive_location
        raise CoVeriLangException(msg, 100)


def check_policy_compliance(ac, policy_file=None):
    policy = load_policy(policy_file)
    allowed_locations = policy.get("allowed_locations", None)
    if allowed_locations:
        check_policy_compliance_allowed_locations(
            allowed_locations, ac.archive_location
        )
