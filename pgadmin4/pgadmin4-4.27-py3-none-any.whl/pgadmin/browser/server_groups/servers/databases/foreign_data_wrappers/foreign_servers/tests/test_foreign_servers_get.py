##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2020, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################


import uuid

from pgadmin.browser.server_groups.servers.databases.extensions.tests import \
    utils as extension_utils
from pgadmin.browser.server_groups.servers.databases.foreign_data_wrappers.\
    tests import utils as fdw_utils
from pgadmin.browser.server_groups.servers.databases.tests import \
    utils as database_utils
from pgadmin.utils.route import BaseTestGenerator
from regression import parent_node_dict
from regression.python_test_utils import test_utils as utils
from . import utils as fsrv_utils
from unittest.mock import patch


class ForeignServerGetTestCase(BaseTestGenerator):
    """This class will get foreign server properties under FDW node."""
    skip_on_database = ['gpdb']
    scenarios = utils.generate_scenarios('foreign_server_get',
                                         fsrv_utils.test_cases)

    def setUp(self):
        """ This function will create extension and foreign data wrapper."""
        super(ForeignServerGetTestCase, self).setUp()
        self.schema_data = parent_node_dict['schema'][-1]
        self.server_id = self.schema_data['server_id']
        self.db_id = self.schema_data['db_id']
        self.db_name = parent_node_dict["database"][-1]["db_name"]
        self.schema_name = self.schema_data['schema_name']
        self.extension_name = "cube"
        self.fdw_name = "fdw_%s" % (str(uuid.uuid4())[1:8])
        self.fsrv_name = "test_fsrv_add_%s" % (str(uuid.uuid4())[1:8])
        self.extension_id = extension_utils.create_extension(
            self.server, self.db_name, self.extension_name, self.schema_name)
        self.fdw_id = fdw_utils.create_fdw(self.server, self.db_name,
                                           self.fdw_name)
        self.fsrv_id = fsrv_utils.create_fsrv(self.server, self.db_name,
                                              self.fsrv_name, self.fdw_name)

    def get_foreign_server(self):
        """
        This function returns the foreign server get response
        :return: foreign server get response
        """
        return self.tester.get(self.url + str(utils.SERVER_GROUP) + '/' +
                               str(self.server_id) + '/' +
                               str(self.db_id) + '/' +
                               str(self.fdw_id) + '/' +
                               str(self.fsrv_id),
                               content_type='html/json')

    def get_foreign_server_list(self):
        """
        This functions returns the foreign server list
        :return: foreign server list
        """
        return self.tester.get(self.url + str(utils.SERVER_GROUP) + '/' +
                               str(self.server_id) + '/' +
                               str(self.db_id) + '/' +
                               str(self.fdw_id) + "/",
                               content_type='html/json')

    def runTest(self):
        """This function will get foreign server properties present under test
        database."""
        db_con = database_utils.connect_database(self,
                                                 utils.SERVER_GROUP,
                                                 self.server_id,
                                                 self.db_id)
        if not db_con["info"] == "Database connected.":
            raise Exception("Could not connect to database.")
        fdw_response = fdw_utils.verify_fdw(self.server, self.db_name,
                                            self.fdw_name)
        if not fdw_response:
            raise Exception("Could not find FDW.")

        if self.is_positive_test:
            if hasattr(self, "foreign_server_list"):
                fsrv_response = self.get_foreign_server_list()
            else:
                fsrv_response = self.get_foreign_server()
        else:
            if hasattr(self, "error_fetching_fsrv"):
                with patch(self.mock_data["function_name"],
                           return_value=eval(self.mock_data["return_value"])):
                    if hasattr(self, "foreign_server_list"):
                        fsrv_response = self.get_foreign_server_list()
                    else:
                        fsrv_response = self.get_foreign_server()

            if hasattr(self, "wrong_fsrv_id"):
                self.fsrv_id = 99999
                fsrv_response = self.get_foreign_server()

        actual_response_code = fsrv_response.status_code
        expected_response_code = self.expected_data['status_code']
        self.assertEqual(actual_response_code, expected_response_code)

    def tearDown(self):
        """This function disconnect the test database and drop added extension
         and dependant objects."""
        extension_utils.drop_extension(self.server, self.db_name,
                                       self.extension_name)
        database_utils.disconnect_database(self, self.server_id, self.db_id)
