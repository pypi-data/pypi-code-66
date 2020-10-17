#File to permit has use model test

from clients.note import NoteModel

nte = NoteModel()
nte.valeur = 10
print(nte.get())