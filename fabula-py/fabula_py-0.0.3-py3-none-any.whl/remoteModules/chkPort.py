'''
Created on 9 окт. 2020 г.

@author: ladmin
'''
import sys
import socket
import argparse
import os
from contextlib import closing

def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")

def module_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return os.path.dirname((sys.executable, encoding))
    return os.path.dirname((__file__, encoding))

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--host', default='127.0.0.1')
    parser.add_argument ('--port', default='80')
    return parser

def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            #print('{host} {port} exist'.format(host=host, port=port))
            sys.exit(0)
        else:
            #print('{host} {port} unexist'.format(host=host, port=port))
            sys.exit(1)
            

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args() 
    kwargs={'host':namespace.host, "port":int(namespace.port)}
    check_socket(**kwargs)