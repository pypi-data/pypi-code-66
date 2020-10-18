import unittest

from mystix.language.evaluation.vars import Memory, OutOfMemoryError
from mystix.language.shared.primitives.values import IntegerValue, Value


class MemoryTests(unittest.TestCase):

    def test_fresh_location_no_set(self):
        m = Memory()
        l1 = m.get_fresh_loc()
        l2 = m.get_fresh_loc()
        self.assertEqual(l1,l2)

    def test_fresh_location_post_set(self):
        m = Memory()
        l1 = m.get_fresh_loc()
        m.write(l1, Value())
        l2 = m.get_fresh_loc()
        self.assertNotEqual(l1, l2)

    def test_set_get(self):
        m = Memory()
        l1 = m.get_fresh_loc()
        m.write(l1, IntegerValue(22))
        v: Value = m.read(l1)
        self.assertTrue(isinstance(v, IntegerValue))
        self.assertEqual(v.value, 22)

    def test_free_location_post_set(self):
        m = Memory()
        l1 = m.get_fresh_loc()
        m.write(l1, Value())
        m.free(l1)
        l2 = m.get_fresh_loc()
        self.assertEqual(l1, l2)

    def test_overwrite(self):
        m = Memory()
        l1 = m.get_fresh_loc()
        m.write(l1, IntegerValue(22))
        m.write(l1, IntegerValue(23))
        v: Value = m.read(l1)
        self.assertTrue(isinstance(v, IntegerValue))
        self.assertEqual(v.value, 23)

    def test_no_limit_on_fresh_no_write(self):
        m = Memory()
        for i in range(Memory.MAX_VALUES):
            m.get_fresh_loc()
        try:
            m.get_fresh_loc()
        except OutOfMemoryError:
            self.fail()

    def test_memory_limit(self):
        m = Memory()
        for i in range(Memory.MAX_VALUES):
            l = m.get_fresh_loc()
            m.write(l, IntegerValue(1))
        try:
            m.get_fresh_loc()
            self.fail()
        except OutOfMemoryError:
            pass
