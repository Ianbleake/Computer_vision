#cadena="hola Alumnos de la Esime"

#print(cadena)
#print(cadena[5:10])
#print(cadena[10])
#print(cadena[5:])

#dir(cadena)
#print(len(cadena))

#help(cadena.capitalize)

#Ejercicio1
cadena="Angel"
medio=len(cadena)//2
ultimo=len(cadena)
inicio=cadena[0]
centro=cadena[medio]
fin=cadena[ultimo-1]
resultado=inicio+centro+fin

print(resultado)

#Ejercicio2
cadena="America"
cadena2="Japan"

medio=len(cadena)//2
ultimo=len(cadena)
inicio=cadena[0]
centro=cadena[medio]
fin=cadena[ultimo-1]
resultado=inicio+centro+fin
medio=len(cadena2)//2
ultimo=len(cadena2)
inicio=cadena2[0]
centro=cadena2[medio]
fin=cadena2[ultimo-1]
resultado2=inicio+centro+fin
print(resultado+resultado2)

#secuencias
b=[3,8,7,11,-1,-9,20,51,7,-1,3,11]
c=[8,2,28,17,2,50,32,21,100,99,20]

print(b)
print(c)
print(b[1])
b[2]=10
print(b)
type(b)
print(len(b))
b.append(500)
print(b)
