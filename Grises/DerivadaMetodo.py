import cv2
import numpy as np

A = cv2.imread("Grises\Micro2.jpg")
M, N, L = A.shape

D = np.zeros((M, N, 1), np.uint8)
B = np.zeros((M, N, 1), np.uint8)

# Convertir a escala de grises directamente
D = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)

# Primera derivada
B = cv2.Sobel(D, cv2.CV_64F, 1, 0, ksize=3)

# Segunda derivada usando Laplacian
C = cv2.Laplacian(D, cv2.CV_64F)

R = cv2.resize(D, (738, 488))
R1 = cv2.resize(B, (738, 488))
R2 = cv2.resize(C, (738, 488))
cv2.imshow('Escala de grises', R)
cv2.imshow('Derivada', R1)
cv2.imshow('Segunda Derivada', R2)
cv2.waitKey(0)
cv2.destroyAllWindows()
