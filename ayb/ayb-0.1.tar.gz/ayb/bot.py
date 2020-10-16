import requests
from . import errors, category, client

class Bot():
    """
    Represents a bot on the website.
    
    An instance of this class may be returned from `Client.fetch_bot` method, BUT SHOULD NOT BE MANUALLY CREATED.

    Attributes
    ----------
    clientid : int
        This is the bot's discord ID
    
    ownerid : int
        This is the bot owner's discord ID
        
    botname : str
        This is the discord bot's name
    
    botavatar : str
        This is the bot's avatar URL
        
    category : int
        This is the bot category ID, you can fetch the category using the `Bot.fetch_category` method
    
    approved : bool
        Whether or not the bot has been approved on the website
    
    certified : bool
        Whether or not the bot is certified on the website
        
    premium : bool
        Whether or not the bot is premium on the website
    
    prefix : str
        This is the bot's prefix to use
    
    permissions : int
        The permissions the bot asks when you invite it
    
    library : str
        The library the bot is coded with
    
    brief : str
        The short description for the bot
    
    description : str
        The long description text for the bot
    
    websiteurl : str or None
        The bot website URL, if any
    
    github : str or None
        The bot github URL, if any
    
    supportservercode : str or None
        The support server invite code, the part after "https://discord.gg/", if any
    """
    def __init__(self, client, payload: dict, id_ : int):
        self.client = client
        if payload["success"] == False:
            raise errors.InvalidBot(id_)
        
        self.clientid = int(payload["clientid"])
        self.ownerid = int(payload["ownerid"])
        self.botname = payload["botname"]
        self.botavatar = payload["botavatar"]
        #self.score = payload["score"]
        self.category = payload["category"]
        self.approved = payload["approved"]
        self.certified = payload["certified"]
        self.premium = payload["premium"]
        self.prefix = payload["prefix"]
        self.permissions = int(payload["permissions"])
        self.library = payload["library"]
        self.brief = payload["brief"]
        self.description = payload["description"]
        self.websiteurl = payload["websiteurl"] or None
        self.github = payload["github"] or None
        self.supportservercode = payload["supportservercode"] or None
    
    @property
    def score(self):
        raise NotImplementedError("Bot scoring will be added as an attribute when scoring functionality will be added on the website.")
    
    def fetch_category(self):
        return self.client.fetch_category(self.category)