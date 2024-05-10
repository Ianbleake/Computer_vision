import numpy as np
import cv2 # as cv


"""
#DibujarImagen
img= np.zeros((600,600,3),np.uint8)
[M,N,L]=img.shape
X=M//2
Y=N//2
cv2.line(img,(0,X),(M,X),(29,9,99),5)#Dibuja una linea de esquina a horizontal
cv2.line(img,(X,0),(X,N),(29,9,99),5)#Dibuja una linea horizontal
cv2.rectangle(img,(200,200),(400,400),(58,58,0),3)
cv2.circle(img,(300,300),100,(200,100,100),-1)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'Ivan',(240,450),font,2,(255,255,255))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() #cierra las ventanas al teclear algo
"""

"""
#leer imagen
A=cv2.imread("fotos_9\DSC_0237.JPG")#Direccion de la imagen
[M,N,L]=A.shape
res=cv.resize(A,(500,500))
cv2.imshow("Imagen",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
#Imagen cuadriculada
A=cv.imread("fotos_9\DSC_0237.JPG")#Direccion de la imagen
[M,N,L]=A.shape #(x,y,z)
X=M//2
Y=N//2
res=cv.resize(A,(500,500))

for x in range(0,M,25):
    cv.line(res,(x,0),(x,N),(255,255,255),2)
for y in range(0,N,25):
    cv.line(res,(0,y),(M,y),(255,255,255),2)
cv.imshow("Imagen",res)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('Resultados\Cuadricula.jpg',res) #Guardar la imagen
"""

"""
#Rotar Imagenes
C = cv2.imread("fotos_9\DSC_0237.JPG")
M,N,L = C.shape

#Transpuesta
D = np.zeros((M,N,3), np.uint8)

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



cv2.imshow('Original', R)
cv2.imshow('Traspuesta', R1)
cv2.imshow('90Grados', R2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Resultados\Original.jpg',R)
cv2.imwrite('Resultados\Traspuesta.jpg',R1)
cv2.imwrite('Resultados\90.jpg',R2)
"""

"""
#Suma
C = cv2.imread("fotos_9\DSC_0237.JPG")
M,N,L = C.shape
C = np.zeros((M,N,3), np.uint8)

A = cv2.imread("fotos_9\DSC_0237.JPG")
B = cv2.imread("fotos_9\DSC_0239.JPG")

A = np.array(A,dtype=float)
B = np.array(B,dtype=float)
for k in range (0,L):
    for i in range (0,M):
        for j in range (0,N):
            C[i,j,k] = 0.4*A[i,j,k] + 0.4*B[i,j,k]
           
C = np.array(C,dtype=(np.uint8))

R = cv2.resize(C,(738,488))
cv2.imshow('Imagen', R)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Resultados\Suma.jpg',R)
"""

"""
#Resta
C = cv2.imread("fotos_9\DSC_0237.JPG")
M,N,L = C.shape
C = np.zeros((M,N,3), np.uint8)

A = cv2.imread("fotos_9\DSC_0237.JPG")
B = cv2.imread("fotos_9\DSC_0239.JPG")

A = np.array(A,dtype=float)
B = np.array(B,dtype=float)
for k in range (0,L):
    
    for i in range (0,M):
        
        for j in range (0,N):
            if(A[i,j,k] > B[i,j,k]):
                C[i,j,k] = A[i,j,k] - B[i,j,k]
            else:
                C[i,j,k] == 0
            
D = np.array(C,dtype=(np.uint8))

R = cv2.resize(D,(738,488))
cv2.imshow('Imagen', R)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Resultados\Resta.jpg',R)
"""

"""
#Multiplicacion
C = cv2.imread("fotos_9\DSC_0237.JPG")
M,N,L = C.shape
C = np.zeros((M,N,3), np.uint8)

A = cv2.imread("fotos_9\DSC_0237.JPG")
B = cv2.imread("fotos_9\DSC_0239.JPG")

A = np.array(A,dtype=float)
B = np.array(B,dtype=float)
for k in range (0,L):
    
    for i in range (0,M):
        
        for j in range (0,N):
            C[i,j,k] = (A[i,j,k] * B[i,j,k])/255
           
D = np.array(C,dtype=(np.uint8))

R = cv2.resize(D,(738,488))
cv2.imshow('Imagen', R)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Resultados\multiplicacion.jpg',R) #Guardar la imagen
"""

"""
#Extraccion RGB
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

cv2.imwrite('Azul.jpg',R)
cv2.imwrite('Verde.jpg',R1)
cv2.imwrite('Rojo.jpg',R2)
"""