CLI_CONFIG = {
    "format_plugin": {"options": ["-p"]},
    "output": {"source": "rend", "default": None,},
    "add_sub": {"nargs": "*"},
    "sub": {"positional": True, "nargs": "?",},
}
CONFIG = {
    "add_sub": {"help": "Add a sub to the hub", "default": [],},
    "sub": {"type": str, "help": "The sub on the hub to parse", "default": None,},
}
SUBCOMMANDS = {}
DYNE = {
    "tree": ["tree"],
}
