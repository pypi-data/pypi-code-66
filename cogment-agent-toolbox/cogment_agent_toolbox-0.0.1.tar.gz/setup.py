# Copyright 2019 Age of Minds inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""cogment agent toolbox packaging."""

from setuptools import setup, Command, find_packages
from setuptools.command.build_py import build_py as _build_py
from setuptools.command.develop import develop as _develop

class BuildProtos(Command):
    """Command to generate project *_pb2.py modules from proto files."""

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # due to limitations of the proto generator, we require that only *one*
        # directory is provided as an 'include' directory. We assume it's the '' key
        # to `self.distribution.package_dir` (and get a key error if it's not
        # there).
        from grpc.tools import command
        command.build_package_protos(self.distribution.package_dir[''])

class build_py(_build_py):
    def run(self):
        self.run_command('build_protos')
        super().run()
        

class develop(_develop):
    def run(self):
        self.run_command('build_protos')
        super().run()


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

version = {}
with open("cogment_agent_toolbox/version.py") as fp:
    exec(fp.read(), version)

setup(name='cogment_agent_toolbox',
      version=version['__version__'],
      description='Cogment Agent Toollbox',
      url='https://gitlab.com/ai-r/agent-toolbox',
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      author='Artificial Intelligence Redefined',
      author_email='dev+cogment@ai-r.com',
      license='Apache License 2.0',
      package_dir={'' : '.'},
      packages=['cogment_agent_toolbox', 'cogment_agent_toolbox.api'],
      include_package_data=True,
      tests_require=['pytest'],
      install_requires=[
          'grpcio>=1.32',
          'grpcio-reflection>=1.32',
          'protobuf>=3.7'
      ],
      setup_requires=['grpcio-tools>=1.32'],
      cmdclass={
        'build_protos': BuildProtos,
        'build_py': build_py,
        'develop': develop
      }
)
