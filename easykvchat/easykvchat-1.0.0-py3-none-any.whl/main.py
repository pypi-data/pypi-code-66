from easykvchat.server.app import ServerApp
from easykvchat.client.app import ClientApp

import sys
import os


class InvalidArguments(ValueError):
    pass


def run(argv):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    try:
        if len(argv) < 2:
            raise InvalidArguments()

        mode = argv[1]
        if mode == "server":
            if len(argv) != 3:
                raise InvalidArguments()

            port = int(argv[2])
            if port < 0 or port > 65535:
                raise InvalidArguments()

            ServerApp(port).run()
        elif mode == "client":
            ClientApp().run()
        else:
            raise InvalidArguments()
    except InvalidArguments as err:
        print("Syntaxe : <mode: client|server> [port (mode serveur uniquement)]")
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv))
