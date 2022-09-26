print("\033[1;31;40m"+"SERVICIO MILITAR"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
e=int(input("digite edad: "))
s=input("digite sexo (M/F): ")
n=input("digite nacionalidad: ")
#----------------------------------------------salida/operaciones-------------------------------------------------------
if (e>=18) and (e<25) and (s=="m") and (n=="colombiana"):
    print("debe prestar servicio militar")
else:
    print("no debe prestar servicio militar")
print("hecho por joseph castilla,2022")