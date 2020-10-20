from adcc_backup import PKG_CFG_FOLDER
from adcc_backup import AdccLogger

from markipy.basic import Yaml, Host

_configuration_ = {'class': 'Configuration', 'version': 1}


class AttemptingToReadConfigurationNotLoadedProperly(Exception):
    def __init__(self, log):
        log.error('Attempting To Read Configuration Not Loaded Properly.')


class IncorrectRemoteInLink(Exception):
    def __init__(self, log, link):
        log.error(f'Incorrect remote in link: {link["name"]}')


class ClientMissingFromConfiguration(Exception):
    def __init__(self, log, link):
        log.error(f'Missing "Client" form the configuration.')


class ServerMissingFromConfiguration(Exception):
    def __init__(self, log, link):
        log.error(f'Missing "Server" form the configuration.')


def _get_host_link(host, link, remote, mode):
    if mode == 'src':
        return Host(user=host['user'], ip=host['ip'], path=link['source_path'], remote=remote)
    else:
        return Host(user=host['user'], ip=host['ip'], path=link['destination_path'], remote=remote)


def _convert_host(host):
    return Host(user=host['user'], ip=host['ip'])


def _convert_hosts(hosts):
    h = {}
    for host in hosts:
        h.update({host['name']: host})
    return h


class Configuration(AdccLogger):
    def __init__(self, cfg_name):
        AdccLogger.__init__(self, console=True, file_log='Configuration')
        self._init_atom_register_class(_configuration_)
        self.cfg_file = Yaml(PKG_CFG_FOLDER.__folder__ / cfg_name)
        self.cfg = self.cfg_file.load()
        if self.cfg is None:
            # Start Wizard
            self.log.debug(f'Configuration was not found.')
            self.cfg_file.write(YAML_BASE_CFG)
            self.log.debug(f'New cfg file: {self.cfg_file}. {self.red("Please modify it for your needs!.")}')
            self.loaded = False
        else:
            self.loaded = True
            self.hosts = _convert_hosts(self.cfg['Hosts'])
            self.links = self.cfg['Links']

    def __call__(self):
        if self.loaded:
            return self.cfg
        else:
            raise AttemptingToReadConfigurationNotLoadedProperly(self.log)

    def _get_src_dst(self, link):
        if link['remote'] == 'source':
            src_flag, dst_flag = True, False
        elif link['remote'] == 'destination':
            src_flag, dst_flag = False, True
        else:
            raise IncorrectRemoteInLink(self.log, link)

        src = _get_host_link(self.hosts[link['source']], link, remote=src_flag, mode='src')
        dst = _get_host_link(self.hosts[link['destination']], link, remote=dst_flag, mode='dst')
        return src, dst

    def get_eth_client(self):
        if 'Client' not in self.cfg.keys():
            raise ClientMissingFromConfiguration(self.log)
        return self.cfg['Client']['eth']

    def get_server_path(self):
        if 'Server' not in self.cfg.keys():
            raise ServerMissingFromConfiguration(self.log)
        return self.cfg['Server']['watch_path'], self.cfg['Server']['fixed_path']


YAML_BASE_CFG = f'''

Hosts:
-
    name:
    ip:
    user:
    ssh_port: 22
-
    name:
    ip:
    user:
    ssh_port: 22
    
Links:
-   
    enable: True
    name:
    
    remote: destination
    source:
    destination:
    
    source_path: 
    destination_path: 
    delete: False

Client:
    eth: 

Server:
    watch_path: 
    fixed_path:
'''
