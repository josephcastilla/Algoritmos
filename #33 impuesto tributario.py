print("\033[1;31;40m"+"IMPUESTO TRIBUTARIO"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
e= int(input("digite su edad: "))
z = float(input("digite sus ingresos mensuales: "))
#-----------------------------------------------salida/operaciones------------------------------------------------------
if e > 16 and z >= 1000:
    print("tiene que tributar")
else:
    print("No tiene que tributar")
print("hecho por joseph castilla,2022")