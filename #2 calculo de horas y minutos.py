print("\033[1;31;40m"+"CALCULO DE HORAS Y MINUTOS"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
mts=int(input("digite los minutos: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
h=mts//60
m=mts%60
#----------------------------------------------------salida-------------------------------------------------------------
print("son:", h,"horas" " y", m, "minutos")
input("hecho por joseph castilla, 2022")