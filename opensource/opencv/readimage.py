import cv2

#captura imagem do disco e mostra colorido 
# o defaulthe colorido caso nao informado 
imagem = cv2.imread("datasets/fotos/reuniao-professores.jpeg",1)
cv2.imshow("Mostra Imagem Colorida",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()


#captura imagem do disco e mostra em cinza 
imagem = cv2.imread("datasets/fotos/reuniao-professores.jpeg",0)
cv2.imshow("Mostra Imagem em Cinza",imagem)
cv2.waitKey(0)



cv2.destroyAllWindows()

