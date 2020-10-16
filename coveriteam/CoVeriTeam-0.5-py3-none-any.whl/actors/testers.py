# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

from coveriteam.language.actor import TestGenerator
from coveriteam.language.atomicactor import AtomicActor
from coveriteam.language.artifact import CProgram, TestSpecification, TestSuite


class ProgramTester(TestGenerator, AtomicActor):
    _input_artifacts = {"program": CProgram, "test_spec": TestSpecification}
    _output_artifacts = {"test_suite": TestSuite}
    _result_files_patterns = ["**/test-suite/*"]

    # It is a deliberate decision to not have the init function. We do not want anyone to
    # create instances of this class.

    def _prepare_args(self, program, test_spec):
        return [program.path, test_spec.path]

    def _extract_result(self):
        # extract result
        # Yes, test suite is directory.
        for file in self.log_dir().glob("**/test-suite"):
            ts = TestSuite(file)

        return {"test_suite": ts}
