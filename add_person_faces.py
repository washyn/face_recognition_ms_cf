# oka executed

import sys
import os
import time
import cognitive_face as CF

from global_variables import personGroupId
from global_variables import cfKey
from global_variables import sqliteDbFileName
from apiKeys import URL

import urllib
import sqlite3
import pathlib

from models import *

CF.Key.set(cfKey)
CF.BaseUrl.set(URL)

###################################################################
# OLD CODE
## a partir del id en db se obtiene el id de cara
def get_person_id():
    person_id = ''
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    c = connect.cursor()
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    c.execute(cmd)
    row = c.fetchone()
    person_id = row[3]
    connect.close()
    return person_id



def getCurrentFakeFaceIdByUserId(idToFind):
    return Student.get_by_id(idToFind).folderGuid



def getFaceIdFromPersonId(idToFind):
    return Student.get_by_id(idToFind).personGuid



def main():
    print("For generate face id from microsoft cognitive services")
    userId = str(input("Enter user id from db:"))
    resultFolderGuid = getCurrentFakeFaceIdByUserId(userId)
    resultFaceId = getFaceIdFromPersonId(userId)

    imageFolder = os.path.join(os.getcwd(), "dataset", resultFolderGuid)

    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
            print(filename)
            
            imgurl = urllib.request.pathname2url(os.path.join(imageFolder, filename))
            res = CF.face.detect(imgurl)
            print(res)

            if len(res) != 1:
                print("No face detected in image")
            else:
                res = CF.person.add_face(imgurl, personGroupId, resultFaceId)
                print(res)
            time.sleep(6)

main()


# ###################################################################
# # if len(sys.argv) is not 1:
# if len(sys.argv) != 1:
#     # currentDir = os.path.dirname(os.path.abspath(__file__))
#     currentDir = os.getcwd()
#     imageFolder = os.path.join(currentDir, "dataset", str(sys.argv[1]))
# 	# recive el id de estudiante en base de datos, la col3 el personID
#     person_id = get_person_id()
#     for filename in os.listdir(imageFolder):
#         if filename.endswith(".jpg"):
#             print(filename)
#             # imgurl = urllib.pathname2url(os.path.join(imageFolder, filename))
#             imgurl = pathlib.Path(os.path.join(imageFolder, filename)).as_uri()
            
#             res = CF.face.detect(imgurl)
#             if len(res) != 1:
#                 print("No face detected in image")
#             else:
#                 res = CF.person.add_face(imgurl, personGroupId, person_id)
#                 print(res)
#             time.sleep(6)
