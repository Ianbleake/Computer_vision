#Clases, (self), Programación Orientada a Objetos
#Viernes 29 de septiembre
"""
class Complejo():
    def __init__(self,a:int,b:int):
        self.R=a
        self.I=b

    def Imprime(self):
        if(self.I>0):
            if(self==1):
                return(f"{self.R}+1")
            else:
                return(f"{self.R}+{self.I}i")
        else:
            return()

    def Leer(self):
        self.R=input("Ingrese la parte Real")
        self.I=input("Ingrese la parte imaginaria")
    
    @classmethod
    def Inicia(cls, a:int):
        return(Complejo(a,a))

    def __add__(self, A):
        return(Complejo(self.R+A.R, self.I+A.I))
    
    def __str__(self):
        if(self.I==0):
            return(f"{self.R}")
        
        else:
            if(self.I>0):
                if(self.I==1):
                    return(f"{self.R}+i")
                else:
                    return(f"{self.R}+{self.I}i")
                
            else:
                return(f"{self.R}{self.I}i")
    
A=Complejo.Inicia(1)
A.Imprime()
print(A)


B=Complejo(3,1)
C=Complejo()
print(B)
print(C)
"""

#lista de listas
#Cada elemento de la lista es otra lista de n elementos

#A=[[10,13],[18,22]]

#print(A[0][1]) #se accede a la lista
#print(type(A))
#print(len(A))

import numpy as np #se importa la libreria numpy para manejo de matrices

#print(np.ndim(A))

B=np.zeros((2,3,3),np.int32)

B[0][0][1]=2
B[0,1,1]=2
print(B)