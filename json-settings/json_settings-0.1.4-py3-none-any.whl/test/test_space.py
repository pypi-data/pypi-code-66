import unittest

from json_settings import Space
from json_settings import Settings
from json_settings import NumberSetting


class MainSettings(Settings):

    @Settings.assign
    def __init__(self, values):
        self.a = Float
        self.b = Float
        self.c = Float
        self.badger = str


class MainSettingsMany(Settings):

    @Settings.assign
    def __init__(self, values):
        self.a = Float
        self.b = Float
        self.c = Float
        self.d = Float
        self.e = Float
        self.f = Float
        self.badger = str


class RestrictSettings(Settings):
    @Settings.assign
    def __init__(self, values):
        self.item = DepthOne
        self.object = DepthTwo


class DepthOne(Settings):

    @Settings.assign
    def __init__(self, values):
        self.a = Float
        self.fish = str


class DepthTwo(Settings):

    @Settings.assign
    def __init__(self, values):
        self.a = Float
        self.dog = str


class Float(NumberSetting):

    @NumberSetting.assign
    def __init__(self, value):
        self.type = float

    def check(self):
        pass


class TestSpace(unittest.TestCase):
    """The unit tests for the :class:`~.Space` class.

    """
    def test_initialisation(self):
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        c = [7.0, 8.0, 9.0]
        values = {
            "a": {
                "array": a
            },
            "b": {
                "array": b
            },
            "c": {
                "array": c
            },
            "badger": "creature"
        }

        s = MainSettings(values)
        space = Space(s)
        self.assertEqual(space.shape, (3, 3, 3))

    def test_array_values_correct(self):
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        c = [7.0, 8.0, 9.0]
        values = {
            "a": {
                "array": a
            },
            "b": {
                "array": b
            },
            "c": {
                "array": c
            },
            "badger": "creature"
        }

        s = MainSettings(values)
        space = Space(s)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    self.assertEqual(space[i, j, k].a, a[i])
                    self.assertEqual(space[i, j, k].b, b[j])
                    self.assertEqual(space[i, j, k].c, c[k])
                    self.assertEqual(space[i, j, k].badger, "creature")

    def test_many_dimensions(self):
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        c = [7.0, 8.0, 9.0]
        d = [10.0, 11.0, 12.0]
        e = [13.0, 14.0, 15.0]
        f = [16.0, 17.0, 18.0]
        values = {
            "a": {
                "array": a
            },
            "b": {
                "array": b
            },
            "c": {
                "array": c
            },
            "d": {
                "array": d
            },
            "e": {
                "array": e
            },
            "f": {
                "array": f
            },
            "badger": "creature"
        }

        s = MainSettingsMany(values)
        space = Space(s)
        for ai in range(3):
            for bi in range(3):
                for ci in range(3):
                    for di in range(3):
                        for ei in range(3):
                            for fi in range(3):
                                self.assertEqual(
                                    space[ai, bi, ci, di, ei, fi].a, a[ai])
                                self.assertEqual(
                                    space[ai, bi, ci, di, ei, fi].b, b[bi])
                                self.assertEqual(
                                    space[ai, bi, ci, di, ei, fi].c, c[ci])
                                self.assertEqual(
                                    space[ai, bi, ci, di, ei, fi].d, d[di])
                                self.assertEqual(
                                    space[ai, bi, ci, di, ei, fi].e, e[ei])
                                self.assertEqual(
                                    space[ai, bi, ci, di, ei, fi].f, f[fi])
                                self.assertEqual(
                                    space[ai, bi, ci, di, ei, fi].badger,
                                    "creature")

    def test_match(self):
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        c = [7.0, 8.0, 9.0]
        values = {
            "a": {
                "array": a,
                "match": "f"
            },
            "b": {
                "array": b
            },
            "c": {
                "array": c,
                "match": "f"
            },
            "badger": "creature"
        }

        s = MainSettings(values)
        space = Space(s)
        for i in range(3):
            for j in range(3):
                self.assertEqual(space[i, j].a, a[j])
                self.assertEqual(space[i, j].b, b[i])
                self.assertEqual(space[i, j].c, c[j])
                self.assertEqual(space[i, j].badger, "creature")

    def test_many_match(self):
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        c = [7.0, 8.0, 9.0]
        d = [10.0, 11.0, 12.0]
        e = [13.0, 14.0, 15.0]
        f = [16.0, 17.0, 18.0]
        values = {
            "a": {
                "array": a,
                "match": "first"
            },
            "b": {
                "array": b,
                "match": "second"
            },
            "c": {
                "array": c,
                "match": "first"
            },
            "d": {
                "array": d
            },
            "e": {
                "array": e
            },
            "f": {
                "array": f,
                "match": "second"
            },
            "badger": "creature"
        }

        s = MainSettingsMany(values)
        space = Space(s)
        for ai in range(3):
            for bi in range(3):
                for ci in range(3):
                    for di in range(3):

                        self.assertEqual(
                            space[ai, bi, ci, di].a, a[ci])
                        self.assertEqual(
                            space[ai, bi, ci, di].b, b[di])
                        self.assertEqual(
                            space[ai, bi, ci, di].c, c[ci])
                        self.assertEqual(
                            space[ai, bi, ci, di].d, d[ai])
                        self.assertEqual(
                            space[ai, bi, ci, di].e, e[bi])
                        self.assertEqual(
                            space[ai, bi, ci, di].f, f[di])
                        self.assertEqual(
                            space[ai, bi, ci, di].badger,
                            "creature")

    def test_restrict(self):
        array = [1.0, 2.0, 3.0]
        values = {
            "item": {
                "a": {
                    "array": array
                },
                "fish": "carp"
            },
            "object": {
                "a": {
                    "array": array
                },
                "dog": "terrier"
            }
        }

        settings = RestrictSettings(values)

        space = Space(settings, {"object": "a"})

        self.assertEqual(space.shape, (3,))
        self.assertEqual(space[1].item.a, 2.0)
        self.assertEqual(space[1].object.a, array)
