import os
import sys

from threading import Thread, Event
import subprocess


class Process(Thread):
    """
    Subprocess manager. Consumes output asynchronously so it can be monitored and reported.
    It is capable of running synchronously and of killing that process even when async.
    """

    def __init__(self, cmd_args, env=os.environ.copy(), out=sys.stdout, buffered=True):
        """
        Note: in buffered mode, commands like `watch` don't work well.
        """
        Thread.__init__(self)
        self._cmd_args = cmd_args
        self._env = env
        self._buffered = buffered
        self._kill = Event()

    def kill(self):
        """
        Abort process gracefully.
        """
        self._kill.set()

    @property
    def returncode(self):
        """
        Query return code.
        """
        return self._ps.returncode

    def run(self):
        """
        If called directly acts as a blocking call to the process.

        Use start() and join() instead to execute asynchronously.
        """
        self._ps = subprocess.Popen(
            self._cmd_args, stdout=subprocess.PIPE, env=self._env
        )
        self._consume_output(self._ps)

    def _consume_output(self, process, outstream=sys.stdout):
        """
        Consumes stdout output from the process and feeds it to the output stream.
        """
        buf = ""
        char = b""
        while process.poll() is None or char:
            if self._kill.is_set():
                process.terminate()
                break
            char = process.stdout.read(1).decode("utf-8")  # read 1 byte
            if char:
                buf += char
                if not self._buffered or char == os.linesep:
                    if outstream is not None:
                        outstream.write(buf)
                        outstream.flush()
                    buf = ""

        process.stdout.close()
