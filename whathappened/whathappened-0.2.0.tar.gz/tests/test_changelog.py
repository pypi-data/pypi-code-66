import pytest

from whathappened import changelog as cl


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            "Break feat(readme): specify expected message format",
            {
                'description': 'specify expected message format',
                'type': 'feat',
                'scope': 'readme',
                'is_breaking': True,
                'is_feature': True,
                'is_fix': False,
            },
        ),
        (
            "BREAKING fix (code): repair things",
            {
                'description': 'repair things',
                'type': 'fix',
                'scope': 'code',
                'is_breaking': True,
                'is_feature': False,
                'is_fix': True,
            },
        ),
        (
            "breaking fix: repair things",
            {
                'description': 'repair things',
                'type': 'fix',
                'scope': None,
                'is_breaking': True,
                'is_feature': False,
                'is_fix': True,
            },
        ),
        (
            "fix: add inspiration",
            {
                'description': 'add inspiration',
                'type': 'fix',
                'scope': None,
                'is_breaking': False,
                'is_feature': False,
                'is_fix': True,
            },
        ),
        (
            "docs (readme): add badges",
            {
                'description': 'add badges',
                'type': 'docs',
                'scope': 'readme',
                'is_breaking': False,
                'is_feature': False,
                'is_fix': False,
            },
        ),
        (
            "build(actions): create python-app.yml for github action's",
            {
                'description': 'create python-app.yml for github action\'s',
                'type': 'build',
                'scope': 'actions',
                'is_breaking': False,
                'is_feature': False,
                'is_fix': False,
            },
        ),
        (
            "Initial commit",
            {
                'description': 'Initial commit',
                'type': 'other',
                'scope': None,
                'is_breaking': False,
                'is_feature': False,
                'is_fix': False,
            },
        ),
    ],
)
def test_commit_title_parsing(test_input, expected):
    commit = cl.Commit({'hash': '00000', 'title': test_input})

    commit_attr = {}
    for attr in expected.keys():
        commit_attr[attr] = getattr(commit, attr)

    print(commit_attr)

    assert commit_attr == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            [
                {
                    'hash': 'e324c324df48a76113ad9b3c0887f161324046e4',
                    'tags': ['v0.1.1'],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 17:30:25 2020 +0200',
                    'message': '',
                    'title': 'breaking feat(readme): specify expected message format',
                },
                {
                    'hash': '7b4e7e657f9e3f2f4033cc5f47bcc637f5799fe9',
                    'tags': [],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 15:00:48 2020 +0200',
                    'message': '',
                    'title': 'breaking fix (code): repair things',
                },
                {
                    'hash': '7b4e7e657f9e3f2f4033cc5f47bcc637f5799fe9',
                    'tags': [],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 15:00:48 2020 +0200',
                    'message': '',
                    'title': 'breaking fix: repair things',
                },
                {
                    'hash': '7b4e7e657f9e3f2f4033cc5f47bcc637f5799fe9',
                    'tags': [],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 15:00:48 2020 +0200',
                    'message': '',
                    'title': 'fix: add inspiration',
                },
                {
                    'hash': 'f60445bba0ac48e12ce6be5526644037234ae500',
                    'tags': ['v0.0.1'],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 15:00:31 2020 +0200',
                    'message': '',
                    'title': 'docs (readme): add badges',
                },
                {
                    'hash': '9e57ba91f54244af913931c017480a39605c15f9',
                    'tags': [],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 13:55:04 2020 +0200',
                    'message': (
                        'Setup Python 3.6 on ubuntu-latest\n'
                        'Install pipenv and dependencies\n'
                        'Test'
                    ),
                    'title': 'build(actions): create python-app.yml for github actions',
                },
                {
                    'hash': '4094d22846daea951c4fe0d74abb2a798e9a3404',
                    'tags': ['v0.0.0'],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 13:19:28 2020 +0200',
                    'message': '',
                    'title': 'Initial commit',
                },
            ],
            """# Changelog

## v0.1.1 (2020-10-17)

### Features

* Readme - specify expected message format [BREAKING]

### Fixes

* Add inspiration
* Repair things [BREAKING]
* Code - repair things [BREAKING]


## v0.0.1 (2020-10-17)

### Docs

* Readme - add badges


## v0.0.0 (2020-10-17)

### Other

* Initial commit
""",
        )
    ],
)
def test_changelog(test_input, expected):
    start = None
    end = None
    commits = test_input
    commits = cl.filter_commits(commits, start, end)
    versions = cl.compile_log(commits)
    log = cl.format_log(versions)

    print(log)

    assert log == expected
