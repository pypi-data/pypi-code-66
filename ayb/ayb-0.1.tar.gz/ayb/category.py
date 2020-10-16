import requests
from . import errors

class Category():
    """
    Represents a category on the website.
    
    An instance of this class may be returned from `Bot.fetch_category` or `Client.fetch_category` methods, BUT SHOULD NOT BE MANUALLY CREATED.
    
    Attributes
    ----------
    id : int
        This is the category's ID

    name : str
        This is the category's name

    slug : str
        This is the category's slug, unique and lowercased
    """

    def __init__(self, payload: dict, id_ : int):
        if payload["success"] == False:
            raise errors.InvalidCategory(id_)
        
        self.id = payload["id"]
        self.name = payload["name"]
        self.slug = payload["slug"]