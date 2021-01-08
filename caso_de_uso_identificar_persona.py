import cv2
import dlib
import urllib
import os

import cognitive_face as CF

from models import *
from global_variables import *


############################################################


CF.Key.set(APIKEY1)
CF.BaseUrl.set(URL)


def createFolderIfNotExits(folder):
    imagePath = os.path.join(os.getcwd(), folder)
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)
    return imagePath




def getPersonDetailsFromImage(imagePath):

    imgurl = urllib.request.pathname2url(imagePath)
    # Detect Face and return Face ID
    # result = CF.face.detect(imgurl)
    result = CF.face.detect(imagePath)
    # this faceIds only contain one face id, why image for detect has one face
    faceIds = []
    for face in result:
        faceIds.append(face["faceId"])

    # returns id of person detected personId
    # for this case only return one result
    # require object as
    # {
    #     'personGroupId': personGroupId,
    #     "faceIds": [faceId],
    #     "maxNumOfCandidatesReturned": 1,
    #     "confidenceThreshold": 0.5
    # }

    # RESULT
    # [{
    #       "faceId":
    #       "1990e7b2-490e-49fc-a0bd-c25c39eb7a7f",
    #       "candidates": [{
    #           "personId": "66ec4630-5369-4830-a20b-0f329d6eaf56",
    #           "confidence": 0.77458
    #         }]
    #  }
    # ]

    # def identify(face_ids,
    #              person_group_id=None,
    #              large_person_group_id=None,
    #              max_candidates_return=1,
    #              threshold=None):
    result = CF.face.identify(faceIds, personGroupId)
    for face in result:
        # def get(person_group_id, person_id):
        # TODO: check, "personId" is in first element of candidates
        personId = face["candidates"][0]["personId"]
        # Retrieve a person's information
        # personCode = CF.person.get(personGroupId, personId)
        student = Student.select().where(Student.personId == personId).first()
        print(student)


def detectFaces(folderTemp):

    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()

    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(img, 1)
        
        for i, d in enumerate(dets):
            # TODO: check this part
            fileName = "person--" + str(uuid.uuid4()) +".jpg"
            fullFileName = os.path.join(folderTemp, fileName)
            cv2.imwrite(fullFileName, img[d.top():d.bottom(), d.left():d.right()])
            # print(f"image num {fileName}")
            # eror de escritura
            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2)
            cv2.waitKey(200)
            getPersonDetailsFromImage(fullFileName)

        cv2.imshow('frame', img)
        cv2.waitKey(1)


    cap.release()
    cv2.destroyAllWindows()



path = "folder_temp_detect"
tempImagePath = createFolderIfNotExits(path)
detectFaces(tempImagePath)


