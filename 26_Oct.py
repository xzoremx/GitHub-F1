#Importando un archivo csv -> lista:

import csv

with open('C:/Users/aa/Desktop/mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

print(mpg[: 3])

print(len(mpg))

#tenemos un diccionario para cada uno de los 234 autos del archivo csv

print(mpg[0].keys()) #observando el nombre de las columnas

