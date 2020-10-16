import requests
from . import errors

class Stats():
    """
    Represents website's stats
    
    An instance of this class may be returned from `Client.fetch_stats` method, BUT SHOULD NOT BE MANUALLY CREATED.
    
    Attributes
    ----------
    bots : int
        This is the number of bots on the website

    pending_approvals : int
        This is the number of pending (not accepted) bots on the website
    """

    def __init__(self, payload: dict):
        if not ("bots" in payload and "pending_approvals" in payload and "unread_reports" in payload):
            raise errors.APIError("Bad payload received for stats")

        
        self.bots = payload["bots"]
        self.pending_approvals = payload["pending_approvals"]

    @property
    def unread_reports(self):
        raise NotImplementedError("Unread reports will be added as an attribute when report functionality will be added on the website.")
