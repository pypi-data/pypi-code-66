from configparser import ConfigParser
import pexpect
import sys
import os
import os.path
import unicodedata
import logging
import re
import socket
import time
import platform


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="Cc")


def check_server_args(*args):
    if len(args) != 2:
        print("Usage: server(dirname, language [, doFork = True, messages = False)])")
        return False
    if not os.path.isdir(args[0]):
        print("The directory " + args[0] + " doesn't exist")
        return False
    if not args[1] in ['R' , 'julia', 'matlab', 'python']:
        print("Language has to be R, julia, matlab, or python")
        return False
    return True


def check_client_args(*args):
    if len(args) != 3:
        print("Usage: client(dirname, language, inputfile)")
        return False
    if not os.path.isdir(args[0]):
        print("The directory " + args[0] + " doesn't exist")
        return False
    if not args[1] in ['R' , 'julia', 'matlab', 'python']:
        print("Language has to be R, julia, matlab, or python")
        return False
    if (args[2] == 'QUIT'):
        return True
    if args[2].startswith("```"):
        return True
    if not os.path.isfile(args[2]):
        print("The input file " + args[2] + " doesn't exist")
        return False
    return True


def read_config(dirname, lang):
    configname = dirname + "/" + lang + ".config"
    if os.path.isfile(configname):
        config_object = ConfigParser()
        config_object.read(configname)
        return config_object["SERVERCONFIG"]
    else:
        print("Config file " + configname + " not found")
        return False


def server(*args, doFork = True, messages = False): # dirname, lang
    if platform.system() == 'Windows':
        print("On Windows 10 the talk2stat server has to run using a Linux subsystem (see documentation).")
        return False
    if not check_server_args(*args):
        return False
    dirname = args[0]
    lang = args[1]
    serverinfo = read_config(dirname, lang)
    if serverinfo == False:
        return False
    if doFork:
        # Fork, and exit the parent process. The child will continue to run
        pid = os.fork()
        if pid:
            sys.exit(0)
        print("pid {}".format(os.getpid()), file=open(dirname + '/serverPID' + lang + '.txt', 'w'))
    os.environ["TERM"] = "dumb" # needed for julia
    original_stdout = sys.stdout
    if lang == 'R':
        promptchar = '> '
        exe = 'R --vanilla --interactive -q'
        runfile = 'source'
    if lang == 'matlab':
        promptchar = '>>'
        exe = 'matlab -nodisplay -nosplash -nodesktop -nojvm'
        runfile = 'run'
    if lang == 'julia':
        promptchar = 'julia>'
#        exe = 'julia -q --color=no --banner=no --inline=no'
        exe = 'julia -q --color=no --banner=no'
        runfile = 'include'
    if lang == 'python':
        promptchar = '>>> '
        exe = 'python3'
        runfile = 'run' # not a native python function! defined below!
    # set up a bi-directional pipe to interact with the interpreter (e.g. julia)
    child = pexpect.spawn(exe)
    fout = open(dirname + '/' + serverinfo["DEBUGFILE"],'ab')
    child.logfile = fout
    child.setecho(False)
    child.expect(promptchar, timeout=60)
    if lang == 'python':
        child.sendline('run = lambda filename : exec(open(filename).read())') 
        child.expect(promptchar.rstrip("\n"), timeout=60)
    if lang == 'R':
        promptchar = '>>> '
        child.sendline('options(prompt = ">>> ")')
        child.expect(promptchar.rstrip("\n"), timeout=60)
    print(lang + ": Ready")
    print("Listening to port: " + serverinfo["PORT"])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        runbool = True
        s.bind(('127.0.0.1', int(serverinfo["PORT"])))
        s.listen()
        while runbool: 
            conn, addr = s.accept()
            with conn:
                current_time = time.strftime("%Y/%M/%D %H:%M:%S", time.localtime())
                fout.write(f'\n------ {current_time} ------\n'.encode())
                #fout.write(f'Connected by: {addr}\n'.encode())
                if messages == True:
                    print(f'Connected by: {addr}')
                buffer = []
                while True:
                    # user_input is a source file name
                    user_input = conn.recv(1024*1024).decode().rstrip('\n')
                    if messages == True:
                        print(user_input)
                    if not user_input:
                        break
                    if user_input.endswith("QUIT"):
                        conn.sendall('END'.encode())
                        runbool = False
                        break
                    if user_input.startswith("```"):
                        child.sendline(user_input.lstrip("```").rstrip("```"))
                    else:
                        child.sendline(runfile + '("' + user_input +'")')
                    try: 
                        child.expect(promptchar.rstrip("\n"), timeout=int(serverinfo["PIPETIMEOUT"]))
                    except pexpect.TIMEOUT:
                        fout.write(f'\nTimed out {current_time} ------\n'.encode())
                    buffer.append(remove_control_characters(str(child.before, "utf-8")))
                    buffer.append("\nEND")
                    if messages == True:
                        print(''.join(buffer))
                    conn.sendall(''.join(buffer).encode())
                current_time = time.strftime("%Y/%M/%D %H:%M:%S", time.localtime())
                fout.write(f'\n====== {current_time} ======\n'.encode())

    fout.close()
    child.close()
    return True


def client(*args): # dirname, lang, filename
    if not check_client_args(*args):
        return False
    dirname = args[0]
    lang = args[1]
    filename = args[2]
    serverinfo = read_config(dirname, lang)
    if serverinfo == False:
        return False
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('127.0.0.1', int(serverinfo["PORT"])))
        except ConnectionRefusedError:
            print('Connection refused. Is server running?')
            return False
        s.sendall(filename.rstrip().encode())
        resp = ""
        while not resp.rstrip().endswith("END"):
            resp = resp + s.recv(1024*1024).decode()
        print(resp.rstrip("END\n"))
    return True


__all__ = ("client", "server",)
