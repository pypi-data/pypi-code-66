import os
import sys

from .utils import error
from .Process import Process
from . import exceptions
from .Git import Git

NO_VERIFY = "NO_VERIFY"


def run_sign_off_challenge(cmd):
    """
    Runs a command and declares the environment variable _GIT_DIR_ pointing to the repo root.
    """
    env = os.environ.copy()
    env["_GIT_DIR_"] = Git().root
    p = Process(cmd, env=env)
    try:
        p.run()
    except Exception as e:
        error(e)
    if not p.returncode == 0:
        error(Exception("git-sign-off challenge failed. Aborting sign-off."))


def check_trivial_fs_name(name):
    """
    Check that the name is trivial, so it can be stored easily on the filesystem.
    Throws a ValueError if it's not.
    """
    char_ok_filter = lambda c: c.isalpha() or c.isdigit() or c in [".", "-", "_"]
    invalid_chars = [char for char in name if not char_ok_filter(char)]
    if any(invalid_chars):
        raise ValueError(
            f"Found invalid characters {invalid_chars} in task name '{name}'."
        )


class SignOff:
    def __init__(
        self,
        task_name="main",
    ):
        self._git = Git()
        self._root = self._git.root / ".git-sign-off-task-certificates"
        os.makedirs(self._root, exist_ok=True)

        check_trivial_fs_name(task_name)
        self._task_name = task_name

        self._signature_filepath = self._root / f"{task_name}__signature"

    def gen_signature(self, rev="HEAD"):
        """
        Generates a signature
        """
        try:
            return self._git.get_commit_hash(rev)
        except subprocess.CalledProcessError:
            error(
                exceptions.GitError(
                    "Is this a git repo? Need more than 1 commit to generate a signature."
                )
            )

    def write_signature(self):
        """
        Writes the challenge file with the hash of the latest commit.

        Note: Use only before commit. E.g. when using hooks: in pre-commit hook.
        """
        if self.is_verify_enabled():
            with open(self._signature_filepath, "w") as signature:
                msg = self.gen_signature()
                signature.write(msg)
            self._git.add(self._signature_filepath)
            print(f"Added git-sign-off signature for task '{self._task_name}'.")
        else:
            print("Verification is disabled. Skipping git-sign-off.")

    def check_signature(self):
        """
        Checks that the signature is up-to-date.

        Note: Use only after commit was executed. E.g. when using hooks: in post-commit hook.
        """
        try:
            with open(self._signature_filepath) as signature:
                signature_msg = signature.read()
                ref_msg = self.gen_signature("HEAD^1")
                if ref_msg != signature_msg:
                    error(
                        exceptions.SignatureError(
                            "Outdated signature found."
                            " Latest signature was generated after commit:\n"
                            f"{signature_msg}"
                        )
                    )
                else:
                    print(f"Signature check for task '{self._task_name}' passed.")
        except FileNotFoundError:
            error(
                exceptions.SignatureError(
                    f"No signature found for task '{self._task_name}'."
                )
            )

    def is_verify_enabled(self):
        """
        Useful to skip checks on rebase etc.
        """
        return os.environ.get(NO_VERIFY) not in ("true", "t", "True", "T", "1", 1)
