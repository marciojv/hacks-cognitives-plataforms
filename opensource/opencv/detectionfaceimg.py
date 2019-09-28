import cv2         # importa biblioteca OpenCV 

imagem = cv2.imread('datasets/fotos/reuniao-professores.jpeg')

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5) # 1.3 e a velocidade de captura 
for (x,y,w,h) in faces:
	img = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('frame',img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
