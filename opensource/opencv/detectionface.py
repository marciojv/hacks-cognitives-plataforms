import numpy as np #importa bibliotaca numpy e renomaia para np
import cv2         # importa biblioteca OpenCV 

#Use este para entrada via WebCam
#cap = cv2.VideoCapture(0) # Captura como entrada Video da Camera Principal do Computador

#cap = cv2.VideoCapture('datasets/videos/hack-linx.mp4')
cap = cv2.VideoCapture('datasets/videos/torvalds.mp4')

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

while(True):
	_, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 5) # 1.3 e a velocidade de captura 
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow('frame',frame)

	key = cv2.waitKey(1)   # fica monutorando teclas clicadas , 1 he milisegundos de espera
	if key == 27:  # aborta se for a tela ESC
		break

cap.release()
cv2.destroyAllWindows()
