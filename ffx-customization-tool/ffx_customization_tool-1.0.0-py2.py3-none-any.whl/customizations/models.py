"""
example = {
    "Auto Phoenix": {
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
}
"""


class Parser:

    @staticmethod
    def requirement(raw):
        material = raw.split(" ")
        return {
            "name": " ".join(material[:-1]),
            "quantity": material[-1]
        }


class Customization:

    def __init__(self, name, material):
        self.name = name
        self.material = material

    def parse(self):
        pass
