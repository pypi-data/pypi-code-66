#!/usr/bin/python

from ansible.module_utils.basic import *
from shutil import copyfile
import glob


def main():
    module = AnsibleModule(argument_spec=dict(
        src=dict(type='str', required=True),
        dest=dict(type='str', required=True)
    ))

    # Ensure backup dir exists
    if not os.path.isdir(module.params["dest"]):
        os.makedirs(module.params["dest"])

    changed = False
    for file in glob.glob(module.params["src"]):
        changed = True
        copyfile(file, module.params["dest"] + "/" + os.path.basename(file))

    module.exit_json(changed=changed)


if __name__ == '__main__':
    main()
