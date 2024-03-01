recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                 ['2021-05-01', "15:00", "No trabajar"],
                 ['2021-07-15', "13:00", "No hacer nada es feriado"],
                 ['2021-09-18', "16:00", "Ramadas"],
                 ['2021-12-25', "00:00", "Navidad"]]

# Output

for i in range(len(recordatorios)):
    for j in range(len(recordatorios[i])):
        if recordatorios[i][j]=='2021-01-01':
            recordatorios.insert(i+1,['2021-02-02','06:00','Empezar el Año'])
        elif recordatorios[i][j]=='2021-07-15':
            recordatorios[i][j]='2021-07-16'
       
 
for i in range(len(recordatorios)):
    for j in range(len(recordatorios[i])):
         if recordatorios[i][j]=='2021-12-25':
             recordatorios.insert(i,['2021-12-24','22:00','Cena de Navidad'])
             recordatorios.insert(i+2,['2021-12-31','22:00','Cena de Año Nuevo'])



print(recordatorios)

