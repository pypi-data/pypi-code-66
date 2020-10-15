import os
import shutil

from olutils import storing

TMP_DIR = "tmp"
MOCK_DIR = os.path.join("olutils", "tests", "mockups")


def assert_content_equal(path, content):
    with open(path) as file:
        assert file.read() == content


def readout(capfd):
    """Read output"""
    return capfd.readouterr()[0]


# --------------------------------------------------------------------------- #
# Setup / Teardown

def setup_function(function):
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)


def teardown_function(function):
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)


# --------------------------------------------------------------------------- #
# Tests

def test_rm_eol():
    assert storing.txt.rm_eol("hello") == "hello"
    assert storing.txt.rm_eol("hello\n") == "hello"
    assert storing.txt.rm_eol("hello\r\n") == "hello"
    assert storing.txt.rm_eol("hello\n\r") == "hello"
    assert storing.txt.rm_eol("hello \n") == "hello "


def test_read_txt():

    path = os.path.join(MOCK_DIR, "base_comma.csv")

    content_list = storing.read_txt(path)
    assert isinstance(content_list, list)
    assert content_list == [
        'col_1,col_2,col_3\n',
        '11,12,13\n',
        '21,22,""\n',
        '31,,33\n',
        'forty_one,forty_two,forty_three\n',
    ]

    content_iter = storing.read_txt(path, rtype='iter')
    assert not isinstance(content_iter, list)
    assert hasattr(content_iter, "__next__")
    assert list(content_iter) == content_list

    content_str = storing.read_txt(path, rtype='str')
    assert isinstance(content_str, str)
    assert content_str == "".join(content_list)

    content_list_clean = storing.read_txt(path, w_eol=False)
    assert content_list_clean == [l[:-1] for l in content_list]

    content_list_crlf = storing.read_txt(path, f_eol="\r\n")
    assert content_list_crlf == [l.replace("\n", "\r\n") for l in content_list]


def test_write_txt():

    path = os.path.join(TMP_DIR, "file.txt")

    clean_lines = ["Hi,", "Hope you are doing great.", "", "Bye"]
    content = "\n".join(clean_lines) + "\n"

    storing.write_txt(content, path)
    assert_content_equal(path, content)

    storing.write_txt(clean_lines, path, has_eol=False)
    assert_content_equal(path, content)

    lines = [line + "\n" for line in clean_lines]
    storing.write_txt(lines, path)
    assert_content_equal(path, content)