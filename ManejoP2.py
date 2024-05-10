import numpy as np
import cv2 
import matplotlib as plt

"""
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
"""

"""
#En escala de Gris 
#E de G= 0.299*R + 0.587*R1 + 0.114*R2

A = cv2.imread("fotos_9\DSC_0237.JPG")
A = np.array(A,dtype=float)

M,N,L = A.shape

D=np.zeros((M,N,1),np.uint8)   #Se crea la nueva imagen
  
for i in range (0,M):
        
    for j in range (0,N):
        D[i,j,0] = 0.299*A[i,j,0] + 0.587*A[i,j,1] +0.114*A[i,j,2]
        
R2 = cv2.resize(D,(738,488))

cv2.imshow('Gris', R2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
#Claridad de imagen
A = cv2.imread("fotos_9\DSC_0237.JPG")
A = np.array(A,dtype=float)

M,N,L = A.shape

D=np.zeros((M,N,1),np.uint8)

for i in range (0,M):
        
    for j in range (0,N):
        D[i,j,0] = 0.299*A[i,j,0] + 0.587*A[i,j,1] +0.114*A[i,j,2]

R = cv2.resize(D,(738,488)) #Imagen en escala de gris

#B=(R2/255)**5  #Se oscurece la imagen / Mientras mas alto el valor mas oscuro 
#B=(R/255)*5    #Se ilumina la imagen / Mientras mas alto el valor mas luminoso
B=((R/255)**5)*255    #Se modifica el contraste / [0<valor<1] la imagen se aclara, [valor>1] se obscurece / Funcion gamma nos permite cambiar la intencidad de los pixeles 

#cv2.imshow('Original', R)
cv2.imshow('Claridad', B)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""



#Contar en la imagen cuantas veces se repiten las intencidades 0,1...255 hacer un vector y graficar. (img original en gris)

A = cv2.imread("fotos_9\DSC_0237.JPG")
A = np.array(A,dtype=float)

M,N,L = A.shape

D=np.zeros((M,N,1),np.uint8)

for i in range (0,M):
        
    for j in range (0,N):
        D[i,j,0] = 0.299*A[i,j,0] + 0.587*A[i,j,1] +0.114*A[i,j,2]

R = cv2.resize(D,(738,488)) #Imagen en escala de gris

Contraste=[]

E=np.zeros((M,N,1),np.uint8)

for i in range(0,M):

    for j in range(0,N):
        nivel_gris = R[i, j]
        Contraste.append(nivel_gris)
        
Contraste== np.array(Contraste)

#Para graficar 
plt.hist(Contraste, bins=256, range=[0, 256], density=True, color='gray', alpha=0.7)
plt.title('Histograma de Niveles de Gris')
plt.xlabel('Nivel de Gris')
plt.ylabel('Frecuencia Normalizada')
plt.show()

"""
#escala de gris
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

imagen = cv.imread("fotos_9\DSC_0237.JPG")
resultante = cv.resize(imagen, (1024, 720))
[M, N, L] = resultante.shape

escalaGrises = np.zeros([M, N])
cv.imshow("Imagen original", resultante)
resultante = np.array(resultante, dtype=(float))
escalaGrises = np.array(escalaGrises, dtype=(float))
resultante = pow(resultante.astype(np.float64) / 255, 1) * 255

for x in range(M):
    for y in range(N):
        for z in range(L):
            escalaGrises[x, y] = resultante[x, y, 0] * 0.299 + resultante[x, y, 1] * 0.587 + resultante[x, y, 2] * 0.114

escalaGrises = np.array(escalaGrises, dtype=(np.uint8))
cv.imshow("Escala de grises", escalaGrises)
cv.waitKey(0)
cv.destroyAllWindows()

# Obtener valores de intensidad y comparar
intensidades = escalaGrises.flatten()  # Aplanar la matriz de intensidades
print("Valores de intensidad:", intensidades)

# Comparar los valores de intensidad (puedes utilizar cualquier métrica de comparación)
# Por ejemplo, imprimir el valor máximo y mínimo
print("Valor máximo de intensidad:", np.max(intensidades))
print("Valor mínimo de intensidad:", np.min(intensidades))

# También puedes calcular la media, la desviación estándar, etc.
print("Valor medio de intensidad:", np.mean(intensidades))
print("Desviación estándar de intensidad:", np.std(intensidades))

# Histograma de los valores de intensidad
plt.hist(intensidades, bins=256, range=(0, 256), density=True, color='gray', alpha=0.7)
plt.title('Histograma de Intensidades')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')
plt.show()
"""