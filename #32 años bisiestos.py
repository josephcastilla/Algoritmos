print("\033[1;31;40m"+"AÑO BISIESTO"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
año=int (input("Digita un año: "))
#---------------------------------------------salida/operaciones--------------------------------------------------------
if año<1500 or año>2200:
    print("fuera de rango")
elif (año % 4==0 and año % 100 != 0) or año % 400 == 0:
    print ("el año",año, "es bisiesto")
else:
    print ("el año",año," no es bisiesto")
print("hecho por joseph castilla,2022")