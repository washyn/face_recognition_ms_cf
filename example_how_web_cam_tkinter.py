import PIL
import pytesseract
import cv2
import dlib
import os
import uuid

from tkinter import *
from PIL import Image,ImageTk
from caso_de_uso_identificar_persona import createFolderForImages, getPersonDetailsFromImageFrame, getPersonDetailsFromImageName









width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()

root.geometry("800x550")
root.resizable(False, False)
root.bind('<Escape>', lambda e: root.quit())

lmain = Label(root)
lmain.pack()

personLabel = Label(root, text="Datos de persona identificada", font=("Arial",25))
personLabel.pack()

# root.protocol("WM_DELETE_WINDOW", root.quit())









detector = dlib.get_frontal_face_detector()
folderTemp = createFolderForImages()









trainIfNotTrained()








counter = 4564

def show_frame():
    # global counter
    # counter = counter + 1

    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # add recognizer here
    print("image")

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    #################################################################################
    # cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    dets = detector(frame,1)
    for i,d in enumerate(dets):
        fileName = str(uuid.uuid4()) + ".jpg"
        fullFileName = os.path.join(folderTemp, fileName)
        # TODO: uncomment
        # cv2.imwrite(fullFileName, frame[d.top():d.bottom(), d.left():d.right()])


        # print(f"image num {fileName}")
        # eror de escritura

        cv2image = cv2.rectangle(frame, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2)

        
        # cv2.waitKey(200)
        # personDetails = getPersonDetailsFromImageName(fullFileName)
    
        # personDetails = getPersonDetailsFromImage(frame[d.top():d.bottom(), d.left():d.right()])


        # TODO: uncomment
        # personDetails = getPersonDetailsFromImageName(fullFileName)
        # personLabel.config(text = personDetails)



    #################################################################################


    # img = PIL.Image.fromarray(frame)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)





show_frame()
root.mainloop()
