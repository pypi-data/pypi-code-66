from whathappened import changelog as cl
from whathappened.git_commits import get_commits


def test_changelog():
    start = 'v0.0.0'
    end = None
    commits = get_commits()
    commits = cl.filter_commits(commits, start, end)
    versions = cl.compile_log(commits)
    log = cl.format_log(versions)

    expected = """# Changelog

* add test_git_commits.py
* git_commits - blacken
* setup development environment
* git_commits - convert to Python3
* git_commits - add credit to original source
* add git_commits.py from existing Gist
* readme - specify expected message format
* readme - add inspiration
* readme - add badges
* actions - create python-app.yml for github actions
* Initial commit

"""
    print(log)

    assert log == expected
