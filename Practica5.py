import cv2
import numpy as np

A = cv2.imread("fotos_9\DSC_0237.JPG")
A = np.array(A,dtype=float)

M,N,L = A.shape

D=np.zeros((M,N,1),np.uint8)   #Se crea la nueva imagen
  
for i in range (0,M):
        
    for j in range (0,N):
        D[i,j,0] = 0.299*A[i,j,0] + 0.587*A[i,j,1] +0.114*A[i,j,2]
        

imagen_gris = cv2.resize(D,(738,488))

alto, ancho = imagen_gris.shape

imagen_color = np.zeros((alto, ancho, 3), dtype=np.uint8)

for i in range(alto):
    for j in range(ancho):
        intensidad_gris = imagen_gris[i, j]

        imagen_color[i, j, 0] = min(255, 4 * intensidad_gris) 
        imagen_color[i, j, 1] = min(255, 6 * (255 - intensidad_gris)) 
        imagen_color[i, j, 2] = min(255, 2 * intensidad_gris)  

cv2.imshow('Imagen en Gris', imagen_gris)
cv2.imshow('Imagen con Falso Color', imagen_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Resultados\FalsoColor.jpg',imagen_color)

