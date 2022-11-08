#Aprendiendo! - Cambio 9:34 am

import numpy as np

from PIL import Image

from IPython.display import display

import matplotlib.pyplot as plt

import matplotlib.image as mpimg



foto_pike = Image.open('pike.png')

#foto_pike.show()

formacion = np.array(foto_pike)

print(formacion.shape)

print(formacion)


mascara = np.full(formacion.shape, 255)

foto_modificada = formacion - mascara

foto_modificada = foto_modificada * -1

print(foto_modificada.dtype)

#Image.fromarray(foto_modificada).show()

#foto_modf_tamaño = np.reshape(foto_modificada, (990,600))

#Image.fromarray(foto_modf_tamaño).show()

########################################################

    #Index

a = np.array([4,5,6])

print(a[0])

b = np.array([[4,5,6], 
             [3,4,6]])

print(b[1,0])

#El primer index es la fila (1, recordar de que comienza en 0) y la siguiente es la columna (cero)

print(a[a>5])
#Mostrando los elementos que cumplen ciertas condiciones en cada formacion!
print(b[b>3])

print(b[:1, 1:2]) #Imprimiendo solo parte de la formacion \ primero fila -> luego columna - Usando rangos!

a = np.array([[1,2], [3,4], [5,6]])

print(np.array([a[0,0], a[1,1], a[2,1]]))

























