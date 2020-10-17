from whathappened.git_commits import get_commits


def test_get_commits():
    commits = get_commits()[-1]

    print(commits)

    expected = {
        'hash': '4094d22846daea951c4fe0d74abb2a798e9a3404',
        'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
        'date': 'Sat Oct 17 13:19:28 2020 +0200',
        'message': '',
        'title': 'Initial commit',
    }

    assert commits == expected
