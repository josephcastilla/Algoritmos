print("\033[1;31;40m"+"CALCULAR SUELDO DE EMPLEADOS"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
n=input("digite su nombre: ")
h=int(input("digite numero de horas trabajadas: "))
v=int(input("digite valor de horas: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
s=(h*v)
ds=(s*0.085)
dp=(s*0.08)
df=(s*0.04)
td=(ds+dp+df)
ts=(s-td)
#----------------------------------------------------salida-------------------------------------------------------------
print(n,"su sueldo es",s)
print("\033[;31m"+"-8.5% salud\n-8% pension\n-4% Fondo de empleados"+'\033[0;m')
print("Total de descuento",round (td,2))
print("Total de sueldo",round (ts,2))
print("hecho por joseph castilla,2022")