import cv2

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
#cap = cv2.VideoCapture('datasets/videos/professor.mp4')
cap = cv2.VideoCapture(0)

amostra = 1
numAmostras = 25
idFace = raw_input('Seu Nome:')

while(True):
	conectado, imagem = cap.read()
 	imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BRG2GRAY)
	facesDetectadas = face_cascadedetectMultiScale(imagemCinza,scaleFactor=1.5,minSize=(100,100))

	for (x,y,w,h) in faces:
		img = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow('frame',img)

	key = cv2.waitKey(1)   # fica monutorando teclas clicadas , 1 he milisegundos de espera
	if key == 27:  # aborta se for a tela ESC
		break

cap.release()
cv2.destroyAllWindows()



