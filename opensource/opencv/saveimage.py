import cv2

#captura imagem em cinza
imagem = cv2.imread("datasets/fotos/reuniao-professores.jpeg",0)
cv2.imshow("Mostra em Cinza",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Salva o arquivo na pasta results no mesmo diretorio corrente ( deve ser ciado o diretorio) 
cv2.imwrite("results/imagemCinza.jpeg",imagem)

