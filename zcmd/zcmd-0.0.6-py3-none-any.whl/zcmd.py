from .handle import system
import threading,time
time_sleep = 0.5
s_cd = "cd "
s_cp_dir = "cp -r "
s_cp_file = "cp "
s_space = ""
s_conn = " && "
s_nextline = "\n"
class ZCmd():
    def __init__(self):
        self.cmd = None
    def conn(self , cmd1, cmd2):
        return cmd1 + s_conn + cmd2
    def run(self , cmd ,  b_input = False ,b_output = False , b_print = True):
        if self.cmd:cmd = self.conn(self.cmd , cmd)
        handle = b_input and self.handle or None
        _,out = system(cmd , b_print, handle)
        if b_output:return out.split(s_nextline)
    def cd(self ,cmd):
        cmd = cmd.strip()
        if not cmd.startswith(s_cd):cmd = s_cd + cmd
        _,out = system(cmd , True)
        if out == s_space:self.cmd = cmd
    def t_input(self , child):
        time.sleep(time_sleep)
        while child.isalive():
            line = input()
            if child.isalive():
                child.sendline(line)
            time.sleep(time_sleep)
    def handle(self , child):
        task = threading.Thread(target=self.t_input, args=(child,))
        task.start()
def setSleepTime(sleep_time):
    time_sleep = sleep_time
zcmd = ZCmd()
run = zcmd.run
cd = zcmd.cd
