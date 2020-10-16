import os
import subprocess
from pyngrok import ngrok

try:
    from google.colab import drive

    colab_env = True
except ImportError:
    colab_env = False



class ColabJupyter:
    def __init__(self, port=10000, password=None, mount_drive=False):
        self.port = port
        self.password = password
        self._mount = mount_drive
        self._install_code()
        self._start_server()
        self._run_code()

    def _install_code(self):
        subprocess.run(
            ["pip3 install", "jupyterlab"], stdout=subprocess.PIPE
        )
    def _start_server(self):
        active_tunnels = ngrok.get_tunnels()
        for tunnel in active_tunnels:
            public_url = tunnel.public_url
            ngrok.disconnect(public_url)
        url = ngrok.connect(port=self.port, options={"bind_tls": True})
        print(f"Code Server can be accessed on: {url}")

    def _run_code(self):
        os.system(f"fuser -n tcp -k {self.port}")
        if self._mount and colab_env:
            drive.mount("/content/drive")
        if self.password:
            code_cmd = f"jupyter lab --port {self.port}"
        else:
            code_cmd = f"jupyter lab --port {self.port}"
        with subprocess.Popen(
            [code_cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
        ) as proc:
            for line in proc.stdout:
                print(line, end="")
