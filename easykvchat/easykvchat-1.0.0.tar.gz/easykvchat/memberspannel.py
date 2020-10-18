from kivy.uix import label, boxlayout
from kivy.properties import ObjectProperty


class MemberName(label.Label):
    pass


class MembersPannel(boxlayout.BoxLayout):
    list = ObjectProperty()
