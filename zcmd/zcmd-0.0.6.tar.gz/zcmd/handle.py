# Stdlib
import sys
import pexpect
DEFAULT_ENCODING = "utf-8"
class ProcessHandler(object):
    read_timeout = 0.05
    terminate_timeout = 0.2
    logfile = None
    _sh = None
    @property
    def sh(self):
        if self._sh is None:        
            self._sh = pexpect.which('sh')
            if self._sh is None:
                raise OSError('"sh" shell not found')
        
        return self._sh

    def __init__(self, logfile=None, read_timeout=None, terminate_timeout=None):
        """Arguments are used for pexpect calls."""
        self.read_timeout = (ProcessHandler.read_timeout if read_timeout is
                             None else read_timeout)
        self.terminate_timeout = (ProcessHandler.terminate_timeout if
                                  terminate_timeout is None else
                                  terminate_timeout)
        self.logfile = sys.stdout if logfile is None else logfile
    def getoutput(self, cmd):
        try:
            return pexpect.run(self.sh, args=['-c', cmd]).replace('\r\n', '\n')
        except KeyboardInterrupt:
            print('^C', file=sys.stderr, end='')

    def getoutput_pexpect(self, cmd):
        try:
            return pexpect.run(self.sh, args=['-c', cmd]).replace('\r\n', '\n')
        except KeyboardInterrupt:
            print('^C', file=sys.stderr, end='')
    def system(self, cmd ,output = False , handle = None):
        enc = DEFAULT_ENCODING
        patterns = [pexpect.TIMEOUT, pexpect.EOF]
        EOF_index = patterns.index(pexpect.EOF)
        out_size = 0
        out = ''
        try:
            if hasattr(pexpect, 'spawnb'):
                child = pexpect.spawnb(self.sh, args=['-c', cmd]) # Pexpect-U
            else:
                child = pexpect.spawn(self.sh, args=['-c', cmd])  # Vanilla Pexpect
            if handle:handle(child)
            flush = sys.stdout.flush
            while True:
                res_idx = child.expect_list(patterns, self.read_timeout)
                line = child.before[out_size:].decode(enc, 'replace')
                if output:out += line
                print(line, end='')
                flush()
                if res_idx==EOF_index:break
                out_size = len(child.before)
        except KeyboardInterrupt:
            child.sendline(chr(3))
            try:
                out_size = len(child.before)
                child.expect_list(patterns, self.terminate_timeout)
                line = child.before[out_size:].decode(enc, 'replace')
                if output:out += line
                print(line, end='')
                sys.stdout.flush()
            except KeyboardInterrupt:
                pass
            finally:
                child.terminate(force=True)
        child.isalive()
        if child.exitstatus is None:
            if child.signalstatus is None:
                return 0 , out
            return -child.signalstatus , out
        if child.exitstatus > 128:
            return -(child.exitstatus - 128) ,out
        return child.exitstatus , out
system = ProcessHandler().system