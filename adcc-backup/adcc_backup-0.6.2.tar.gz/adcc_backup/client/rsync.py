from markipy.basic import Rsync, Host
from markipy.basic import Terminator
from markipy.basic import Performance

from adcc_backup import PKG_LOG_FOLDER

_adcc_rsync_ = {'class': 'AdccRsync', 'version': 1}


class IncorrectRemoteInLink(Exception):
    def __init__(self, log, link):
        log.error(f'Incorrect remote in link: {link["name"]}')


def _get_host(host, link, remote, mode):
    if mode == 'src':
        return Host(user=host['user'], ip=host['ip'], path=link['source_path'], remote=remote)
    else:
        return Host(user=host['user'], ip=host['ip'], path=link['destination_path'], remote=remote)


def _convert_hosts(hosts):
    h = {}
    for host in hosts:
        h.update({host['name']: host})
    return h


class AdccRsync(Rsync):
    def __init__(self, cfg, console=True, use_term=False):
        Rsync.__init__(self, file_log='AdccRsync', console=console, log_path=PKG_LOG_FOLDER())
        self._init_atom_register_class(_adcc_rsync_)
        self.hosts = _convert_hosts(cfg()['Hosts'])
        self.links = cfg()['Links']
        self.term = Terminator(console=console) if use_term else None

    @Performance.collect
    def upload(self):
        for link in self.links:
            self.upload_link(link)

    @Performance.collect
    def check(self):
        for link in self.links:
            self.check_link(link)

    @Performance.collect
    def upload_link(self, link):
        src, dst = self._get_src_dst(link)
        self.update_hosts(src, dst)
        if self.term:
            self.term.run_process(self.get_upload_cmd())
        else:
            self.async_upload()

    @Performance.collect
    def check_link(self, link):
        src, dst = self._get_src_dst(link)
        self.update_hosts(src, dst)
        if self.term:
            self.term.run_process(self.get_check_cmd())
        else:
            self.async_check()

    def _get_src_dst(self, link):
        if link['remote'] == 'source':
            src_flag, dst_flag = True, False
        elif link['remote'] == 'destination':
            src_flag, dst_flag = False, True
        else:
            raise IncorrectRemoteInLink(self.log, link)

        src = _get_host(self.hosts[link['source']], link, remote=src_flag, mode='src')
        dst = _get_host(self.hosts[link['destination']], link, remote=dst_flag, mode='dst')
        return src, dst
