# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

from coveriteam.interpreter.file_collector import collect_files
from coveriteam.language.actorconfig import ActorDefinitionLoader
from functools import reduce
import os
import sys
import requests
from pathlib import Path
import zipfile

CVT_REMOTE_URL = "https://coveriteam.sosy-lab.org/execute"
CVT_REMOTE_URL = "http://127.0.0.1:5000/execute"
load_config = ActorDefinitionLoader.load_config
collect_included_files = ActorDefinitionLoader.collect_included_files


def get_included_configs(fs):
    ActorDefinitionLoader.add_constructor("!include", ActorDefinitionLoader.include)
    included_files = []
    for f in fs:
        if Path(f).suffix == ".yml":
            included_files += collect_included_files(load_config(f))
    return included_files


def expand_file_paths(paths):
    expanded = []
    for p in paths:
        if os.path.isabs(p):
            sys.exit(
                "There is a file with absolute path. Please use only relative paths."
            )
        if os.path.isdir(p):
            expanded += [str(x) for x in Path(p).rglob("*") if x.is_file()]
        else:
            expanded += [p]
    return expanded


def exec_remotely(inputs, cvt_file):
    # Collect files
    fs = collect_files(cvt_file)
    # TODO check if inputs are actually file paths
    input_paths = [v for _, v in inputs]
    files_needed = [cvt_file] + fs + input_paths
    files_needed = expand_file_paths(files_needed)
    if reduce(lambda x, y: x or y, map(os.path.isabs, files_needed)):
        sys.exit("There is a file with absolute path. Please use only relative paths.")

    # collect all the required yml files.
    files_needed += get_included_configs(files_needed)

    # Preparing inputs
    cp = os.path.commonpath(list(map(os.path.abspath, files_needed)))
    working_dir = os.path.relpath(os.getcwd(), cp)
    json = {
        "coveriteam_inputs": inputs,
        "cvt_program": cvt_file,
        "working_directory": working_dir,
        "filenames": files_needed,
    }
    res = call_service(json)
    show_result(res)


def call_service(data):
    response = requests.post(CVT_REMOTE_URL, json=data)
    return response


def show_result(response):
    if response.status_code != 200:
        show_error(response)
        return
    output_dir = Path("cvt-output")
    if not output_dir.exists():
        output_dir.mkdir()

    archive_path = output_dir / "ar.zip"

    with archive_path.open("wb") as f:
        f.write(response.content)

    with zipfile.ZipFile(archive_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)

    with (output_dir / "LOG").open("r") as log:
        print(log.read())


def show_error(response):
    if response.json().get("message", None):
        print("Server returned an error with  message: %s" % response.json()["message"])
    else:
        print(
            "Unexpected response from the server. Please contact the development team."
        )
