#Funciones de Aclarado y Obscurecimiento de Imagenes

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("fotos_9\DSC_0237.JPG")
img_res = cv2.resize(img, (1024, 720))
img = np.array(img_res, dtype=np.uint8)
M, N, L = img.shape

img = np.array(img, dtype=float)

C = np.zeros((M, N, L), dtype=float)
D = np.zeros((M, N, L), dtype=float)

gamma = 2

# Aplicar corrección gamma
for i in range(M):
    for j in range(N):
        C[i, j] = img[i, j, 0] * 0.114 + img[i, j, 1] * 0.587 + img[i, j, 2] * 0.299
        D[i, j] = pow(C[i, j] / 255, gamma) * 255

img = np.array(img, dtype=np.uint8)
C = np.array(C, dtype=np.uint8)
D = np.array(D, dtype=np.uint8)

# Mostrar imágenes
cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Escala de Grises", C)
cv2.imshow("Imagen Gamma", D)
cv2.imwrite("Resultados/Gama.jpg", D)

# Calcular y mostrar histograma 
plt.hist(D.ravel(), 256, [0, 256])
plt.title("Histograma de la Imagen gamma")
plt.xlabel("Valor de Píxel")
plt.ylabel("Frecuencia")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
