from pathlib import Path
import subprocess


def cmd(args):
    """
    Runs a shell command.
    """
    return subprocess.check_output(args).decode("utf-8")


class Git:
    """
    Basic helper module for git
    """

    def __init__(self):
        self._root = Path(cmd("git rev-parse --show-toplevel".split()).strip())

    def show(self, rev="HEAD", args=[]):
        return cmd(["git", "show", rev] + args)

    def get_commit_hash(self, rev="HEAD"):
        return cmd(["git", "rev-parse", rev]).strip()

    def add(self, filepath):
        cmd(["git", "add", filepath])

    @property
    def root(self):
        return self._root
