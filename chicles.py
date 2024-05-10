import cv2
import numpy as np

A = cv2.imread("Grises\Chicles.jpeg")
A = np.array(A, dtype=float)
M, N, L = A.shape


D = np.zeros((M, N, 1), np.uint8)
B = np.zeros((M, N, 1), np.uint8)

# Convertir a escala de grises
for i in range(0, M):
    for j in range(0, N):
        D[i, j, 0] = 0.299 * A[i, j, 0] + 0.587 * A[i, j, 1] + 0.114 * A[i, j, 2]

R1 = cv2.resize(D, (738, 488))
cv2.imshow('Escala de grises', R1)


for i in range(0, M):
    for j in range(0, N - 1):
        if D[i, j] > 0 and D[i,j]<50 or D[i, j] > 130 and D[i,j]<155:
            B[i,j]=0
        else:
            B[i,j]=D[i,j]


R2 = cv2.resize(B, (738, 488))
cv2.imshow('Umbral', R2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Resultados\humbral.jpeg',R2)


