#!/usr/bin/python

from ansible.module_utils.basic import *


def main():
    module = AnsibleModule(argument_spec=dict(
        state=dict(type='str', required=True)
    ))
    with open("/tmp/progress.log", "a") as file_object:
        # Append 'hello' at the end of file
        file_object.write(module.params["state"] + "\n")
    module.exit_json(changed=True)


if __name__ == '__main__':
    main()
