import cv2
import numpy as np

A = cv2.imread("Grises\micro2.jpg")
A = np.array(A,dtype=float)
M,N,L = A.shape

D=np.zeros((M,N,1),float)   

for i in range (0,M):
        
    for j in range (0,N):
        D[i,j,0] = 0.299*A[i,j,0] + 0.587*A[i,j,1] +0.114*A[i,j,2]
        
FalsoColor = np.zeros((M, N, L), dtype=float)

for i in range(M):
    for j in range(N):
         #if(D[i, j, 0]>60 and D[i, j, 0]<99):
            FalsoColor[i, j, 0] = 0.9* D[i, j, 0]
            FalsoColor[i, j, 1] = 2.2* D[i, j, 0]
            FalsoColor[i, j, 2] = 1.8* D[i, j, 0]


D = np.array(D,dtype=(np.uint8))
FalsoColor = np.array(FalsoColor,dtype=(np.uint8))

R = cv2.resize(D,(738,488))
R1 = cv2.resize(FalsoColor,(738,488))
cv2.imshow('Escala de grises', R)
cv2.imshow('Falso Color', R1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('FalsoColor.jpg',FalsoColor)

