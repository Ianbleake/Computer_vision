#Ejemplo 14 de septimbre del 2023
"""cadena="Hola alumnos de la ESIME"
print(cadena)
print(cadena[5:10])
print(cadena[10])
print(cadena[5:])

dir (cadena)

print(len(cadena))        //Largo de la cadena
help(cadena.capitalize)   //Ayuda"""

#Ejericio 1
"""cadena="Diego"
A=len(cadena)
B=int(A/2)
print(cadena[0],cadena[B],cadena[A-1])"""

#Ejericio 2
"""s1="America"
s2="Japan"
A1=len(s1)
A12=int(A1/2)
print(s1[0],s2[0],s1[A12],s2[2:])"""

#Secuencias en Python
"""b= [3,8,7,11,-1,-9,20,51,7,-1,3,11]   #Es una secuencia
c= [8,2,28,17,2,50,32,21,100,99,20]   

print(b)
print(c)
print(b[1])
b[2]=10
print(b)
type(b)
print(len(b))
b.append(500)  #Agrega el 500 en la secuencia b#
print(b)"""


#Martes 19 de septiembre
"""b=[3,8,7,11,-1,-9,20,51,7,-1,3,11]
c=[8,2,28,17,2,50,32,21,100,99,20]
a=set(b)
print(a)

a=set(c)
print(a)
m=(3,8,10,11,-1,-9,20,51,7,-1,3,11)
print(m)
print(m[1])
type(m)
#type(a)"""

#Listas
"""l1=list(range(2,21,2))
print(l1)

print (l1[5])

print(l1)
l1.insert(5,30)  #Inserta el numero 30 en la posición 5
print(l1)

l1.append(1)   #Es para agregar al final
print(l1)

l1.sort()   #Es para ordenar la lista
print(l1)
#help (l1.sort)  //Ayuda

#Secciones de una lista
print(l1)
milista=l1[1:5]  #Hace una nueva lista con los numero del 1 al 4  de la lista anterior
print(milista) 

del milista[0:2]  #Elimino de mi nueva lista
print(milista)

milista2=l1[:]   #Se crea una nueva lista con todos los elementos de la primera lista
print(milista2)

#milista3=milista2.reverse
milista2.reverse()   #La lista al revés 
print(milista2) """

#Ciclos for
""" for x in range (20):
    print(x, end=" ") #Para que salga en forma horizontal
    
for x in range (1,20):

    print (x, end=" ")

for x in range (1,20,2):  #Valor donde inicia, donde termina y el incremento

    print(x, end=" ") """

"""b=[3,8,7,11,-1,-9,20,51,7,-1,3,11]
for x in b:
    print(x, end=" ")"""


#Jueves 21 de septiembre del 2023

#Ciclo For
"""for  x in range (1,21):
    if x%2==0:
        print(x,"Es par")
    else:
        print(x)
    print("Fin del ciclo")
    print("Fin del programa")"""

#Ciclo While
"""a=input("Teclee un valor mayor que 10: ")
a=int (a)
while(a<10):
    print("El valor no es mayor que 10")
    a=input("Teclee nuevamente el valor; mayor a 10: ")
    a=int (a)
else:
    print("El valor es mayor a 10")
    print("Salimos del ciclo")
    print("El valor es: ",a, "y es de tipo: ", type(a))"""
    
    
#Diccionarios 

"""NumerosTelefono={"Jefe": 55565242432, "Jesus": 55527378282}

A=NumerosTelefono.keys()       #Método KEYS recuerda toda las listas del diccionarios
print(A)
print(NumerosTelefono["Jefe"])

for key in NumerosTelefono.keys():
    print (key, "->", NumerosTelefono[key])"""

#Método items: Retorna una lista de tuplas, donde cada tupla es un par de cada clave con su valor

"""print(NumerosTelefono.items())"""

#Método updata: Se agrega la llave y el valor

"""NumerosTelefono.update({"Jafeth": 51414151})
NumerosTelefono.update({"Diego": 5514512854})
print(NumerosTelefono.items())"""

#Eliminar Claves 

"""print (len(NumerosTelefono))
del NumerosTelefono["Jafeth"]
print(NumerosTelefono.items())
print(len(NumerosTelefono))"""


#Funciones: Es un bloque de sentenicas que se ejecutan 

"""def MiFuncion():
    print("Hola mundo")
    
MiFuncion()"""

"""def factorial (x: int):        #Factorial
    b=1
    for a in range (1,x+1):
        b*=a
    return b

print (factorial(5))"""

"""def factorial (x: int):        #Factorial por si no hay ningún valor
    b=1
    for a in range (1,x+1):
        b=b*a;
    return b

print (factorial()) """


