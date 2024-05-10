import numpy as np
import cv2 

C = cv2.imread("fotos_9\DSC_0237.JPG")
M,N,L = C.shape

D = np.zeros((M,N,3), np.uint8)

#Transpuesta
for k in range (0,3):
    a = M-1
    for i in range (0,M):
        b = N-1
        for j in range (0,N):
            D[i,j,k] = C[a,b,k]
            b=b-1
        a=a-1

  
#90°

E = np.zeros((N,M,L), np.uint8)

for k in range (0,3):
    #a = M-1
    for i in range (0,M):
        #b = N-1
        for j in range (0,N):
            E[j,i,k] = C[i,j,k]
            #b=b-1
        #a=a-1
    
R = cv2.resize(C,(738,488))
R1 = cv2.resize(D,(738,488))
R2 = cv2.resize(E,(488,738))

cv2.imshow('Imagen', R)
cv2.imshow('Imagen1', R1)
cv2.imshow('Imagen2', R2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#270°
E = np.zeros((N,M,L), np.uint8)

for k in range (0,3):
    #a = M-1
    for i in range (0,M):
        #b = N-1
        for j in range (0,N):
            E[j,i,k] = C[i,j,k]
            #b=b-1
        #a=a-1
    
R = cv2.resize(C,(738,488))
#R1 = cv2.resize(D,(738,488))
R2 = cv2.resize(E,(488,738))

cv2.imshow('Imagen', R)
#cv2.imshow('Imagen1', R1)
cv2.imshow('Imagen2', R2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Suma
A = cv2.imread("DSC_0238.jpg")
B = cv2.imread("DSC_0240.jpg")

A = np.array(A,dtype=float)
B = np.array(B,dtype=float)
for k in range (0,L):
    for i in range (0,M):
        for j in range (0,N):
            C[i,j,k] = 0.1*A[i,j,k] + 0.1*B[i,j,k]
           
#C[x,y,z] = 0.4*A[x,y,z] + B[x,y,z]
C = np.array(C,dtype=(np.uint8))

R = cv2.resize(C,(738,488))
cv2.imshow('Imagen', R)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Resta
A = cv2.imread("DSC_0238.jpg")
B = cv2.imread("DSC_0240.jpg")

A = np.array(A,dtype=float)
B = np.array(B,dtype=float)
for k in range (0,L):
    
    for i in range (0,M):
        
        for j in range (0,N):
            if(A[i,j,k] > B[i,j,k]):
                D[i,j,k] = A[i,j,k] - B[i,j,k]
            else:
                D[i,j,k] == 0
            
D = np.array(D,dtype=(np.uint8))

R = cv2.resize(D,(738,488))
cv2.imshow('Imagen', R)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Multiplicacion
A = cv2.imread("gato.jpg")
B = cv2.imread("mapa.jpg")

A = np.array(A,dtype=float)
B = np.array(B,dtype=float)
for k in range (0,L):
    
    for i in range (0,M):
        
        for j in range (0,N):
            D[i,j,k] = (A[i,j,k] * B[i,j,k])/255
           
D = np.array(D,dtype=(np.uint8))

R = cv2.resize(D,(738,488))
cv2.imshow('Imagen', R)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('multiplicacion.jpg',C) #Guardar la imagen

"""