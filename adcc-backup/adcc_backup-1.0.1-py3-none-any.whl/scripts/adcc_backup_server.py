from time import sleep
import argparse
from adcc_backup import Configuration

from adcc_backup import AutoBagFixer, ManualBagFixer


def adcc_backup_server_main():
    parser = argparse.ArgumentParser(description=f"Adcc Server Backup")
    parser.add_argument('-nw', '--no_watcher', action='store_true', default=False,
                        help='Start the bag fixer without the watcher.')
    args = parser.parse_args()

    print('adcc_backup_server')
    cfg = Configuration('default')
    if cfg.loaded:

        if args.no_watcher:
            manual_fixer = ManualBagFixer(cfg)
            manual_fixer.start()
        else:
            auto_fixer = AutoBagFixer(cfg)
            auto_fixer.start()

            while True:
                auto_fixer.log.debug(f'Adcc server backup {auto_fixer.green("Alive")}')
                sleep(30)
