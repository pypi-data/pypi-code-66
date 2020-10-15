#!/usr/bin/python

from ansible.module_utils.basic import *
from shutil import copyfile
import glob


def main():
    module = AnsibleModule(argument_spec=dict(
        src=dict(type='str', required=True),
        dest=dict(type='str', required=True),
        remove_from_dest=dict(type='str', required=True)
    ))

    changed = False

    previousfile = module.params["dest"] + "/" + module.params["remove_from_dest"]
    for file in glob.glob(previousfile):
        changed = True
        os.remove(file)

    for file in glob.glob(module.params["src"]):
        changed = True
        copyfile(file, module.params["dest"])

    module.exit_json(changed=changed)


if __name__ == '__main__':
    main()
