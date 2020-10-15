##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2020, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

import uuid
import json

from pgadmin.utils import server_utils as server_utils
from pgadmin.utils.route import BaseTestGenerator
from regression import parent_node_dict
from regression.python_test_utils import test_utils as utils
from . import utils as resource_groups_utils


class ResourceGroupsDeleteTestCase(BaseTestGenerator):
    """This class will delete the resource groups"""
    scenarios = [
        ('Delete multiple resource groups',
         dict(url='/browser/resource_group/obj/'))
    ]

    def setUp(self):
        self.server_id = parent_node_dict["server"][-1]["server_id"]
        server_response = server_utils.connect_server(self, self.server_id)
        if not server_response["info"] == "Server connected.":
            raise Exception("Could not connect to server to add resource "
                            "groups.")
        if "type" in server_response["data"]:
            if server_response["data"]["type"] == "pg":
                message = "Resource groups are not supported by PG."
                self.skipTest(message)
            else:
                if server_response["data"]["version"] < 90400:
                    message = "Resource groups are not supported by PPAS " \
                              "9.3 and below."
                    self.skipTest(message)
        self.resource_groups = ["test_resource_group_delete%s" %
                                str(uuid.uuid4())[1:8],
                                "test_resource_group_delete%s" %
                                str(uuid.uuid4())[1:8]]
        self.resource_group_ids = [
            resource_groups_utils.create_resource_groups(
                self.server, self.resource_groups[0]),
            resource_groups_utils.create_resource_groups(
                self.server, self.resource_groups[1])]

    def runTest(self):
        """This function will delete resource groups."""
        resource_grp_response = resource_groups_utils.verify_resource_group(
            self.server, self.resource_groups[0])
        if not resource_grp_response:
            raise Exception("Could not find the resource group to fetch.")

        resource_grp_response = resource_groups_utils.verify_resource_group(
            self.server, self.resource_groups[1])
        if not resource_grp_response:
            raise Exception("Could not find the resource group to fetch.")

        data = {'ids': self.resource_group_ids}
        response = self.tester.delete(
            "{0}{1}/{2}/".format(self.url,
                                 utils.SERVER_GROUP,
                                 self.server_id),
            follow_redirects=True,
            data=json.dumps(data),
            content_type='html/json'
        )
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """This function delete the resource group from the database."""
        connection = utils.get_db_connection(self.server['db'],
                                             self.server['username'],
                                             self.server['db_password'],
                                             self.server['host'],
                                             self.server['port'],
                                             self.server['sslmode'])
        resource_groups_utils.delete_resource_group(connection,
                                                    self.resource_groups[0])
        connection = utils.get_db_connection(self.server['db'],
                                             self.server['username'],
                                             self.server['db_password'],
                                             self.server['host'],
                                             self.server['port'],
                                             self.server['sslmode'])
        resource_groups_utils.delete_resource_group(connection,
                                                    self.resource_groups[1])
