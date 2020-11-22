# oka exec get faces
import cv2
import dlib
import os
import sys
import sqlite3

#cam = cv2.VideoCapture(1)
detector = dlib.get_frontal_face_detector()
##############################################################################

fileName = "/media/chester/393955402E88C1D1/Autoattendance-Cognitive/pics/test1.jpg"
# recive un arg que sera la imagen con la que se probara
# if len(sys.argv) is not 1:
# 	img = cv2.imread(str(sys.argv[1]))
# 	dets = detector(img, 1)
# 	if not os.path.exists('./Cropped_faces'):
# 		os.makedirs('./Cropped_faces')
# 	print("detected = " + str(len(dets)))
# 	# escribe las caras detectadas
# 	for i, d in enumerate(dets):
# 		cv2.imwrite(f'./Cropped_faces/face{str(i + 1)}.jpg', img[d.top():d.bottom(), d.left():d.right()])



img = cv2.imread(fileName)
dets = detector(img, 1)
if not os.path.exists('./Cropped_faces'):
	os.makedirs('./Cropped_faces')
print("detected = " + str(len(dets)))
# escribe las caras detectadas
for i, d in enumerate(dets):
	cv2.imwrite(f'./Cropped_faces/face{str(i + 1)}.jpg', img[d.top():d.bottom(), d.left():d.right()])
