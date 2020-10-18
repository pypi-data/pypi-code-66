import easykvchat.client.network
from easykvchat.memberspannel import MemberName
from easykvchat.roomlogs import Message

import kivy
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.metrics import mm
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty

from twisted.internet import endpoints
from twisted.internet import reactor

kivy.require("2.0.0")

Window.minimum_width = mm(170)
Window.minimum_height = mm(120)


class LoginInput(AnchorLayout):
    hint = StringProperty()
    text = StringProperty()
    writeTab = BooleanProperty(False)
    connect = ObjectProperty()


class LoginButton(AnchorLayout):
    button = ObjectProperty()

    def __init__(self, **kwargs):
        self.register_event_type("on_connect")
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.button.collide_point(*touch.pos):
            self.dispatch("on_connect")

        return super().on_touch_down(touch)

    def on_connect(self):
        Logger.debug("Connexion...")


class LoginForm(BoxLayout):
    host = ObjectProperty()
    name = ObjectProperty()
    connection = ObjectProperty()


class LoginScreen(AnchorLayout):
    form = ObjectProperty()


class RoomScreen(BoxLayout):
    messages = ObjectProperty()


class Messages(BoxLayout):
    chat = ObjectProperty()
    input = ObjectProperty()


class Pannel(BoxLayout):
    LeavingColor = (.97, .29, 0)
    NormalColor = (.05, .05, .05)

    members = ObjectProperty()
    leave = ObjectProperty()

    def __init__(self, **kwargs):
        self.register_event_type("on_quit")
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        if not self.leave.collide_point(*touch.pos):
            return super().on_touch_down(touch)

        touch.grab(self)
        self.leave.background_color = Pannel.LeavingColor

        return True

    def on_touch_up(self, touch):
        if touch.grab_current != self:
            return super().on_touch_up(touch)

        self.leave.background_color = Pannel.NormalColor
        self.dispatch("on_quit")
        touch.ungrab(self)

        return True

    def on_quit(self):
        Logger.info("Session: Déconnexion")


class InvalidHostFormat(ValueError):
    def __init__(self, reason):
        super().__init__(reason)


class ErrorMessage(AnchorLayout):
    text = StringProperty()


class ErrorPopup(Popup):
    def __init__(self, title, error):
        super().__init__(title=title, content=ErrorMessage(text=error))

    def on_touch_down(self, _):
        self.dismiss()
        return True


class MainScreen(FloatLayout):
    login = ObjectProperty()
    room = ObjectProperty()

    def __init__(self, **kwargs):
        self.register_event_type("on_start")
        super().__init__(**kwargs)
        self.members = {}

    def on_start(self):
        self.login.form.connection.bind(on_connect=self.connect)
        self.room.messages.input.bind(on_text_validate=self.validateMessage)
        self.room.pannel.bind(on_quit=self.disconnect)

    def connect(self, _):
        host = ""
        port = 0
        try:
            host = self.login.form.host.text.split(":")

            if len(host) != 2 or not host[0]:
                raise InvalidHostFormat("Format : <adresse>:<port>")

            try:
                port = int(host[1])

                if port < 0 or port > 65535:
                    raise ValueError()
            except ValueError:
                raise InvalidHostFormat("Le port doit être un entier compris entre 0 et 65535 inclus.")
        except InvalidHostFormat as err:
            ErrorPopup("Hôte invalide", str(err)).open()
            return

        self.chat = easykvchat.client.network.SessionFactory(self.login.form.name.text)
        self.client = endpoints.TCP4ClientEndpoint(reactor, host[0], port)
        self.client.connect(self.chat).addErrback(self.ioError)

        self.chat.bind(on_registration_error=self.registrationFailed,
                       on_registered=self.registered,
                       on_connection_lost=lambda _, failure: self.ioError(failure),
                       on_message=self.message,
                       on_login=lambda _, name: self.registerMember(name),
                       on_logout=lambda _, name: self.unregisterMember(name))

        self.switchMode()

    def disconnect(self, _=None):
        self.switchMode()

        if not self.chat.active():
            return

        self.chat.end()
        self.chat = None

        self.room.messages.chat.logs.clear_widgets()
        for member in self.members.values():
            self.room.pannel.members.list.remove_widget(member)
            del member

    def validateMessage(self, _):
        message = self.room.messages.input.text

        self.chat.message(message)
        self.room.messages.input.text = ""
        self.message(sender=self.chat.name, msg=message)

    def ioError(self, failure):
        self.disconnect()
        ErrorPopup(failure.value.__class__.__name__, failure.getErrorMessage()).open()

    def registrationFailed(self, _, reason):
        self.switchMode()
        ErrorPopup("Inscription échouée", reason).open()

    def registerMember(self, member):
        self.members[member] = MemberName(text=member)
        self.room.pannel.members.list.add_widget(self.members[member])

    def unregisterMember(self, name):
        member = self.members[name]

        self.room.pannel.members.list.remove_widget(member)
        del member

    def registered(self, _, members):
        for member in members:
            self.registerMember(member)

    def message(self, _=None, **msg):
        self.room.messages.chat.logs.add_widget(Message(**msg))

    def switchMode(self):
        self.login.pos_hint, self.room.pos_hint = self.room.pos_hint, self.login.pos_hint


class ClientApp(App):
    def on_start(self):
        super().on_start()
        self.root.dispatch("on_start")


if __name__ == "__main__":
    ClientApp().run()
