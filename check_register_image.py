import dlib
import time
import urllib
import os
import pathlib
import cv2



from models import *




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





# ok, Read person details from console, full name and code
def readPersonDetails():
    student = Student()

    student.fullName = str(input("Ingrese nombre y apellido de una persona:"))
    student.code = str(input("Ingrese el codigo o identificador de la persona:"))
    
    student.personGuid = str(uuid.uuid4())
    student.folderGuid = str(uuid.uuid4())
    student.personId = str(uuid.uuid4())

    return student






# ok, register faces of student
def creaateSampleFacesStudent(student, folderForSave):
    sampleNum = 0
    nSamples = 100

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
            # show 
            cv2.waitKey(200)
        cv2.imshow('frame', img)
        # show 
        cv2.waitKey(1)
        print(f"image num {sampleNum}")
        if(sampleNum >= nSamples):
            break

    cap.release()
    cv2.destroyAllWindows()


################################################################################################

# crea un folder donde se guardara las imagenes de muestra
def createFolderForDataset(folderName):
    folderDataset = "datasets"
    currentDirectory = os.getcwd()
    folderPath = os.path.join(currentDirectory, folderDataset, folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    return folderPath


####################################

student = readPersonDetails()


folder = createFolderForDataset(student.folderGuid)
creaateSampleFacesStudent(student, folder)
