import numpy as np
import cv2 as cv

img= np.zeros((600,600,3),np.uint8)
[M,N,L]=img.shape
X=M//2
Y=N//2
cv.line(img,(0,X),(M,X),(29,9,99),5)#Dibuja una linea de esquina a horizontal
cv.line(img,(X,0),(X,N),(29,9,99),5)#Dibuja una linea horizontal
cv.rectangle(img,(200,200),(400,400),(58,58,0),3)
cv.circle(img,(300,300),100,(200,100,100),-1)
font=cv.FONT_HERSHEY_COMPLEX
cv.putText(img,'Ivan',(240,450),font,2,(255,255,255))
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows() #cierra las ventanas al teclear algo
"""
#leer imagen
A=cv.imread("fotos_9\DSC_0237.JPG")#Direccion de la imagen
[M,N,L]=A.shape
X=M//2
Y=N//2
res=cv.resize(A,(500,500))
for a in range(0,500,25):
    cv.line(A,(0,X),(M,X),(29,9,99),5)

cv.imshow("Imagen",res)
cv.waitKey(0)
cv.destroyAllWindows()
#Imagen cuadriculada
"""