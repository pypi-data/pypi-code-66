# This file is part of BenchExec, a framework for reliable benchmarking:
# https://github.com/sosy-lab/benchexec
#
# SPDX-FileCopyrightText: 2007-2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import benchexec.tools.template
import benchexec.util as util


class Tool(benchexec.tools.template.BaseTool):
    """
    This tool selects the verifier backend for MetaVal based on the specification.
    url: https://gitlab.com/sosy-lab/software/metaval
    """

    _exec_path = "metaval-algo-selector.sh"

    def name(self):
        return "Algorithm (Verifier) Selector for MetaVal"

    def executable(self):
        return util.find_executable(self._exec_path)

    def version(self, executable):
        return self._version_from_tool(executable)

    def cmdline(self, executable, options, tasks, propertyfile, rlimits):
        # Not using the program file.
        return [executable] + options + ["--spec"] + [propertyfile or "None"]
