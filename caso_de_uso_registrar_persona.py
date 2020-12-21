import cv2
import dlib
import time
import urllib
import os

import numpy as np
import uuid
from models import *
from peewee import *
import pathlib

from global_variables import *
import cognitive_face as CF



CF.Key.set(cfKey)
CF.BaseUrl.set(URL)


# registrar estudiante por consola
# guardar estudiante en db
# check if exist person group
# read faces
# add faces to personGroup

def readPersonDetails():
    student = Student()
    student.fullName = str(input("Ingrese nombre y apellido de una persona:"))
    student.code = str(input("Ingrese el codigo o identificador de la persona:"))
    
    student.personGuid = str(uuid.uuid4())
    student.folderGuid = str(uuid.uuid4())

    return student



def saveStudentInDb(student):
    newStudent = Student.create(fullName = student.fullName, 
        code = student.code, 
        folderGuid = student.folderGuid,
        personGuid = student.personGuid)
    newStudent.save()



def createPersonGroupIfNotExits():
    personGroups = CF.person_group.lists()
    for personGroup in personGroups:
        if personGroupId == personGroup['personGroupId']:
            return None
    result = CF.person_group.create(personGroupId)





def creaateSampleFacesStudent(student, folderForSave):
    sampleNum = 0
    cantidadDeMuestras = 20

    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()

    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(img, 1)
        for i, d in enumerate(dets):
            sampleNum += 1
            fileName = "person--" + str(student.folderGuid) + "--" + str(sampleNum) + ".jpg"
            fullFileName = os.path.join(folderForSave, fileName)
            cv2.imwrite(fullFileName, img[d.top():d.bottom(), d.left():d.right()])
            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2)
            cv2.waitKey(200)
        cv2.imshow('frame', img)
        cv2.waitKey(1)
        print(f"image num {sampleNum}")
        if(sampleNum >= cantidadDeMuestras):
            break

    cap.release()
    cv2.destroyAllWindows()


def createFolderForDataset(folderName):
    currentDirectory = os.getcwd()
    folderPath = os.path.join(currentDirectory, "datasets", folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    return folderPath




def createPersonInCf(student):
    res = CF.person.create(personGroupId, f"{student.code}")
    print(res)
    Student.update(personGuid = res['personId']).where(Student.id == student.id).execute()



def addImageFacesToPersonId(student, folder):

    for filename in os.listdir(folder):
        if filename.endswith(".jpg"):
            print(filename)
            
            imgurl = urllib.request.pathname2url(os.path.join(folder, filename))
            res = CF.face.detect(imgurl)
            print(res)

            if len(res) != 1:
                print("No face detected in image")
            else:
                res = CF.person.add_face(imgurl, personGroupId, student.personGuid)
                print(res)
            time.sleep(6)


# check status, if not trained train
def train(student):
    res = CF.person_group.train(personGroupId)


student = readPersonDetails()
saveStudentInDb(student)

folder = createFolderForDataset(student.folderGuid)
creaateSampleFacesStudent(student, folder)

createPersonGroupIfNotExits()
createPersonInCf(student)


addImageFacesToPersonId(student, folder)
train(student)

