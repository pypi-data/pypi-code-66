import easykvchat.server.network
from easykvchat.roomlogs import Message
from easykvchat.memberspannel import MemberName

import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from twisted.internet import endpoints
from twisted.internet import reactor

kivy.require("2.0.0")


class RoomScreen(BoxLayout):
    chat = ObjectProperty()
    members = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.membersList = {}

    def refreshChat(self, _, **msg):
        self.chat.logs.add_widget(Message(**msg))

    def addMember(self, _, **member):
        name = member["name"]
        self.membersList[name] = MemberName(text="{name} ({endpt})".format(**member))
        self.members.list.add_widget(self.membersList[name])

    def delMember(self, _, **member):
        target = self.membersList[member["name"]]
        self.members.list.remove_widget(target)
        del target


class ServerApp(App):
    def __init__(self, port, **kwargs):
        super().__init__(**kwargs)
        self.port = port

        self.room = easykvchat.server.network.ChatRoom()
        self.server = endpoints.TCP4ServerEndpoint(reactor, self.port)
        self.server.listen(self.room)

        self.room.bind(on_message=self.refreshChat,
                       on_registered=self.addMember,
                       on_disconnected=self.delMember)

    def refreshChat(self, room, **args):
        self.root.refreshChat(room, **args)

    def addMember(self, room, **args):
        self.root.addMember(room, **args)

    def delMember(self, room, **args):
        self.root.delMember(room, **args)


if __name__ == "__main__":
    ServerApp(39999).run()
