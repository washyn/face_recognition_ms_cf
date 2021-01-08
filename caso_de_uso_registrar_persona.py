import cv2
import dlib
import time
import urllib
import os
import pathlib


import cognitive_face as CF

from models import *
from global_variables import *



CF.Key.set(cfKey)
CF.BaseUrl.set(URL)



###############################################################################
# create person group if not exits
###############################################################################
# add person
###############################################################################
# add faces to person
###############################################################################
###############################################################################



# registrar estudiante por consola
# guardar estudiante en db
# check if exist person group
# read faces
# add faces to personGroup



###############################################################################
###############################################################################
###############################################################################

# Ok, iterate all person groups when not exists person group
# crete person group
def createPersonGroupIfNotExits():
    personGroups = CF.person_group.lists()
    for personGroup in personGroups:
        if personGroupId == personGroup['personGroupId']:
            return None
    result = CF.person_group.create(personGroupId)
    return result


# ok, create person id
def createPersonInCfAndUpdateInLocalDb(student):
    # def create(person_group_id, name, user_data=None):
    response = CF.person.create(personGroupId, f"{student.code}")
    Student.update(personGuid = response['personId']).where(Student.id == student.id).execute()
    Student.update(personId = response['personId']).where(Student.id == student.id).execute()
    print(response)
    # return response
    return Student.get_by_id(student.id)

# add image faces to person
def addImageFacesToPerson(student, folder):
    for filename in os.listdir(folder):
        if filename.endswith(".jpg"):
            print(filename)

            # corregit el url de image
            # ver el objeto URL
            # os.path.abspath


           

            fullFileName = os.path.join(folder, filename)
            # absPath = os.path.abspath(fullFileName)
            # imgurl = urllib.request.pathname2url(absPath)
            # imgurl = pathlib.Path(fullFileName).as_uri()


            res = CF.face.detect(fullFileName)

            print(res)

            if len(res) != 1:
                print("No face detected in image")
            else:
                # def add_face(image,
                #              person_group_id,
                #              person_id,
                #              user_data=None,
                #              target_face=None):
                res = CF.person.add_face(fullFileName, personGroupId, student.personId)
                print(res)
            time.sleep(6)


###############################################################################
###############################################################################
###############################################################################


# ok
def readPersonDetails():
    student = Student()

    student.fullName = str(input("Ingrese nombre y apellido de una persona:"))
    student.code = str(input("Ingrese el codigo o identificador de la persona:"))
    
    student.personGuid = str(uuid.uuid4())
    student.folderGuid = str(uuid.uuid4())
    student.personId = str(uuid.uuid4())

    return student





# ok
def saveStudentInDb(student):
    newStudent = Student.create(fullName = student.fullName, 
        code = student.code, 
        folderGuid = student.folderGuid,
        personGuid = student.personGuid,
        personId = student.personId)
    newStudent.save()
    return newStudent

# ok, register faces of student
def creaateSampleFacesStudent(student, folderForSave):
    sampleNum = 0
    nSamples = 5

    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()

    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(img, 1)
        for i, d in enumerate(dets):
            # TODO: check this part
            sampleNum += 1
            fileName = "person--" + str(student.folderGuid) + "--" + str(sampleNum) + ".jpg"
            fullFileName = os.path.join(folderForSave, fileName)
            # se toma la captura 2 veces
            # cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg", img[d.top():d.bottom(), d.left():d.right()])      

            cv2.imwrite(fullFileName, img[d.top():d.bottom(), d.left():d.right()])
            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2)
            cv2.waitKey(200)
        cv2.imshow('frame', img)
        cv2.waitKey(1)
        print(f"image num {sampleNum}")
        if(sampleNum >= nSamples):
            break

    cap.release()
    cv2.destroyAllWindows()


################################################################################################


def createFolderForDataset(folderName):
    folderDataset = "datasets"
    currentDirectory = os.getcwd()
    folderPath = os.path.join(currentDirectory, folderDataset, folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    return folderPath



# OK, check status, if not trained train
def train():
    # def train(person_group_id):
    # statusTrained = CF.person_group.get_status(personGroupId)
    # if statusTrained["status"] != "succeeded":
    #     res = CF.person_group.train(personGroupId)
    res = CF.person_group.train(personGroupId)
    return res


def eliminarPersonGroup(personGr):
    CF.person_group.delete(personGr)

####################################

# student = readPersonDetails()
# student = saveStudentInDb(student)

# folder = createFolderForDataset(student.folderGuid)
# creaateSampleFacesStudent(student, folder)

# createPersonGroupIfNotExits()

# student = createPersonInCfAndUpdateInLocalDb(student)
# addImageFacesToPerson(student, folder)
####################################


# eliminarPersonGroup(personGroupId)

train()
