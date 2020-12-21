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


def getCurrentFakeFaceIdByUserId(idToFind):
    return Student.get_by_id(idToFind).folderGuid

def getFaceIdFromPersonId(idToFind):
    return Student.get_by_id(idToFind).personGuid

def main():
    print("For generate face id from microsoft cognitive services")
    userId = str(input("Enter user id from db:"))
    resultFolderGuid = getCurrentFakeFaceIdByUserId(userId)
    resultFaceId = getFaceIdFromPersonId(userId)

    imageFolder = os.path.join(os.getcwd(), "../dataset", resultFolderGuid)

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
