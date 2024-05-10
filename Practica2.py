import numpy as np
import cv2 
import matplotlib as plt


#Obtencion RGB de Imagen
A = cv2.imread("fotos_9\DSC_0237.JPG")
A = np.array(A,dtype=float)

M,N,L = A.shape

B=np.zeros((M,N,3),np.uint8)
C=np.zeros((M,N,3),np.uint8)
D=np.zeros((M,N,3),np.uint8)
  
for i in range (0,M):
        
    for j in range (0,N):
        B[i,j,0] = A[i,j,0]
        C[i,j,1] = A[i,j,1]
        D[i,j,2] = A[i,j,2]
           

R = cv2.resize(B,(738,488))
R1 = cv2.resize(C,(738,488))
R2 = cv2.resize(D,(738,488))
cv2.imshow('Azul', R)
cv2.imshow('Verde', R1)
cv2.imshow('Rojo', R2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Resultados\Azul.jpg',R)
cv2.imwrite('Resultados\Verde.jpg',R1)
cv2.imwrite('Resultados\Rojo.jpg',R2)

