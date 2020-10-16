# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------


from ._core import AssetVersion


class Environment(AssetVersion):
    """This is a simple implementation of environment, will be replaced by the finalized one."""

    def __init__(self, python=None, docker=None):
        self._python = python
        self._docker = docker

    @property
    def docker(self):
        return self._docker

    @property
    def python(self):
        return self._python

    @classmethod
    def _from_dict(cls, dct):
        return cls(**dct)

    def _to_dict(self):
        return {
            'docker': self.docker,
            'python': self.python
        }

    def _to_aml_sdk_env(self):
        from azureml.core.environment import Environment, CondaDependencies
        env = Environment(name=None, _skip_defaults=True)
        conda = self.python.get('condaDependencies') if self.python else None
        if conda:
            env.python.conda_dependencies = CondaDependencies(_underlying_structure=conda)
        else:
            # If conda is not set, use the user's custom image.
            env.python.user_managed_dependencies = True
        if self.docker:
            if 'baseImage' in self.docker:
                env.docker.base_image = self.docker['baseImage']
        return env
