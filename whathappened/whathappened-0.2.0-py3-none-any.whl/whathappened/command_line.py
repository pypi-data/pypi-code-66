from whathappened import changelog
from whathappened.git_commits import get_commits


def main():
    commits = get_commits()
    versions = changelog.compile_log(commits)
    log = changelog.format_log(versions)
    changelog.write_log(log, "CHANGELOG.md")


if __name__ == '__main__':
    main()
