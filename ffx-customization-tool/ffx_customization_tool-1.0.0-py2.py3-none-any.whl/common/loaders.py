from pathlib import Path

from ttp import ttp


ROOT_PATH = Path(__file__).resolve().parent.parent.parent
DATA_PATH = f"{ROOT_PATH}/ffx/data"

MONSTERS_PATH = f"{DATA_PATH}/monsters/monsters.txt"
MONSTERS_TEMPLATE_PATH = f"{DATA_PATH}/monsters/template.txt"

WEAPONS_PATH = f"{DATA_PATH}/items/weapons.txt"
ARMORS_PATH = f"{DATA_PATH}/items/armors.txt"
ITEM_TEMPLATE_PATH = f"{DATA_PATH}/items/template.txt"


class Parser:

    def __init__(self, path):
        self.path = path

    def parse(self, items):
        with open(self.path) as template_file:
            template = template_file.read()
        parser = ttp(items, template)
        parser.parse()
        return parser.result()


class Reader:

    def __init__(self, parser, path):
        self.parser = parser
        self.path = path

    def read(self, field):
        with open(self.path) as descriptor:
            data = descriptor.read()
        result = self.parser.parse(data)
        items = result[0][0][field]
        return items


class Loader:

    def __init__(self, template_path, path, field):
        self.template_path = template_path
        self.field = field
        self.path = path

    def load(self):
        parser = Parser(self.template_path)
        reader = Reader(parser, self.path)
        items = reader.read(self.field)
        return items


class LoaderFactory:

    @staticmethod
    def monsters():
        return Loader(MONSTERS_TEMPLATE_PATH, MONSTERS_PATH, 'monster')

    @staticmethod
    def weapons():
        return Loader(ITEM_TEMPLATE_PATH, WEAPONS_PATH, 'item')

    @staticmethod
    def armors():
        return Loader(ITEM_TEMPLATE_PATH, ARMORS_PATH, 'item')
