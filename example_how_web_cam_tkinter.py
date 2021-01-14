import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import *

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

personLabel = Label(root, text="Persona identificada", font=("Arial",25))

personLabel.pack()

# root.protocol("WM_DELETE_WINDOW", root.quit())

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()
