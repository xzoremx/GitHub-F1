#Coding...

x = (1, "a", 3, "c")
print(x)

print(type(x))

#x.append(1.5) # el atributo append no aplica para tuple's 

y = [1,2,3]

print(y)

print(type(y))

y.append('b')

print(y)

#Explorando la lista "Y"

#Primero usando for<

for item in y:
    print(item)

#Segundo usando while

i = 0
while (i != len(y)):
    print(y[i])
    i +=1

#verificando la presencia de un elemento en la tupla o lista

if (10 in y):
    print("Si está")
else:
    print("No está")

#That's very sick!!!!

###################################################

#Tecnica BroadCasting


#Rebanar - listas/strings

string = 'Esto es un string'

#Rebanamos la primera letra!

print(string[0])

#Rebanamos la ultima letra!

print(string[-1])

####################################################

#Ahora por rangos

#Las letras en la 4ta y 3era ultima posicion

print(string[-4:-2])

    #Funciona como el primero es cerrado y el otro abierto

#Recuerda que una lista o String comienza del <<CERO>>

#Imprimiendo la primera palabra "Esto"

print(string[0:4])

#Imprimiendo el resto del String

print(string[4:])

######################################

#Ejercicio

#Obtener 'Christopher'

x = 'Dr. Christopher Brooks'

print(x[4:15])

#Reconrdar que comienza en 0 y se al regresar en -1

###############################################################

# Strings!

Nombre_1 = "Renato"
Nombre_2 = "Noe"

Apellido_1 = "Huamani"
Apellido_2 = "Poma"

#Imprimiendo el nombre completo

print(Nombre_1 + ' ' + Nombre_2 + ' ' + Apellido_1 + ' ' + Apellido_2)

Completo = Nombre_1 + ' ' + Nombre_2 + ' ' + Apellido_1 + ' ' + Apellido_2

#Multiplicacion

print(Nombre_1 * 3)

#Analizar los elementos presentes

print('R' in Nombre_1)

###############################################

#Pero a partir de una nombre completo es posible obtener los nombres y apellidos por separado

#Split

N_1 = Completo.split(' ')[0]
	
print(N_1)

A_1 = Completo.split(' ')[-2]

print(A_1)

#Type

print(type(Completo))

#################################

#Diccionarios -> {}

#No cuentan con un orden en especifico por lo tanto es necesario 
#una clave

from statistics import correlation
from unicodedata import name


D = {'correo' :'a20196546@pucp.edu.pe', 'apodo' : 'zorem'}
print(D['correo'])

#Llamando a los valores 

for name in D:
    print(D[name])
for correo_apodo in D:
    print(D[correo_apodo])


#Asignando los valores - Diccionario

F = {'Renato', 'zorem', 'a20196546@pucp.edu.pe'}
Nombre_1, Apodo_1, Email = F

print(Nombre_1)
print(Apodo_1)
print(Email)
print(F)
































 