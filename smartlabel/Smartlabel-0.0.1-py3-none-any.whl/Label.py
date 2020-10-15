from connection import db

class Label_Object():
    def __init__(self):
        self.name=""
    
    def create_Label(self, name, LabelType = ""):
        mycursor = db.cursor()

        mycursor.execute("INSERT INTO labelobj (ProjectId, Name, LabelType, Color) VALUES (%s,%s,%s,%s)",(7,name, LabelType,"#0000"))
        db.commit()

    def get_Label(self, id):
        mycursor = db.cursor()
        mycursor.execute(f"SELECT * FROM labelobj where LabelObjId  = {id}")

        for x in mycursor:
           
           thisdict = {
            "LabelObjId": x[0],
            "ProjectId": x[1],
            "Name": x[2],
            "LabelType": x[3],
            "Color": x[4],
            "DateIn": x[5],
            "DateOut": x[6],
        }

        db.commit()
        return thisdict