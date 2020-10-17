class Commit:
    def __init__(self, commit_dict):
        self.commit_dict = commit_dict

    def __getattr__(self, name):

        try:
            return self.commit_dict[name]
        except KeyError:
            if name == 'header':
                return self.title.split(': ', 1)[0]
            elif name == 'description':
                return (
                    self.title.split(': ', 1)[1] if ': ' in self.title else self.title
                )
            elif name == 'type':
                return self.header.lower().split(' ', 1)[1 if self.is_breaking else 0]
            elif name == 'scope':
                return self.header.split('(')[1][:-1] if '(' in self.header else None
            else:
                raise AttributeError(f"Attribute '{name}' not found in class Commit")

    def __repr__(self):
        return f"{self.hash[:8]} {self.title})"


def filter_commits(commits, start=None, end=None):
    """
    Returns commits from start (exclusive) to end (inclusive).
    start must occur before end
    start and end can be a tag, or hash
    """

    if start is not None:
        for idx, c in enumerate(commits):
            if c['hash'].startswith(start):
                commits = commits[:idx]
                break

    if end is not None:
        for idx, c in enumerate(commits):
            if c['hash'].startswith(end):
                commits = commits[idx:]
                break

    return commits


def compile_log(commits):
    """
    """

    versions = []

    # iterate through commits from latest to earliest

    # group by version
    for commit in commits:
        # make a new version if required
        if len(versions) == 0:
            versions.append([])

        this_commit = Commit(commit)

        # append to current version
        versions[-1].append(this_commit)

    # for version in versions:
    #     print(version)

    return versions


def format_log(versions):
    output = "# Changelog\n\n"

    for version in versions:
        for commit in version:
            scope = f"{commit.scope} - " if commit.scope else ''
            desc = commit.description
            desc = desc if len(scope) == 0 else desc
            output += f"* {scope}{desc}\n"

        # add following newline
        output += "\n"

    return output


def write_log(log, filename):
    with open(filename, 'w') as f:
        f.write(log)
