import cv2
import numpy as np

imagen = cv2.imread('fotos_9\DSC_0237.JPG')
res_imagen = cv2.resize(imagen, (1024, 720))
imagen = np.array(res_imagen, dtype=np.uint8)  
M, N, L = imagen.shape

cv2.imshow("Original", imagen)

### IDENTIDAD ###

def iD():
    imgI = np.zeros((M, N, L), dtype=np.uint8)

    for i in range(M):
        for j in range(N):
            imgI[i, j] = imagen[i, j]

    cv2.imshow("Identidad", imgI)
    cv2.imwrite("Resultados/identidad.jpg", imgI)


###INVERSO NEGATIVO###

def iN(): 
    imgN = np.zeros((M, N, L), dtype=np.uint8)

    for i in range(M):
        for j in range(N):
            imgN[i, j] = 255 - imagen[i, j]

    cv2.imshow("Inverso Negativo", imgN)
    cv2.imwrite("Resultados\InversoNegativo.jpg", imgN)



###UMBRAL###
def iU():
    imgU = np.zeros((M, N, L), dtype=np.uint8)

    p1 = 40  # La visualización de la imagen es proporcional a p1 y p2
    p2 = 110

    for i in range(M):
        for j in range(N):
            if (imagen[i, j, 1] <= p1 or imagen[i, j, 1] >= p2):
                imgU[i, j] = 255
            else:
                imgU[i, j] = 0

    cv2.imshow("Umbral", imgU)
    cv2.imwrite("Resultados/umbral.jpg", imgU)


### UMBRAL BINARIO ###

def iUB():
    imgUB = np.zeros((M, N, L), dtype=np.uint8)

    p1 = 40 
    p2 = 110

    for i in range(M):
        for j in range(N):
            if (imagen[i, j, 1] < p1 or imagen[i, j, 1] >= p2):
                imgUB[i, j] = 255
            else:
                imgUB[i, j] = 0

    cv2.imshow("Umbral Binario", imgUB)
    cv2.imwrite("Resultados/umbralBinario.jpg", imgUB)



###UMBRAL BINARIO INVERTIDO###

def iUBI():
    imgBI = np.zeros((M, N, L), dtype=np.uint8)

    p1 = 40  # La visualización de la imagen es proporcional a p1 y p2
    p2 = 110

    for i in range(M):
        for j in range(N):
            if (imagen[i, j, 1] <= p1 or imagen[i, j, 1] >= p2):
                imgBI[i, j] = 0
            else:
                imgBI[i, j] = 255

    cv2.imshow("Umbral Binario Invertido", imgBI)
    cv2.imwrite("Resultados/umbralInvertido.jpg", imgBI)



### UMBRAL ESCALA DE GRISES ###

def iUEG(): 
    imgUEG = np.zeros((M, N, L), dtype=np.uint8)

    P1 = 40
    P2 = 110

    for i in range(M):
        for j in range(N):
            if (imagen[i, j, 1] <= P1 or imagen[i, j, 1] >= P2):
                imgUEG[i, j] = 255
            else:
                imgUEG[i, j] = imagen[i, j, 1]

    cv2.imshow("Umbral Escala de Grises", imgUEG)
    cv2.imwrite("Resultados/umbralGris.jpg", imgUEG)


###UMBRAL ESCALA A GRISES INVERTIDO###

def iUIEGI():
    imgUEGI = np.zeros((M, N, L), dtype=np.uint8)

    P1 = 40
    P2 = 110

    for i in range(M):
        for j in range(N):
            if (imagen[i, j, 1] <= P1 or imagen[i, j, 1] >= P2):
                imgUEGI[i, j] = 255
            else:
                imgUEGI[i, j] = 255 - imagen[i, j, 1]

    cv2.imshow("Umbral Escala Grises Invertido", imgUEGI)
    cv2.imwrite("Resultados/umbralInvertidoGris.jpeg", imgUEGI)


iD()
iN()
iU()
iUB()
iUBI()
iUEG()
iUIEGI()
cv2.waitKey(0)
cv2.destroyAllWindows()

