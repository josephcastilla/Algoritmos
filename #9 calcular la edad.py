print("\033[1;31;40m"+"CALCULAR EDAD"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
ac=int(input("año actual: "))
an=int(input("año de nacimiento: "))
da=int(input("dia actual: "))
dn=int(input("dia de nacimiento: "))
ma=int(input("mes actual: "))
mn=int(input("mes de nacimiento: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
ed=ac-an
if mn>ma or (mn==ma and dn>da):
    ed=ed-1
#----------------------------------------------------salida-------------------------------------------------------------
print ("su edad es: ",ed)
print("hecho por joseph castilla,2022")