# oka executed

## execute this for each student
import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
import dlib
import os                                                                       # for creating folders
import uuid

# from db_models import Student
from models import *
from peewee import *

from global_variables import sqliteDbFileName



###############################################################################

# def createStudentFolderId(dbFile):
#     db = SqliteDatabase(dbFile)
#     db.connect()
#     students = Student.select()
#     for i in students:
#         currentDirectory = os.getcwd()
#         folderPath = os.path.join(currentDirectory, "dataset",i.personGuid)
#         if not os.path.exists(folderPath):
#             os.makedirs(folderPath)
#     db.close()



def createStudentImages(personId):
    currentDirectory = os.getcwd()
    folderPath = os.path.join(currentDirectory, "dataset",personId)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)



def readStudentInfo():
    userInfo ={
        "name":"",
        "folderGuid":str(uuid.uuid4()),
        "personGuid":str(uuid.uuid4()),
    }
    userInfo["name"] = input("Ingrese nombre de estudiante:")
    return userInfo



def addStudent(dbFile,student):
    db = SqliteDatabase(dbFile)
    db.connect()
    newStudent = Student.create(fullName=student["name"], folderGuid=student["folderGuid"], personGuid=student["personGuid"])
    newStudent.save()
    db.close()




def creaateSampleFacesStudent(folderForSave):
    ###############################################################################
    # capture sample images of student for train, and save image in folder
    sampleNum = 0
    # ideal 20
    cantidadDeMuestras = 20
    ###############################################################################
    # get device video capturer, first device 0
    # if not have device thows exception or thow error
    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    ###############################################################################
    while(True):
        ret, img = cap.read()                                                       # reading the camera input
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
        # detector image
        dets = detector(img, 1)
        for i, d in enumerate(dets):                                                # loop will run for each face detected
            sampleNum += 1
            fileName = "person--" + student["folderGuid"] + "--" + str(sampleNum) + ".jpg"
            fullFileName = os.path.join(folderForSave, fileName)
            cv2.imwrite(fullFileName, img[d.top():d.bottom(), d.left():d.right()])                                                # Saving the faces
            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
            cv2.waitKey(200)                                                        # waiting time of 200 milisecond
        cv2.imshow('frame', img)                                                    # showing the video input from camera on window
        cv2.waitKey(1)
        print(f"image num {sampleNum}")
        if(sampleNum >= cantidadDeMuestras):                                                        # will take 20 faces
            break

    ###############################################################################
    # dispose webcam pointer
    cap.release()                                                                   # turning the webcam off
    cv2.destroyAllWindows()                                                         # Closing all the opened windows



student = readStudentInfo()
addStudent(sqliteDbFileName, student)
createStudentImages(student["folderGuid"])
# this create for all students folder
# createStudentFolderId(sqliteDbFileName)

folderCreateSampleImages = os.path.join(os.getcwd(), "dataset",student["folderGuid"])
creaateSampleFacesStudent(folderCreateSampleImages)