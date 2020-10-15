from pydantic import EmailStr

from .Examples import Responses as Examples
from ..Attributes import ModelId, ModelInfo


class Create(ModelId):
    pass


class Get(Examples.Get, ModelInfo):
    pass


class Train(Examples.Train, ModelId):
    pass


class Deploy(Examples.Deploy, ModelId):
    pass


class Clear(Examples.Clear, ModelId):
    pass


class Delete(Examples.Delete, ModelId):
    pass


class AddCollaborator(Examples.AddCollaborator):
    collaborator: EmailStr


class RemoveCollaborator(Examples.RemoveCollaborator):
    collaborator: EmailStr
