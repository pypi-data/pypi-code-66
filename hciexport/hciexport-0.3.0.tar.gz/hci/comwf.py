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
from typing import List
from pprint import pprint

from .combase import ApiConBase, printstep


class ApiConWorkflows(ApiConBase):
    """
    Connection class to deal with Workflow export
    """
    def __init__(self, *args, **kwargs):
        """
        param hci:  the HCIs FQDN
        """
        super().__init__(*args, **kwargs)

    def get_wfobj(self, obj: str) -> List[str]:
        """
        Get a list of workflow objects from HCI.

        :param obj: a valid object name
        :returns:   a list of object UUIDs
        """
        printstep(f'\tretrieving {obj}', 40)

        r = self.client.get(f'/api/workflow/{obj.lower()}')

        uuids = []
        if r.status_code == 200:
            for x in r.json():
                uuids.append(x['uuid'])
            print(f'OK ({len(uuids)})')
        else:
            sys.exit(f'fatal: failed getting the {obj} list - http {r.status_code}')

        return uuids

    def export_workflows(self, filename):
        """
        Export Workflows including all components.
        """

        # collect all the UUIDs needed to build the query
        uuidcollection = {'workflows': None,
                          'dataSources': None,
                          'pipelines': None,
                          'indexes': None,
                          'contentClasses': None
                          }

        for obj in uuidcollection:
            if obj == 'modelVersion':
                continue
            uuidcollection[obj] = self.get_wfobj(obj)

        printstep('\texporting workflows', 40)

        r = self.client.post('/api/workflow/workflows/export',
                             json=uuidcollection)

        if r.status_code == 200:
            print(f'OK ({filename})')
            return r.text
        else:
            sys.exit(f'fatal: failed to export workflows - http {r.status_code}')
