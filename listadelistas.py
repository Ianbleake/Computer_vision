#lista de listas
#Cada elemento de la lista es otra lista de n elementos

#A=[[10,13],[18,22]]

#print(A)
#print(A[0][1]) #se accede a la lista
#print(type(A))
#print(len(A))

import numpy as np #se importa la libreria numpy para manejo de matrices
import cv2 #importa la libreria opencv para manejar imagenes como magtriz 3d

#print(np.ndim(A))

#A=np.zeros((2,2)) #np hace referencia a la biblioteca numpy y zeros es un metodo de esta bioblioteca que crea matrices (filas,columbas)
#print(A)

#print(np.ndim(A)) #nos dice las dimenciones de la matriz

"""
B=np.zeros((2,2,3),np.int32) #z(num matrices,profundidad),filas,columnas

B[0][0][0]=1
B[0][1][0]=1
B[1][0][0]=1
B[1][1][0]=1

B[0][0][1]=2
B[0][1][1]=2
B[1][0][1]=2
B[1][1][1]=2

B[0][0][0]=3
B[0][0][0]=3
B[0][0][0]=3
B[0][0][0]=3

print(B)

for z in range(3):
    for x in range(2):
        for y in range(2):
            print(B[x][y][z])
    print("\n")
"""

img= np.zeros((600,600,3),np.uint8)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

