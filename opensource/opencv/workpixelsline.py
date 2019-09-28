import cv2

#captura imagem colorida
imagem = cv2.imread("datasets/fotos/reuniao-professores.jpeg")

print imagem.shape
# Imagem em BRG ( de 0 a 2 )
#      Canal Vermelho 2 , Canal Verde 1    , Canal Azul 0 
print imagem.item(0,0,2),imagem.item(0,0,1),imagem.item(0,0,0)

alturaImagem =  imagem.shape[0]

# Adiconando linha na cor vermelha com 1 pixel de largura
posicaopixel = 0
while ( posicaopixel < alturaImagem ):
	imagem.itemset((posicaopixel,0,2),255)
	imagem.itemset((posicaopixel,0,1),0)
	imagem.itemset((posicaopixel,0,0),0)
	posicaopixel= posicaopixel+1
  
cv2.imwrite("results/imagemvermelha.jpeg",imagem)

