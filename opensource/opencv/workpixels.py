import cv2

#captura imagem colorida
imagem = cv2.imread("datasets/fotos/reuniao-professores.jpeg")

print imagem.shape
# imagem em BRG ( de 0 a 2 )
     # Canal Vermelho 2 , Canal Verde 1    , Canal Azul 0 
print imagem.item(0,0,2),imagem.item(0,0,1),imagem.item(0,0,0)

print imagem.shape[0]

#imagem.itemset((0,0,2),255)
#imagem.itemset((0,0,1),0)
#imagem.itemset((0,0,0),0)



#posicaopixel = 0
#for posicaopixel <= imagem.item(0,0,2)
  


#cv2.imwrite("results/imagemvermelha.jpeg",imagem)

