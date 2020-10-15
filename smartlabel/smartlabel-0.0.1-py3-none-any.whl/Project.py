from connection import db

class Project():
    def __init__(self):
        self.name=""
    
    def create_project(self, name, description = ""):
        mycursor = db.cursor()

        mycursor.execute("INSERT INTO project (Createdby,DatasetId, Name, Description, Status, Role) VALUES (%s,%s,%s,%s,%s,%s)",(1, 20, name, description, 0, 0))
        db.commit()

    def get_project(self, id):
        mycursor = db.cursor()
        mycursor.execute(f"SELECT * FROM project where ProjectId = {id}")

        for x in mycursor:
           
           thisdict = {
            "ProjectId": x[0],
            "Createdby": x[1],
            "DatasetId": x[2],
            "Name": x[3],
            "Description": x[4],
            "Status": x[5],
            "Role": x[6],
            "DateIn": x[7],
            "DateOut": x[8],
        }

        db.commit()
        return thisdict