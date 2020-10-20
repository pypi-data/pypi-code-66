# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['azkv', 'azkv.controllers', 'azkv.core', 'azkv.ext', 'azkv.templates']

package_data = \
{'': ['*']}

install_requires = \
['azure-common>=1.1.25,<2.0.0',
 'azure-identity>=1.3.1,<1.4.0',
 'azure-keyvault-secrets>=4.2.0,<5.0.0',
 'cement>=3.0.4,<4.0.0',
 'colorlog>=4.2.1,<5.0.0',
 'jinja2>=2.11.2,<3.0.0',
 'pyyaml>=5.3.1,<6.0.0',
 'typing>=3.7.4,<4.0.0']

extras_require = \
{'code-format': ['black>=19.10b0,<20.0', 'blacken-docs>=1.7,<2.0'],
 'code-lint': ['flake8>=3.8,<4.0',
               'flake8-import-order>=0.18,<0.19',
               'flake8-bandit>=2.1,<3.0',
               'flake8-blind-except>=0.1,<0.2',
               'flake8-bugbear>=20.1,<21.0',
               'flake8-builtins>=1.5,<2.0',
               'flake8-docstrings>=1.5,<2.0',
               'flake8-logging-format>=0.6,<0.7',
               'flake8-mypy>=17.8,<18.0',
               'pep8-naming>=0.8,<0.9',
               'pygments>=2.6,<3.0'],
 'docs': ['recommonmark>=0.6.0,<0.7.0',
          'sphinx>=3.1,<4.0',
          'sphinx-rtd-theme>=0.5,<0.6',
          'sphinx-autodoc-typehints>=1.11,<2.0'],
 'test': ['pytest>=6.0,<7.0',
          'pytest-benchmark[aspect]>=3.2,<4.0',
          'pytest-cov>=2.10,<3.0',
          'pytest-instafail>=0.4,<0.5',
          'pytest-lazy-fixture>=0.6,<0.7',
          'pytest-random-order>=1.0,<2.0']}

entry_points = \
{'console_scripts': ['azkv = azkv.main:main']}

setup_kwargs = {
    'name': 'azkv',
    'version': '0.1.0rc6',
    'description': 'CLI client for the Azure Key Vault data plane',
    'long_description': '# AzKV\n\n[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)][PythonRef] [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)][BlackRef] [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)][MITRef]\n\n[PythonRef]: https://docs.python.org/3.6/\n[BlackRef]: https://github.com/ambv/black\n[MITRef]: https://opensource.org/licenses/MIT\n\n`AzKV` is a CLI client for the Azure Key Vault data plane with support for redundant vaults. It addresses the high reliability scenarios where it is expected that if a Key Vault is not available due to the Azure region-wide failure, the same data could be retrieved from a redundant Key Vault deployed in another unaffected region.\n\nThere is a [native Azure VM extension][AzExtKeyVaultRef] for Linux and Windows that could fetch the certificate and the corresponding secret key. It also performs a periodic check to see if the certificate has been changed and needs to be updated.\n\n[AzExtKeyVaultRef]: https://azure.microsoft.com/en-us/updates/azure-key-vault-virtual-machine-extension-now-generally-available/\n\nWhile this native extension can monitor a list of certificates, they all are fetched individually. So, if the certificate or the Key Vault are not available, there is no retry against a different vault. There is no straightforward hooking functionality to run a shell command if data is updated on the local file system. This extension also has limited support for different Linux distributions and does not support `RHEL` or `CentOS`.\n\nAt this point `AzKV` addresses these limitations of the native Azure VM extension. It allows to fetch PKCS12-formatted blobs form Azure Key Vault, BASE64-decode the data, extract certificate and private key from the PKCS12 package and save/update data on the file system in the PEM format, if retrieved content is different from what has been already saved. It also delivers a post-update hook functionality that allows to execute shell commands upon successful update. This post-update hook could be used to restart a service consuming the certificate/key when content is updated.\n\nWhile geared primarily towards fetching certificates from Key Vaults, current version of the tool could be also used to fetch secrets like passwords and incorporate them in your server or app configuration.\n\n## Getting Started\n\n### Installing\n\n`AzKV` is distributed through the [Python Package Index][PyPIRef] as [azkv][PyPIProjRef]. Run the following command to:\n\n[PyPIRef]: https://pypi.org\n[PyPIProjRef]:https://pypi.org/project/azkv/\n\n* install a specific version\n\n    ```sh\n    pip install "azkv==0.1"\n    ```\n\n* install the latest version\n\n    ```sh\n    pip install "azkv"\n    ```\n\n* upgrade to the latest version\n\n    ```sh\n    pip install --upgrade "azkv"\n    ```\n\n* install optional DEV dependencies like `pytest` framework and plugins necessary for performance and functional testing\n\n    ```sh\n    pip install "azkv[test]"\n    ```\n\n### Configuring\n\n`AzKV` looks for the `YAML` configuration file in the following locations:\n\n* `/etc/azkv/azkv.yaml`\n* `~/.config/azkv/azkv.yaml`\n* `~/.azkv/config/azkv.yaml`\n* `~/.azkv.yaml`\n\nHere is the [example configuration file][AzKVConfigRef]:\n\n[AzKVConfigRef]: config/etc/azkv_example.yaml\n\n```yaml\n### AzKV Configuration Settings\n---\nazkv:\n  # Toggle application level debug (does not toggle Cement framework debugging)\n  # debug: false\n\n  # Common credentials to be used for all vaults, unless some specific vaults\n  # have `credentials` property defined that overrides the common one.\n  credentials:\n    # Type of Azure credentials to use for Key Vault access.\n    # Possible values are:\n    # * `EnvironmentVariables` -  uses `EnvironmentCredential` to pickup service principal or user\n    #            credentials from environment variables.\n    #\n    # * `SystemManagedIdentity` - uses `ManagedIdentityCredential` class configured for system-assigned\n    #            managed identity.\n    #\n    # * `UserManagedIdentity` - uses `ManagedIdentityCredential` class configured for user-assigned\n    #            managed identity. Requires `client_id` or will be reduced to `SystemManagedIdentity`\n    type: EnvironmentVariables\n    # ClientID for the user-assigned managed identity; option required only for `type: UserManagedIdentity`\n    # client_id: 2343556b-7153-470a-908a-b3837db7ec88\n\n  # List of Azure Key Vaults to be referenced in AzKV operations\n  keyvaults:\n    # Short name for a Key Vault (used in logs and CLI options)\n    foo-prod-eastus:\n      # URL for the Azure Key Vault API endpoint\n      url: "https://foo-prod-eastus.vault.azure.net/"\n      # Credentials specific to this Key Vault. Supersedes common credentials above.\n      credentials:\n        type: UserManagedIdentity\n        client_id: 2343556b-7153-470a-908a-b3837db7ec88\n    foo-prod-uksouth:\n      url: "https://foo-prod-uksouth.vault.azure.net/"\n      credentials:\n        type: SystemManagedIdentity\n    foo-prod-ukwest:\n      url: "https://foo-prod-ukwest.vault.azure.net/"\n\n# Logging configuration\nlog.colorlog:\n  # Whether or not to colorize the log file.\n  # colorize_file_log: false\n\n  # Whether or not to colorize the console log.\n  # colorize_console_log: true\n\n  # Where the log file lives (no log file by default)\n  # file: null\n\n  # The level for which to log.  One of: info, warning, error, fatal, debug\n  # level: INFO\n\n  # Whether or not to log to console\n  # to_console: true\n\n  # Whether or not to rotate the log file when it reaches `max_bytes`\n  # rotate: false\n\n  # Max size in bytes that a log file can grow until it is rotated.\n  # max_bytes: 512000\n\n  # The maximun number of log files to maintain when rotating\n  # max_files: 4\n```\n\n## Usage\n\n\n\n## Requirements\n\n* Python >= 3.6\n\n## Built using\n\n* [Cement Framework][CementRef] - CLI application framework\n\n[CementRef]: https://builtoncement.com/\n\n## Versioning\n\nWe use [Semantic Versioning Specification][SemVer] as a version numbering convention.\n\n[SemVer]: http://semver.org/\n\n## Release History\n\nFor the available versions, see the [tags on this repository][RepoTags]. Specific changes for each version are documented in [CHANGELOG.md][ChangelogRef].\n\nAlso, conventions for `git commit` messages are documented in [CONTRIBUTING.md][ContribRef].\n\n[RepoTags]: https://github.com/undp/azkv/tags\n[ChangelogRef]: CHANGELOG.md\n[ContribRef]: CONTRIBUTING.md\n\n## Authors\n\n* **Oleksiy Kuzmenko** - [OK-UNDP@GitHub][OK-UNDP@GitHub] - *Initial design and implementation*\n\n[OK-UNDP@GitHub]: https://github.com/OK-UNDP\n\n## Acknowledgments\n\n* Hat tip to all individuals shaping design of this project by sharing their knowledge in articles, blogs and forums.\n\n## License\n\nUnless otherwise stated, all authors (see commit logs) release their work under the [MIT License][MITRef]. See [LICENSE.md][LicenseRef] for details.\n\n[LicenseRef]: LICENSE.md\n\n## Contributing\n\nThere are plenty of ways you could contribute to this project. Feel free to:\n\n* submit bug reports and feature requests\n* outline, fix and expand documentation\n* peer-review bug reports and pull requests\n* implement new features or fix bugs\n\nSee [CONTRIBUTING.md][ContribRef] for details on code formatting, linting and testing frameworks used by this project.\n',
    'author': 'Oleksiy Kuzmenko',
    'author_email': 'oleksiy.kuzmenko@undp.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/undp/azkv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
