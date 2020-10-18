# The MIT License (MIT)
#
# Copyright (c) 2020 Thorsten Simons (sw@snomis.eu)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import httpx
import ssl
import json
import sys
from collections import OrderedDict as OD
from typing import List

from .combase import ApiConBase, printstep


class ApiConSystem(ApiConBase):
    """
    Connection class to deal with system configuration export
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.export = {"name": self.pkgname,
                       "description": self.pkgdesc,
                       "businessObjectRequest": {"specifications": []},
                       "systemConfigImportExport": {"securitySettings": None,
                                                    "identityProviders": [],
                                                    "groups": [],
                                                    "roles": [],
                                                    "notificationRules": [],
                                                    "clientCertificates": [],
                                                    "systemCertificates": [],
                                                    "selectedForImport": []
                                                    },
                       "pluginBundleImportExport": {"pluginBundles": [],
                                                    "conflicts": [],
                                                    "selectedPluginBundleUniqueIds": []
                                                    }
        }

        self._build = None

    def get_businessObjects(self) -> list:
        """
        Get a list of known business objects.
        """
        printstep('\tretrieving business objects', 40)

        r = self.client.get(f'/api/admin/businessObjects/namespaces',
                            params={'includeCount':True,
                                    'exportableOnly': True,
                                    'useUploadedPackage': False}
                            )

        ret = []
        if r.status_code == 200:
            ret = r.json()
            for bo in ret:
                self.export['businessObjectRequest']['specifications'].append(
                    {'namespace': {'namespace': bo['namespace'],
                                   'type': bo['type']}})
            print('OK')
        else:
            sys.exit(f'fatal: failed retrieving known type/namespace combinations'
                     f' - http {r.status_code}')

    def get_securitysettings(self) -> dict:
        """
        Get the security settings.
        """
        printstep('\tretrieving security settings', 40)

        r = self.client.get(f'/api/admin/security/settings')

        ret = []
        if r.status_code == 200:
            ret = r.json()
            self.export['systemConfigImportExport']['securitySettings'] = ret
            print('OK')
        else:
            sys.exit(f'fatal: failed to retrieve system certificates - http {r.status_code}')

    def get_identityProviders(self) -> list:
        """
        Get the list of IDPs.
        """
        printstep('\tretrieving identity providers', 40)

        r = self.client.get(f'/api/admin/security/identityProviders')

        selectedForImport = []
        if r.status_code == 200:
            ret = r.json()
            for i in ret:
                selectedForImport.append(i['uuid'])

            self.export['systemConfigImportExport']['identityProviders'] = ret
            self.export['systemConfigImportExport']['selectedForImport'] += selectedForImport
            print('OK')
        else:
            sys.exit(f'fatal: failed to retrieve groups - http {r.status_code}')

    def get_groups(self) -> list:
        """
        Get the list of groups.
        """
        printstep('\tretrieving groups', 40)

        r = self.client.get(f'/api/admin/security/groups')

        selectedForImport = []
        if r.status_code == 200:
            ret = r.json()
            for i in ret:
                selectedForImport.append(i['uuid'])

            self.export['systemConfigImportExport']['groups'] = ret
            self.export['systemConfigImportExport']['selectedForImport'] += selectedForImport
            print('OK')
        else:
            sys.exit(f'fatal: failed to retrieve identity providers - http {r.status_code}')

    def get_roles(self) -> list:
        """
        Get the list of roles.
        """
        printstep('\tretrieving roles', 40)

        r = self.client.get(f'/api/admin/security/roles')

        selectedForImport = []
        if r.status_code == 200:
            ret = r.json()
            for i in ret:
                selectedForImport.append(i['uuid'])

            self.export['systemConfigImportExport']['roles'] = ret
            self.export['systemConfigImportExport']['selectedForImport'] += selectedForImport
            print('OK')
        else:
            sys.exit(f'fatal: failed to retrieve roles - http {r.status_code}')

    def get_notificationRules(self) -> list:
        """
        Get the list of roles.
        """
        printstep('\tretrieving notification rules', 40)

        r = self.client.get(f'/api/admin/notifications')

        selectedForImport = []
        if r.status_code == 200:
            ret = r.json()
            for i in ret:
                selectedForImport.append(i['uuid'])

            self.export['systemConfigImportExport']['notificationRules'] = ret
            self.export['systemConfigImportExport']['selectedForImport'] += selectedForImport
            print('OK')
        else:
            sys.exit(f'fatal: failed to notification rules - http {r.status_code}')

    def get_systemcerts(self) -> dict:
        """
        Get the client certificates.
        """
        printstep('\tretrieving system certificates', 40)

        r = self.client.get(f'/api/admin/certificates/system')

        ret = []
        if r.status_code == 200:
            ret = r.json()
            self.export['systemConfigImportExport']['systemCertificates'] = [ret]
            print('OK')
        else:
            sys.exit(f'fatal: failed to retrieve system certificates - http {r.status_code}')

    def get_clientcerts(self) -> List[dict]:
        """
        Get the client certificates.
        """
        printstep('\tretrieving client certificates', 40)

        r = self.client.get(f'/api/admin/certificates')

        ret = []
        if r.status_code == 200:
            ret = r.json()
            self.export['systemConfigImportExport']['clientCertificates'] = ret['certs']
            print('OK')
        else:
            sys.exit(f'fatal: failed to retrieve client certificates - http {r.status_code}')

    def get_pluginBundles(self) -> list:
        """
        Get the non.standard plugin bundles.
        """
        printstep('\tretrieving plugin bundles', 40)

        r = self.client.get(f'/api/admin/plugins/bundles')

        if r.status_code == 200:
            ret = r.json()
            for pb in ret:
                if not pb['builtIn']:
                    self.export['pluginBundleImportExport']['pluginBundles'].append(pb)
                    self.export['pluginBundleImportExport']['selectedPluginBundleUniqueIds'].append(pb['uniqueId'])

            print('OK')
        else:
            sys.exit(f'fatal: failed to retrieve plugin bundles - http {r.status_code}')

    def build(self):
        """
        Build the export.
        """
        self.get_businessObjects()
        self.get_securitysettings()
        self.get_identityProviders()
        self.get_groups()
        self.get_roles()
        self.get_notificationRules()
        self.get_clientcerts()
        self.get_systemcerts()
        self.get_pluginBundles()

        printstep('\tbuilding package', 40)

        r = self.client.post(f'/api/admin/package/build', data=json.dumps(self.export))

        if r.status_code == 200:
            ret = json.loads(r.text)
            print('OK')
            self._build = r.content
        else:
            sys.exit(f'fatal: build failed - http {r.status_code}, {r.text}')

    def export_systemconfig(self, filename: str):

        printstep('\texporting system config', 40)

        r = self.client.post('/api/admin/package/download',
                             headers={'Accept': 'application/octet-stream'},
                             data=self._build
                             )

        if r.status_code == 200:
            print(f'OK ({filename})')
            return r.content
        else:
            print(r.content)
            sys.exit(f'fatal: failed to export system config - http {r.status_code}')
