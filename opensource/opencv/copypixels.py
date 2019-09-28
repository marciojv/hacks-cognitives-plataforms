import cv2

#captura imagem colorida
imagem = cv2.imread("datasets/fotos/reuniao-professores.jpeg")

print imagem.shape
# Imagem em BRG ( de 0 a 2 )
#      Canal Vermelho 2 , Canal Verde 1    , Canal Azul 0 
print imagem.item(0,0,2),imagem.item(0,0,1),imagem.item(0,0,0)
                         
regiaoInteresse = imagem[550:1050,0:350] 
# grava recorte de imagem chamada de regiao de interesse
cv2.imwrite("results/regiaoInteresse.jpeg",regiaoInteresse)

# A imagem recortada tera 500px de Altura ( 1050 - 550) e 350 de largura 
imagem[0:500, 0:350] = regiaoInteresse
cv2.imwrite("results/duplicado.jpeg",imagem)

