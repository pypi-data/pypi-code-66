from kivy.uix import scrollview, label
from kivy.properties import ObjectProperty


class RoomLogs(scrollview.ScrollView):
    logs = ObjectProperty()


class Message(label.Label):
    def __init__(self, sender, msg):
        super().__init__(text="[b]{} :[/b] {}".format(sender, msg))
