import numpy as np
import cv2
import matplotlib.pyplot as plt
#from PIL import Image

A = cv2.imread("fotos_9\DSC_0237.JPG")
[M, N, L] = A.shape
C=np.zeros((M,N),np.uint8)
D=np.zeros((M,N,1),float)   

for i in range (0,M):  
    for j in range (0,N):
        D[i,j,0] = 0.299*A[i,j,0] + 0.587*A[i,j,1] +0.114*A[i,j,2]

D = np.array(D,dtype=(np.uint8))

intensidades = D.flatten()
# Calcular la probabilidad de cada nivel de intensidad
hist, bins = np.histogram(D.flatten(), bins=256, range=[0, 256])
probabilidad = hist / hist.sum()
#print(hist)
#print(probabilidad)
varianzas = []
# Calcular la varianza entre clases para cada posible umbral
for t in range(1, 256):
    w0 = probabilidad[:t].sum()
    w1 = probabilidad[t:].sum()

    mu0 = np.sum(np.arange(t) * probabilidad[:t]) / w0 if w0 > 0 else 0
    mu1 = np.sum(np.arange(t, 256) * probabilidad[t:]) / w1 if w1 > 0 else 0

    varianza_entre_clases = w0 * w1 * ((mu0 - mu1) ** 2)
    varianzas.append(varianza_entre_clases)
# Encontrar el umbral que maximiza la varianza entre clases
umbral = np.argmax(varianzas)

for i in range (0,M):
    for j in range (0,N):
        if(D[i,j]>umbral):
             C[i,j] = D[i,j]
        else:
            C[i,j] = 0

R = cv2.resize(D,(738,488))
cv2.imshow('Escala', R)
R1 = cv2.resize(C,(738,488))
cv2.imshow('Calidad', R1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Resultados/Escala.jpg", R)
cv2.imwrite("Resultados/Calidad.jpg", R1)
