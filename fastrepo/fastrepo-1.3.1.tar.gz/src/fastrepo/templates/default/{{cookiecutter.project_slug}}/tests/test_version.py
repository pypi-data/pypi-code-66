"""A test to check that version respects semver convention.

Tt also illustrates pytest fixture usage.
"""
import re


def test_semver_version(version: str) -> None:
    """Receive version from fixture and check that it is a valid semver version."""
    # Recommended regexp for semver string: https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
    SEMVER_REGEXP = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"  # noqa: E501
    matched = re.search(SEMVER_REGEXP, version)
    # Make sure there is a match
    assert matched is not None
    # This is mainly for mypy
    assert matched.lastindex
    # This one checks that major, minor and patch digits are specified
    assert matched.lastindex >= 3
