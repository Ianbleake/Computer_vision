#No es secuencias
#secuencia python
"""
b=[3,8,7,11,-1,-9,20,51,7,-1,3,11]
c=[8,2,28,117,2,50,32,21,100,99,20]
a=set(b) #?
print("A:",a)
a=set(c)
print("A:",a)
m=(3,8,10,11,-1,-9,20,51,7,-1,3,11)
print("M:",m)
print("M1:",m[1])
print("Tipo m:",type(m)) #?
print("Tipo a:",type(a)) #?
"""
#trabajando una secuencia

l1=list(range(2,21,2))#range(inicio,fin,incremento)
"""
print("L1",l1)
print(l1[-1])#en el indexado un indice negativo implica indexar del final al principio/ en slicing [:-x] implica eliminar el elemento
"""
#metodos insert,append,
"""
print("L1: ",l1)
l1.insert(5,30) #insert(indice,valor) inserta un valoir en una posicion determinada
print("L1 agregando 30: ",l1)

l1.append(1)#append(valor) agrega un valor al final de la lista
print("L1 agregando 1: ",l1)

l1.sort()#ordena la lista
print("L1 ordenada: ",l1)

print("L1: ",l1)
milista=l1[1:5]
print("Mi lista: ",milista)

del milista[0:2] 
print("Mi lista: ",milista)

milista2=l1[:]
print("Mi lista2: ",milista2)

milista2.reverse()
print("Mi lista2: ",milista2)
"""
#Ciclos For

for x in range(20):#range(valor final) cuando range recive un valor va de 0 al valor de uno en uno/ For X esta es la variable de control
    print(x, end=" ")
    #este for va de 0 a 20
print("\n")
for x in range(1,20):
    print(x, end=" ")
print("\n")
for x in range(1,20,2):
    print(x, end=" ")

b=[3,8,7,11,-1,-9,20,51,7,-1,3,11]
print("\n")
for x in b: #recorre la lista
    print(x, end=" ")
