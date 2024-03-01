import sys

#Ingresa el argumento , en este caso el nombre del archivo y su extension
nombre_archivo = sys.argv[1]

#fucion para abrir el archivo ingreso por argumento
with open( nombre_archivo, "r") as file:
    texto = file.read()

#transforma el texto del archivo guardado en la variable texto en una lista separada por palabras
lista = texto.split(" ")

#genera dos estructuras de datos set , una para guardar las palabras distintas y otra inicializada para guardar los caracteres
set_palabras = set(lista)
set_caracteres = set()

for palabra in lista:
    for caracter in palabra :
        set_caracteres.add(caracter)


print(f"El número de caracteres distintos es: {len(set_caracteres)}")
print(f"El número de palabras distintas es: {len(set_palabras)} ")
