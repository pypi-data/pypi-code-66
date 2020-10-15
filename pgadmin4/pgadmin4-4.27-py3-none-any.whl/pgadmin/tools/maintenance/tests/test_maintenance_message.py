##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2020, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

from pgadmin.tools.maintenance import Message
from pgadmin.utils.route import BaseTestGenerator


class MaintenanceMessageTest(BaseTestGenerator):
    """Test the Maintenance Message class"""
    scenarios = [
        ('When maintained the server',
         dict(
             class_params=dict(
                 sid=1,
                 data={
                     'database': 'postgres',
                     'op': 'VACUUM',
                     'vacuum_analyze': False,
                     'vacuum_freeze': False,
                     'vacuum_full': False,
                     'verbose': True
                 },
                 cmd="VACUUM VERBOSE;\n"
             ),
             expected_msg="Maintenance (Vacuum)",
             expected_details_cmd='VACUUM VERBOSE;'

         )),
        ('When maintained the server with FULL VERBOSE options',
         dict(
             class_params=dict(
                 sid=1,
                 data={
                     'database': 'postgres',
                     'op': 'VACUUM',
                     'vacuum_analyze': False,
                     'vacuum_freeze': False,
                     'vacuum_full': True,
                     'verbose': True
                 },
                 cmd="VACUUM FULL VERBOSE;\n"
             ),
             expected_msg="Maintenance (Vacuum)",
             expected_details_cmd='VACUUM FULL VERBOSE;'

         )),
        ('When maintained the server with ANALYZE',
         dict(
             class_params=dict(
                 sid=1,
                 data={
                     'database': 'postgres',
                     'op': 'ANALYZE',
                     'vacuum_analyze': False,
                     'vacuum_freeze': False,
                     'vacuum_full': False,
                     'verbose': True
                 },
                 cmd="ANALYZE VERBOSE;\n"
             ),
             expected_msg="Maintenance (Analyze)",
             expected_details_cmd='ANALYZE VERBOSE;'

         )),
        ('When maintained the server with REINDEX',
         dict(
             class_params=dict(
                 sid=1,
                 data={
                     'database': 'postgres',
                     'op': 'REINDEX',
                     'vacuum_analyze': False,
                     'vacuum_freeze': False,
                     'vacuum_full': False,
                     'verbose': False
                 },
                 cmd="REINDEX;\n"
             ),
             expected_msg="Maintenance (Reindex)",
             expected_details_cmd='REINDEX;'

         )),
        ('When maintained the server with CLUSTER',
         dict(
             class_params=dict(
                 sid=1,
                 data={
                     'database': 'postgres',
                     'op': 'CLUSTER',
                     'vacuum_analyze': False,
                     'vacuum_freeze': False,
                     'vacuum_full': False,
                     'verbose': True
                 },
                 cmd="CLUSTER VERBOSE;\n"
             ),
             expected_msg="Maintenance (Cluster)",
             expected_details_cmd='CLUSTER VERBOSE;'

         )),
    ]

    def runTest(self):
        maintenance_obj = Message(
            self.class_params['sid'],
            self.class_params['data'],
            self.class_params['cmd']
        )

        # Check the expected message returned
        self.assertEqual(maintenance_obj.message, self.expected_msg)

        # Check the command
        obj_details = maintenance_obj.details(self.class_params['cmd'], None)
        self.assertIn(self.expected_details_cmd, obj_details)
