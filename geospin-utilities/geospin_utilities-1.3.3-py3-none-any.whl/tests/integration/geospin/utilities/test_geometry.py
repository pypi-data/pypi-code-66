import pytest

from geospin.utilities.geometry import VG250GeometryParser


@pytest.mark.parametrize(
    'ags, expected',
    [
        ('00000000', 'STA'),
        ('06412000', 'KRS')
    ]
)
def test_vg250geometryparser_get_admin_level_suffix_from_ags_code(
        ags, expected):
    parser = VG250GeometryParser(None, None)
    result = parser._get_admin_level_suffix_from_ags_code(ags)
    assert expected == result
