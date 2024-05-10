#ciclo for
"""
for x in range(1,11):
    if x%2==0:
        print(x, "es par")
    else:
        print(x)
print("Fin del ciclo")
print("fin del programa")
"""      
#ciclo while
"""
a=input("Ingrese un valor mayor que 10: ")
a=int (a) #define el tipo de la variable a como entero
while(a<10):
    print("El valor no es mayor a 10: ")
    a=input("Ingrese un valor mayor que 10")
    a=int (a)
else:
    print("El valor es mayor a 10")
print("salimos del ciclo")
print("el valor es: ",a," y es tipo: ",type(a))
"""
#Diccionarios
#sintaxis de un diccionario: nombredic('llave':valor,'llave':valor...)
# el metodo .keys() te da las llaves de un diccionario, debe ser asignado a una variable para visualizarlo
"""
NumerosTelefono={'jefe':5556581111,'jesus':5522599770} #diccionario
A=NumerosTelefono.keys()
print(A)
print(NumerosTelefono['jefe']) #aqui se hace uso del diccionario para obtener el valor correspondiente a la llave dada.
#imprimir la llave con su valor
for key in NumerosTelefono.keys():
    print(key,"-->",NumerosTelefono[key])
#metodo items: retorna una lista de tuplas(?) donde cada tupla es un par de cada llave con su valor
#tuplas:par de datos
print(NumerosTelefono.items())

#agregar pares a un diccionario metodo .update()
NumerosTelefono.update({"Jafeth":5557296000})
NumerosTelefono.update({"Ivan":5512182737})
print(NumerosTelefono.items())

#eliminar una clave, esto elimina tambien su valor
print(len(NumerosTelefono))
del NumerosTelefono['Jafeth']
print(NumerosTelefono.items())
print(len(NumerosTelefono))
"""

#Funciones: se definen con def namefuncion(parametros):
"""
def mifuncion(): #si no tiene parametros se deja vacio en lugar de poner void
    print("Hola mundo")

#def factorial(x=1) asi definimos un valor al parametro para los casos donde no llegue un valor, esto no afecta el valor que si llega ya que se sobreescribe
def factorial(x: int): #x: int define que el valor recibido sera un entero obligatoriamente (el tipo del parametro no es obligatorio)
    b=1
    for a in range(1,x+1): # ya que range solo el limite del rango de la forma final-1, osea no llega al valor que damos, se queda uno antes, se suma uno para que si llegue al valor que queremos
        b*=a
    return b

print(factorial(5))
"""

def menor(V):

    menor=V[0]

    for x in V: #Recordar que en python for tambien recorre listas sin ir posicion por posicion/ Aqui le digo a for que recorra la lista V y x=almacena el valor en cada posicion una por una
        if (menor>x):
            menor=x
    
    return menor


b=[1,2,6,4,8,5,9,44,8,3,9,0,4,2,7,9,4,5,8,5,3,2,9,0,9,8,-9]
print(b)
print("El menor es: ",menor(b))


