import cv2

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

amostra = 1
numAmostras = 25
id = raw_input('Seu Nome:')
largura, altura = 220,220 # padronizacao do tamanho das imagens

print "Capturando Faces..."

while(True):
	conectado, imagem = cap.read()
 	imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(imagemCinza,scaleFactor=1.5,minSize=(150,150))

	for (x,y,l,a) in faces:
		cv2.rectangle(imagem,(x,y),(x+l,y+a),(255,0,0),2)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura,altura))
			cv2.imwrite("results/alunos/aluno."+str(id)+"."+str(amostra)+".jpg",imagemFace)
			print ("foto " + str(amostra) + " capturada")
			amostra += 1

	cv2.imshow('Face',imagem)
	cv2.waitKey(1)
	if (amostra >= numAmostras +1):
		break

cap.release()
cv2.destroyAllWindows()



