## execute this for each student
import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
import dlib
import os                                                                       # for creating folders
import uuid

from db_models import Student
from peewee import *

from global_variables import sqliteDbFileName


###############################################################################

def createStudentFolderId(dbFile):
    db = SqliteDatabase(dbFile)
    db.connect()
    students = Student.select()
    for i in students:
        currentDirectory = os.getcwd()
        folderPath = os.path.join(currentDirectory, "dataset",i.personGuid)
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
    db.close()



def createStudentImages(personId):
    currentDirectory = os.getcwd()
    folderPath = os.path.join(currentDirectory, "dataset",folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)



def readStudentInfo():
    userInfo ={
        "name":"",
        "guid":str(uuid.uuid4())
    }
    userInfo["name"] = input("Ingrese nombre de estudiante")
    return userInfo



def addStudent(dbFile):
    db = SqliteDatabase(dbFile)
    db.connect()
    student = readStudentInfo()
    newStudent = Student.create(fullName=student["name"], personGuid=student["guid"])
    newStudent.create()
    db.close()



addStudent(sqliteDbFileName)
createStudentFolderId(sqliteDbFileName)




###############################################################################
### DELETE
## save entered info in sqlite db
def insertOrUpdate(Id, Name, roll) :                                            # this function is for database
    connect = sqlite3.connect("Face-DataBase")                                  # connecting to the database
    cmd = "SELECT * FROM Students WHERE ID = " + Id                             # selecting the row of an id into consideration
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET Name = ? WHERE ID = ?",(Name, Id))
        connect.execute("UPDATE Students SET Roll = ? WHERE ID = ?",(roll, Id))
    else:
        params = (Id, Name, roll)                                               # insering a new student data
        connect.execute("INSERT INTO Students(ID, Name, Roll) VALUES(?, ?, ?)", params)
    connect.commit()                                                            # commiting into the database
    connect.close()                                                             # closing the connection
###############################################################################



# read student data
name = input("Enter student's name : ")
roll = input("Enter student's Roll Number : ")
Id = roll[-2:]
insertOrUpdate(Id, name, roll)                                                  # calling the sqlite3 database
###############################################################################
# create user folder for students images
folderName = "user" + Id                                                        # creating the person or user folder



folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)

if not os.path.exists(folderPath):
    os.makedirs(folderPath)

###############################################################################
# get device video capturer, first device 0
# if not have device thows exception or thow error
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

###############################################################################

# capture sample images of student for train, and save image in folder
sampleNum = 0
while(True):
    ret, img = cap.read()                                                       # reading the camera input
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
    # detector image
    dets = detector(img, 1)
    for i, d in enumerate(dets):                                                # loop will run for each face detected
        sampleNum += 1
        cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg",
                    img[d.top():d.bottom(), d.left():d.right()])                                                # Saving the faces
        cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
        cv2.waitKey(200)                                                        # waiting time of 200 milisecond
    cv2.imshow('frame', img)                                                    # showing the video input from camera on window
    cv2.waitKey(1)
    if(sampleNum >= 20):                                                        # will take 20 faces
        break

###############################################################################

# dispose webcam pointer
cap.release()                                                                   # turning the webcam off
cv2.destroyAllWindows()                                                         # Closing all the opened windows
