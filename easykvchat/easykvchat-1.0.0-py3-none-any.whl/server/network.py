import kivy
import kivy.support
from kivy.properties import DictProperty
from kivy.event import EventDispatcher
from kivy.logger import Logger

# Permet d'éviter de charger le réacteur deux fois avec PyInstaller
import sys
if "twisted.internet.reactor" in sys.modules:
    del sys.modules["twisted.internet.reactor"]

from twisted.internet import protocol  # noqa: E402
from twisted import protocols  # noqa: E402
from twisted.protocols import basic  # noqa: E402


def formatMsg(sender, msg):
    return "{} {}".format(sender, msg).encode()


class MemberConnection(protocols.basic.LineOnlyReceiver):
    def __init__(self, room):
        super().__init__()

        self.registered = False
        self.name = None
        self.room = room
        self.members = self.room.members

    def remote(self):
        peer = self.transport.getPeer()
        return peer.host + ":" + str(peer.port)

    def message(self, sender, msg):
        self.room.notiftyMsg(sender, msg)

        for member in self.members.keys():
            if member != self.name:
                self.members[member].sendLine(formatMsg(sender, msg))

    def connectionMade(self):
        Logger.info("Server: Connexion de " + self.remote())

    def connectionLost(self, reason):
        if self.name not in self.members:
            return

        del self.members[self.name]
        self.message("Server", "Déconnexion : " + self.name)

        self.room.notifyDisconnected(self)

    def lineReceived(self, rawLine):
        line = rawLine.decode()

        if self.registered:
            self.message(self.name, line)
            return

        if line == "Server" or " " in line:
            self.sendLine(formatMsg("Server", "Échec : Le nom ne doit ni être Server ni contenir d'espaces"))
            return

        if line in self.members.keys():
            self.sendLine(formatMsg("Server", "Échec : Ce nom est déjà pris."))
            return

        self.name = line
        self.members[self.name] = self
        self.registered = True
        self.message("Server", "Connexion : " + self.name)

        self.sendLine(formatMsg("Server", "Inscription OK"))
        self.sendLine(formatMsg("Server", "Membres : " + " ".join(self.members.keys())))
        self.room.notifyRegistered(self)


class ChatRoom(protocol.Factory, EventDispatcher):
    protocol = MemberConnection

    def __init__(self):
        for event in ["registered", "disconnected", "message"]:
            self.register_event_type("on_" + event)

        super().__init__()
        self.members = {}

    def buildProtocol(self, _):
        return ChatRoom.protocol(self)

    def notiftyMsg(self, sender, msg):
        self.dispatch("on_message", sender=sender, msg=msg)

    def notifyRegistered(self, member):
        self.dispatch("on_registered", name=member.name, endpt=member.remote())

    def notifyDisconnected(self, member):
        self.dispatch("on_disconnected", name=member.name, endpt=member.remote())

    def on_registered(self, **member):
        Logger.info("Server: Inscription de {endpt} -> {name}".format(**member))

    def on_disconnected(self, **member):
        Logger.info("Server: Déconnexion de {name} ({endpt})".format(**member))

    def on_message(self, **msg):
        Logger.info("Chat: {sender} : {msg}".format(**msg))

    def on_members(self, members):
        if len(members) > self.lastCount:
            print("Inscription :")
