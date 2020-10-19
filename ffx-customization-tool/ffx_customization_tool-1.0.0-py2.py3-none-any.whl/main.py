#!/usr/bin/env python

from simple_term_menu import TerminalMenu
from terminaltables import AsciiTable

from ffx.monsters.models import Monsters
from ffx.common.loaders import LoaderFactory


class Customizations:

    def __init__(self, item_type):
        self.item_type = item_type.lower()

    def all(self):
        loader = getattr(LoaderFactory, self.item_type)()
        items = loader.load()
        valid_items = self.__remove_items_without_requirements(items)
        reformas = self.__get_reformas_from(valid_items)
        return reformas

    def __get_reformas_from(self, valid_items):
        return [(
            item['ability'],
            self.__remove_quantity_from(item['requirement'])
        ) for item in valid_items]

    def __remove_items_without_requirements(self, items):
        return filter(lambda x: not x['requirement'].startswith('N/A'), items)

    def __remove_quantity_from(self, requirement):
        return " ".join(requirement.split(" ")[:-1])


def select_item_type():
    item_types = ["Armors", "Weapons"]
    menu = TerminalMenu(item_types)
    type_entry = menu.show()

    return item_types[type_entry]


def select_customization(customizations):
    all_customizations = customizations.all()
    names = map(lambda x: x[0], all_customizations)
    menu = TerminalMenu(names)
    entry = menu.show()
    selected_customization = all_customizations[entry]
    return selected_customization


def find_monsters(requirement):
    loader = LoaderFactory.monsters()
    raw_data = loader.load()
    monsters = Monsters(raw_data)
    monsters.find_sources(requirement)

    return monsters


def build_table(ability, requirement, monsters, type_entry):
    data = []
    headers = ["Ability", "Material", "Sources"]
    data.append(headers)
    data.append([ability, requirement, monsters])

    return AsciiTable(data, type_entry).table


def main():
    type_entry = select_item_type()

    customizations = Customizations(type_entry)
    ability, requirement = select_customization(customizations)

    monsters = find_monsters(requirement)

    table = build_table(ability, requirement, monsters, type_entry)

    print(table)


if __name__ == "__main__":
    main()
