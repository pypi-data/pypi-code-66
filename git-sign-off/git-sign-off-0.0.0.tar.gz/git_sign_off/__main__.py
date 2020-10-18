import argparse

from .Process import Process
from .sign_off import SignOff, run_sign_off_challenge


def main_sign():
    """
    Runs the given command as a challenge.
    If it runs successfully a sign off signature is added to the
    git project, with a fingerprint pointing to the before-the-latest commit.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", default="default")
    parser.add_argument("-c", "--cmd", nargs="+", required=True)
    args = parser.parse_args()

    run_sign_off_challenge(args.cmd)

    sign_off = SignOff(args.name)
    sign_off.write_signature()


def main_check():
    """
    Checks the signature for a task. By default task is named 'default'.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", default="default")
    args = parser.parse_args()

    sign_off = SignOff(args.name)
    sign_off.check_signature()


if __name__ == "__main__":
    print("Usage: Call programs `git-sign-off` and `git-sign-off-check` directly.")
