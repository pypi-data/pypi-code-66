import os
import sys
import argparse
import subprocess
from pathlib import Path

from markipy.basic import Process, Folder, File
from markipy.basic import Performance

import adcc_backup as adcc
from adcc_backup import PKG_LOG_FOLDER
from adcc_backup import Configuration

ADCC_PKG_DEFAULT_INSTALLED_PATH = Folder(File(adcc.__file__)().parent)
ADCC_SCRIPTS_PATH = ADCC_PKG_DEFAULT_INSTALLED_PATH() / 'scripts'

_copy_ssh_key_ = {'class': 'Process', 'version': 4}
_install_service_ = {'class': 'InstallServerService', 'version': 1}


class CopySshKey(Process):
    def __init__(self, cfg):
        Process.__init__(self, file_log='CopySSHkey', console=False, log_path=PKG_LOG_FOLDER())
        self._init_atom_register_class(_copy_ssh_key_)
        self.cfg = cfg

    @Performance.collect
    def start(self):
        for host_name, host_info in self.cfg.hosts.items():
            self.log.debug(f"Processing: {self.lightblue(host_name)}")
            key = Path().home() / '.ssh' / 'id_rsa.pub'
            if not key.exists():
                self.log.debug('No ssh key founded. Starting process to create one.')
                self.execute(['ssh-keygen'])
            if key.exists():
                self.log.debug('Ssh key found.')
                self.execute(['ssh-copy-id', f"{host_info['user']}@{host_info['ip']}"])


def make_new_service_file(desc, user, executable):
    return f'''
[Unit]
      Description={desc}
[Service]
      Type=simple
      User={user}
      ExecStart={executable}
[Install]
      WantedBy=multi-user.target
'''


class InstallService(Process):
    def __init__(self, user, script, script_path, desc):
        Process.__init__(self, file_log=script, console=True, log_path=PKG_LOG_FOLDER())
        self.user = user
        self.script_name = script
        self.script_path = script_path
        self.desc = desc
        self._init_atom_register_class(_install_service_)

    @Performance.collect
    def start(self):
        service = f'/etc/systemd/system/{self.script_name}.service'
        self.log.debug(f'Creating new service -> {self.green(service)}')
        service = File(service)
        service.write(make_new_service_file(self.desc, self.user, self.script_path))
        self.log.debug(f'Service * {service} -> {self.green("Enable")}')
        subprocess.call(['systemctl', 'enable', self.script_name])
        self.log.debug(f'Service * {service} -> {self.green("Started")}')
        subprocess.call(['service', self.script_name, 'start'])


def adcc_backup_utils_main():
    parser = argparse.ArgumentParser(description=f"Adcc Backup Utils")
    parser.add_argument('-ks', '--ssh-key', action='store_true', default=False,
                        help='Copy the ssh key for all the Host in the CFG in ~/.adcc_backup.')
    parser.add_argument('-is', '--install-server-service', action='store_true', default=False,
                        help='Install adcc_backup_server as service. Pass the user as argument')
    parser.add_argument('-ic', '--install-client-service', action='store_true', default=False,
                        help='Install adcc_backup_client as service. Pass the user as argument')
    # Internal Usage
    parser.add_argument('--script-path', type=str, default='Null',
                        help='Internal usage. Do not use it !')
    parser.add_argument('--user', type=str, default='Null',
                        help='Internal usage. Do not use it !')

    args = parser.parse_args()

    cfg = Configuration('default')

    # Install ssh-key in Hosts
    if args.ssh_key:
        if cfg.loaded:
            copyssh = CopySshKey(cfg)
            copyssh.start()

    # Install adcc_backup_server as service
    if args.install_server_service:
        if os.geteuid() == 0:
            # Root
            install_service = InstallService(args.user, 'adcc_backup_server', args.script_path,
                                             'Adcc Backup Server Service')
            install_service.start()
        else:
            # Not Root
            script_path = subprocess.check_output(['which', 'adcc_backup_server']).decode().strip()
            user = subprocess.check_output(['id', '-u', '-n']).decode().strip()
            subprocess.call(['sudo', 'python3.8', *sys.argv, '--script-path', script_path, '--user', user])
            # Calling again same script as root
            sys.exit()

    # Install adcc_backup_client as service
    if args.install_client_service:
        if os.geteuid() == 0:
            # Root
            install_service = InstallService(args.user, 'adcc_backup_client', args.script_path,
                                             'Adcc Backup Client Service')
            install_service.start()
        else:
            # Not Root
            script_path = subprocess.check_output(['which', 'adcc_backup_client']).decode().strip()
            user = subprocess.check_output(['id', '-u', '-n']).decode().strip()
            subprocess.call(['sudo', 'python3.8', *sys.argv, '--script-path', script_path, '--user', user])
            # Calling again same script as root
            sys.exit()
