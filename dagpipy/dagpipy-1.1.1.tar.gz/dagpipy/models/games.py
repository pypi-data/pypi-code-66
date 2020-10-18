__all__ = (
    'Pokemon',
    'LogoGame',
    'Roast',
    'YoMama',
    'PickupLine',
    'Joke',
    'Waifu'
)


class Pokemon:
    def __init__(self, data: dict):
        DATA = data['Data']
        self.data = data
        self.types = DATA.get('Type')
        self.abilities = DATA.get('abilities')
        self.ascii = DATA.get('ascii')
        self.height = DATA.get('height')
        self.id = int(DATA.get('id'))
        self.link = DATA.get('link')
        self.name = DATA.get('name')
        self.weight = DATA.get('weight')
        self.answer = data.get('answer')
        self.question = data.get('question')

    def __repr__(self):
        return self.question


class LogoGame:
    def __init__(self, data: dict):
        self.answer = data.get('answer')
        self.question = data.get('question')
        self.brand = data.get('brand')
        self.wiki = str(data.get('wiki_url')).replace(" ", "")
        self.hint = data.get('hint')
        self.clue = data.get('clue')
        if data.get('easy'):
            self.difficulty = "easy"
        else:
            self.difficulty = "hard"

    def __repr__(self):
        return str(self.data)


class Roast:
    def __init__(self, data: dict):
        self.roast = data.get('roast')

    def __repr__(self):
        return self.roast


class YoMama:
    def __init__(self, data: dict):
        self.description = data.get('description')

    def __repr__(self):
        return self.description


class PickupLine:
    def __init__(self, data: dict):
        self.category = data.get('category')
        self.joke = data.get('joke')

    def __repr__(self):
        return self.joke


class Joke:
    def __init__(self, data: dict):
        self.id = int(data.get('id'))
        self.joke = data.get('joke')

    def __repr__(self):
        return self.joke


class Series:
    def __init__(self, data: dict):
        self.airing_end = data.get('airing_end')
        self.airing_start = data.get('airing_start')
        self.description = data.get('description')
        self.display_picture = data.get('display_picture')
        self.name = data.get('name')
        self.original_name = data.get('original_name')
        self.release = data.get('release')
        self.romaji_name = data.get('romaji_name')
        self.slug = data.get('slug')
        self.studio = data.get('studio')

    def __repr__(self):
        return self.name


class Creator:
    def __init__(self, data: dict):
        self.name = data.get('name')
        self.id = int(data.get('id'))

    def __repr__(self):
        return self.name


class Waifu:
    def __init__(self, data: dict):
        self.data = data
        self.age = data.get('age')
        self.birthday_day = data.get('birthday_day')
        self.birthday_month = data.get('birthday_month')
        self.blood_type = data.get('blood_type')
        self.bust = data.get('bust')
        self.description = data.get('description')
        self.display_picture = data.get('display_picture')
        self.height = data.get('height')
        self.hip = data.get('hip')
        self.husbando = data.get('husbando')
        self.id = data.get('id')
        self.like_rank = data.get('like_rank')
        self.likes = data.get('likes')
        self.name = data.get('name')
        self.nsfw = data.get('nsfw')
        self.origin = data.get('origin')
        self.original_name = data.get('original_name')
        self.popularity_rank = data.get('popularity_rank')
        self.romaji_name = data.get('romaji_name')
        self.slug = data.get('slug')
        self.tags = data.get('tags')
        self.trash = data.get('trash')
        self.trash_rank = data.get('trash_rank')
        self.url = data.get('url')
        self.waist = data.get('waist')
        self.weight = data.get('weight')

    def __repr__(self):
        return f"{self.name}: {self.description}"
        
    @property
    def creator(self):
        return Creator(self.data.get('creator'))

    @property
    def series(self):
        return Series(self.data.get('series'))

    @property
    def appearances(self):
        return [Series(d) for d in self.data.get('appearances')]