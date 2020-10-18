import kivy
import kivy.support
from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty
from kivy.logger import Logger

# Permet d'éviter de charger le réacteur deux fois avec PyInstaller
import sys
if "twisted.internet.reactor" in sys.modules:
    del sys.modules["twisted.internet.reactor"]

kivy.support.install_twisted_reactor()

from twisted.internet import protocol  # noqa: E402
from twisted import protocols  # noqa: E402
import twisted.protocols.basic  # noqa: E402


def unformatMsg(msg):
    splitted = msg.split()
    return [splitted[0], " ".join(splitted[1:])]


class Session(protocols.basic.LineOnlyReceiver):
    def __init__(self):
        self.stopped = False

    def connectionMade(self):
        self.factory.session = self
        Logger.info("Session: Connecté à {}".format(self.transport.getPeer()))
        self.sendLine(self.factory.name.encode())

    def connectionLost(self, reason):
        if not self.stopped:
            self.factory.notifyConnectionLost(reason)

    def lineReceived(self, rawLine):
        line = unformatMsg(rawLine.decode())
        author, msg = line

        if not self.factory.registered:
            if author != "Server":
                raise RuntimeError("Réception de paquets non autorisée durant la phase d'inscription")

            if msg == "Inscription OK":
                self.factory.registered = True
            else:
                self.factory.notifyRegistrationError(msg)

            return

        notify = True
        if author == "Server":
            args = msg.split()
            operation = args[0]
            if operation == "Connexion":
                self.factory.notifyLogin(args[2])
            elif operation == "Déconnexion":
                self.factory.notifyLogout(args[2])
            elif operation == "Membres":
                self.factory.notifyRegistered(args[2:])
                notify = False

        if notify:
            self.factory.notifyMsg(author, msg)


class SessionFactory(protocol.Factory, EventDispatcher):
    protocol = Session

    def __init__(self, name):
        for event in ["message", "registration_error", "registered", "login", "logout", "disconnected",
                      "connection_lost"]:
            self.register_event_type("on_" + event)

        super().__init__()
        self.registered = False
        self.name = name
        self.session = None

    def message(self, msg):
        self.session.sendLine(msg.encode())

    def end(self):
        self.session.stopped = True
        self.session.transport.loseConnection()
        self.session = None

    def active(self):
        return self.session is not None

    def notifyMsg(self, author, msg):
        self.dispatch("on_message", sender=author, msg=msg)

    def notifyRegistrationError(self, reason):
        self.dispatch("on_registration_error", reason)

    def notifyRegistered(self, members):
        self.dispatch("on_registered", members)

    def notifyDisconnected(self):
        self.dispatch("on_disconnected")

    def notifyConnectionLost(self, reason):
        self.dispatch("on_connection_lost", reason)

    def notifyLogin(self, name):
        self.dispatch("on_login", name)

    def notifyLogout(self, name):
        self.dispatch("on_logout", name)

    def on_connection_lost(self, reason):
        Logger.error("Session: " + reason.getErrorMessage())

    def on_registration_error(self, reason):
        Logger.error("Registration: " + reason)

    def on_registered(self, members):
        Logger.info("Registration: OK")

    def on_message(self, **msg):
        Logger.info("Chat: {sender} : {msg}".format(**msg))

    def on_login(self, name):
        Logger.info("Session: Connexion de " + name)

    def on_logout(self, name):
        Logger.info("Session: Déconnexion de " + name)

    def on_disconnected(self):
        Logger.info("Session: Déconnexion")
