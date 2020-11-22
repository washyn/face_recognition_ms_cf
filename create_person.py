# oka executed

import sys
import cognitive_face as CF
from global_variables import personGroupId
from global_variables import cfKey
from global_variables import sqliteDbFileName
from apiKeys import URL
import sqlite3
from models import *
from apiKeys import APIKEY1
from apiKeys import URL

###################################################################
# microsoft cognitive service

CF.Key.set(APIKEY1)
CF.BaseUrl.set(URL)


def createFaceIdFromStudentId():
    studentId = input("enter student id:")
    res = CF.person.create(personGroupId, str(studentId))
    
    print(res)
    # todo comment where not requier connetct
    db = SqliteDatabase(sqliteDbFileName)
    db.connect()
    # update
    nrows = (Student
            .update(personGuid=res['personId'])
            .where(Student.id == studentId)
            .execute())
    db.close()

createFaceIdFromStudentId()


# if len(sys.argv) is not 1:
#     res = CF.person.create(personGroupId, str(sys.argv[1]))
#     print(res)

#     extractId = str(sys.argv[1])[-2:]
    
#     connect = sqlite3.connect("Face-DataBase")
#     cmd = "SELECT * FROM Students WHERE ID = " + extractId
#     cursor = connect.execute(cmd)
#     isRecordExist = 0
#     for row in cursor:                                                          # checking wheather the id exist or not
#         isRecordExist = 1
#     if isRecordExist == 1:                                                      # updating name and roll no
#         connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res['personId'], extractId))
#     connect.commit()                                                            # commiting into the database
#     connect.close()
#     print("Person ID successfully added to the database")
