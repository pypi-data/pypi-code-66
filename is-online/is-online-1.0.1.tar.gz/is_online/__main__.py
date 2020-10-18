import socket
import argparse


def is_online(host="1.1.1.1", port=53, timeout=3):
    '''
    Cli tool which tells you if you are online or not.
    '''
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False


def main():

    parser = argparse.ArgumentParser(
        description='''Checks with host, and returns true if reachable, false if not.''')
    parser.add_argument('-p', '--port', type=int, default=53, help='The Port to connect to')
    parser.add_argument('-o', '--host', type=str, default='1.1.1.1', help='The IP host to connect to')
    parser.add_argument('-t', '--timeout', type=int, default=3, help='Timeout in seconds')
    args = parser.parse_args()
    res = is_online(args.host, args.port, args.timeout)
    print("You are Online!" if res else "You are Offline!")


if __name__ == "__main__":
    main()
