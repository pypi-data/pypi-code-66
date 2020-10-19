"""
example = {
    "customization": "Auto Phoenix",
    "material": {
        "name": "MegaPhoenix",
        "quantity": 30
    },
    "sources": [{
        "fiend": "Defender X",
        "location": "Zanarkand",
        "mode": {
            "theft": "Phoenix (common), MegaPhoenix (rare)",
            "drop": "Phoenix x2 (common), MegaPhoenix x2 (rare)",
            "bribery": "MegaPhoenix x2 for 1,600,000",
        },
    }]
}
"""


class Sources:

    def __init__(self, name):
        self.name = name
        self.sources = []
        self.monster = None
        self.modes = None

    def __iter__(self):
        for source in self.sources:
            yield source

    def add(self, monster):
        self.monster = monster
        self.__get_modes()
        self.__add_sources()

    def __get_modes(self):
        fields = ["steal", "bribe", "drop"]
        modes = []
        for field in fields:
            if self.name in self.monster[field]:
                modes.append((field, self.monster[field]))
        self.modes = modes

    def __add_sources(self):
        if len(self.modes) != 0:
            source = {
                "name": self.monster['name'],
                "location": self.monster['location'],
                "modes": self.modes
            }
            self.sources.append(source)


class Monsters:

    def __init__(self, monsters):
        self.monsters = monsters
        self.sources = None

    def find_sources(self, name):
        sources = Sources(name)
        for monster in self.monsters:
            sources.add(monster)
        self.sources = sources

    def __repr__(self):
        string = []
        for monster in self.sources:
            name = monster['name']
            location = monster['location']
            modes = monster['modes']
            string.append(f"{name} -> {location}:")
            for mode in modes:
                string.append(f"    {mode[0]}: {mode[1]}")
        return "\n".join(string)
