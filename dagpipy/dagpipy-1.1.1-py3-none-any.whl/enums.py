from enum import Enum

__all__ = (
    'ImageOptions'
    'Games'
)


class ImageOptions(Enum):
    pixel =             "pixel/"
    colours =           "colors/"
    colors =            "colors/"
    wanted =            "wanted/"
    triggered =         "triggered/"
    wasted =            "wasted/"
    five_guys_one_girl = "5g1g/"
    whyareyougay =      "whyareyougay/"
    invert =            "invert/"
    sobel =             "sobel/"
    hog =               "hog/"
    blur =              "blur/"
    rgb =               "rgb/"
    angel =             "angel/"
    satan =             "satan/"
    hitler =            "hitler/"
    obama =             "obama/"
    bad =               "bad/"
    sith =              "sith/"
    jail =              "jail/"
    gay =               "gay/"
    trash =             "trash/"
    deepfry =           "deepfry/"
    ascii =             "ascii/"
    charcoal =          "charcoal/"
    poster =            "poster/"
    sepia =             "sepia/"
    polaroid =          "polaroid/"
    swirl =             "swirl/"
    paint =             "paint/"
    night =             "night/"
    solar =             "solar/"
    thought_image =     "thoughtimage/"
    tweet =             "tweet/"
    discord =           "discord/"

    def __str__(self):
        return self.value


class Games(Enum):
    whos_that_pokemon = "wtp"
    logo_guessing =     "logo"
    roast =             "roast"
    yo_mama =           "yomama"
    pickupline =        "pickupline"
    waifu =             "waifu"
    joke =              "joke"

    def __str__(self):
        return self.value
