#!/usr/bin/env python3

import argparse
import threading
import time
import sys
from mfutil.cli import MFProgress
from mfutil.bash_wrapper import BashWrapper
import rich
from rich.panel import Panel

DESCRIPTION = "execute a command with a nice progressbar"


def thread_advance(progress, tid, timeout):
    i = 1
    while i < timeout:
        progress.update(tid, advance=1)
        time.sleep(1)
        i = i + 1


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("COMMAND", help="command to execute")
    parser.add_argument("COMMAND_ARG", nargs='*',
                        help="command arg")
    parser.add_argument("--timeout",
                        help="timeout (in seconds)", type=int,
                        default=180)
    parser.add_argument("--silent", action="store_true",
                        help="if set, we don't add a debug output in case of "
                        "errors")
    args = parser.parse_args()

    cmd = " ".join([args.COMMAND] + args.COMMAND_ARG)
    if args.timeout == 0:
        command = cmd
    else:
        command = "timeout --kill-after=3 %is %s" % (args.timeout, cmd)

    status = True
    timeout = False
    with MFProgress() as progress:
        t = progress.add_task("FIXME...", total=args.timeout)
        x = threading.Thread(target=thread_advance, args=(progress, t,
                                                          args.timeout),
                             daemon=True)
        x.start()
        bw = BashWrapper(command)
        if bw:
            progress.complete_task(t)
        else:
            if bw.code == 124 or bw.code == 137:
                # timeout
                progress.complete_task_nok(t, "timeout")
                timeout = True
            else:
                progress.complete_task_nok(t, "bad exit code")
            status = False
    if not status:
        if not args.silent and not timeout:
            rich.print(Panel("[bold]Error details:[/bold]\n%s" %  # noqa: E999
                             str(bw)))
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
