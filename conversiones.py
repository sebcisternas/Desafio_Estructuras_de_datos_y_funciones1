import sys
#Definicion de Listas
moneda = ["Sol peruano","Peso Argentino","Dólar Americano"]
conversion = []

#Llenado de listas con argumentos desde consola
conversion = [float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])]
p_chileno = int(sys.argv[4])
diccionario = {key:value for key,value in zip(moneda,conversion)}

#Impresion por pantalla de las conversiones
print(f"Los {p_chileno} pesos chilenos equivalen a:")

#Ciclo for para recorrer el diccionario e imprimir dependiendo de la moneda
for k,v in diccionario.items(): 
    if k=="Sol peruano":
     print(f'{v*p_chileno} Soles')
    elif k=="Peso Argentino":
     print(f'{v*p_chileno} Pesos Argentinos')
    else:
     print(f'{v*p_chileno} Dólares')