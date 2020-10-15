import os
import unittest
from parfis.cmodule.parfisdll import ParfisAPI

class TestAPI(unittest.TestCase):
    def test_parfisdll_exists(self):
        pfs = ParfisAPI
        fname = "./api_test_1.log"
        pfs.set_log_file(fname)
        # os.exists("./api_test_1.log")
        self.assertTrue(os.path.exists(fname))
        fi = open(fname,"r")
        fistr = fi.read()
        self.assertTrue(fistr == "------------------------\n-- ParfisAPI log file --\n------------------------\n")
        fi.close()
        os.remove(fname)
        self.assertFalse(os.path.exists(fname))