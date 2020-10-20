from os import makedirs
from shutil import move
from pathlib import Path

from markipy.basic import Watcher, GeneralThread, Folder, Channel
from markipy.ros.bag import fix_bag

from adcc_backup import PKG_LOG_FOLDER

_auto_bag_fixer_ = {'class': 'AutoBagFixer', 'version': 1}
_manual_bag_fixer_ = {'class': 'ManualBagFixer', 'version': 1}
_bag_fixer_ = {'class': 'BagFixer', 'version': 1}


class AutoBagFixer(Watcher):
    def __init__(self, cfg):
        self.watch_path, self.fixed_path = cfg.get_server_path()
        Watcher.__init__(self, path=self.watch_path, console=True, recursive=True, log_path=PKG_LOG_FOLDER())
        self._init_atom_register_class(_auto_bag_fixer_)
        self.fixer_threads = []

    def task_file_modified(self, event):
        pass

    def task_file_moved(self, event):
        self.log.debug(f'File moved from {self.orange(event.src_path)} to {self.green(event.dest_path)}')
        file_in = event.dest_path
        file_out = Path(self.fixed_path) / Path(file_in).relative_to(Path(self.watch_path))
        self.log.debug(f'New destination for {self.orange(file_in)} to {self.green(file_out)}')
        makedirs(Path(file_out).parent, exist_ok=True)
        if '.bag' in str(file_out):
            self.log.debug(f'Bag to fix {self.cyan(file_out)}')
            self.fixer_threads.append(BagFixer(file_in, file_out))
            self.fixer_threads[-1].start()
        else:
            self.log.debug(f'File moved: {self.cyan(file_out)}')
            move(file_in, file_out)

    def __del__(self):
        for thread in self.fixer_threads:
            thread.join()


class ManualBagFixer(Folder):
    def __init__(self, cfg, max_thread=4):
        self.root_path, self.fixed_path = cfg.get_server_path()
        Folder.__init__(self, folder_path=self.root_path, console=True, log_path=PKG_LOG_FOLDER())
        self._init_atom_register_class(_manual_bag_fixer_)
        self.max_threads = max_thread
        self.fixer_thread_queue = Channel(size=max_thread)

    def start(self):
        for root, subdirs, files in self.walk():
            for file in files:
                file_in = Path(root) / file
                file_out = Path(self.fixed_path) / Path(file_in).relative_to(Path(self.root_path))
                self.log.debug(f'New destination for {self.orange(file_in)} to {self.green(file_out)}')
                makedirs(Path(file_out).parent, exist_ok=True)
                if '.bag' in str(file_out):
                    if not self.fixer_thread_queue.is_full():
                        self.log.debug(f'Bag to fix {self.cyan(file_out)}')
                        bag_fixer = BagFixer(file_in, file_out)
                        bag_fixer.start()
                        self.fixer_thread_queue.put(bag_fixer)
                    else:
                        bag_fixer = self.fixer_thread_queue.get()
                        bag_fixer.join()
                else:
                    self.log.debug(f'File moved: {self.cyan(file_out)}')
                    move(file_in, file_out)

    def __del__(self):
        while not self.fixer_thread_queue.is_empty():
            bag_fixer = self.fixer_thread_queue.get()
            bag_fixer.join()


class BagFixer(GeneralThread):
    def __init__(self, input_bag, output_bag, ):
        GeneralThread.__init__(self, task_name='BagFixer', console=True, daemon=True, log_path=PKG_LOG_FOLDER())
        self.input_bag = input_bag
        self.output_bag = output_bag
        self._init_atom_register_class(_bag_fixer_)

    def task(self):
        self.log.debug(
            f'Start BagFixer input_bag:{self.orange(self.input_bag)} output_bag: {self.green(self.output_bag)}')
        fix_bag(self.input_bag, self.output_bag)
