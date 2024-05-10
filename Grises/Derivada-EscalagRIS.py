import cv2
import numpy as np

A = cv2.imread("Grises\Chicles.jpeg")
A = np.array(A, dtype=float)
M, N, L = A.shape

D = np.zeros((M, N, 1), np.uint8)
B = np.zeros((M, N, 1), np.uint8)
C = np.zeros((M, N, 1), np.uint8)
Ey = np.zeros((M, N, 1), np.uint8)  # Primera derivada en y
Fy = np.zeros((M, N, 1), np.uint8)  # Segunda derivada en y

# Convertir a escala de grises
for i in range(0, M):
    for j in range(0, N):
        D[i, j, 0] = 0.299 * A[i, j, 0] + 0.587 * A[i, j, 1] + 0.114 * A[i, j, 2]

# Primera derivada para x
for i in range(0, M):
    for j in range(0, N - 1):
        if D[i, j - 2] > D[i, j]:
            B[i, j] = D[i, j - 2] - D[i, j]
        else:
            B[i, j] = 0

# Segunda derivada para x
for i in range(0, M):
    for j in range(1, N - 1):
        C[i, j] = D[i, j - 1] - 2 * D[i, j] + D[i, j + 1]

# Primera derivada para y
for i in range(0, M - 1):
    for j in range(0, N):
        if D[i - 2, j] > D[i, j]:
            Ey[i, j] = D[i - 2, j] - D[i, j]
        else:
            Ey[i, j] = 0

# Segunda derivada para y
for i in range(1, M - 1):
    for j in range(0, N):
        Fy[i, j] = D[i - 1, j] - 2 * D[i, j] + D[i + 1, j]

R = cv2.resize(D, (738, 488))
R1 = cv2.resize(B, (738, 488))
R2 = cv2.resize(C, (738, 488))
R3 = cv2.resize(Ey, (738, 488))
R4 = cv2.resize(Fy, (738, 488))

cv2.imshow('Escala de grises', R)
cv2.imshow('Derivada(x)', R1)
cv2.imshow('Segunda Derivada(x)', R2)
cv2.imshow('Derivada(y)', R3)
cv2.imshow('Segunda Derivada(y)', R4)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Resultados\Derivada_x.jpg', R1)
cv2.imwrite('Resultados\Derivada2_x.jpg', R2)
cv2.imwrite('Resultados\Derivada_y.jpg', R3)
cv2.imwrite('Resultados\Derivada2_y.jpg', R4)

#la primera derivada funciona para detectar bordes, la segunda detecta todavia mas bordes