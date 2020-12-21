from models import Student
import uuid

from global_variables import *

import cv2
import numpy as np
import sqlite3
import dlib
import os
import uuid


from models import *
from peewee import *

import cognitive_face as CF




import sys
import os
import time
import cognitive_face as CF

from global_variables import personGroupId
from global_variables import cfKey
from global_variables import sqliteDbFileName


import urllib
import sqlite3
import pathlib

from models import *

############################################################


CF.Key.set(cfKey)
CF.BaseUrl.set(URL)


def createFolderIfNotExits(folder):
    imagePath = os.path.join(os.getcwd(),folder)
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)
    return imagePath

def getPersonDetailsFromImage(imagePath):

    imgurl = urllib.request.pathname2url(imagePath)
    result = CF.face.detect(imgurl)

    faceIds = []
    for face in result:
        faceIds.append(face["faceId"])
    
    result = CF.face.identify(faceIds, personGroupId)
    for face in result:
        personCode = CF.person.get(personGroupId, face["candidates"]["personId"])
        student = Student.select(Student.code == personCode).first()
        print(student)


def detectFaces(folderTemp):

    imageName = ""
    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()

    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(img, 1)
        for i, d in enumerate(dets):
            fileName = "person--" + str(uuid.uuid4()) +".jpg"
            fullFileName = os.path.join(folderTemp, fileName)
            cv2.imwrite(fullFileName, img[d.top():d.bottom(), d.left():d.right()])
            print(f"image num {fileName}")

            # getPersonDetailsFromImage(fullFileName)

            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2)
            cv2.waitKey(200)

        cv2.imshow('frame', img)
        cv2.waitKey(1)


    cap.release()
    cv2.destroyAllWindows()



path = "folder_temp_detect"
tempImagePath = createFolderIfNotExits(path)
detectFaces(tempImagePath)


