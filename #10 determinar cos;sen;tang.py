print("\033[1;31;40m"+"CALCULAR OPERACIONES"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
import math as ma
a=int(input("digite numero: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
res=ma.log(a)
res2=ma.log(a,10)
res3=a**0.5
g=a
r = (g* ma.pi)/180
sen= ma.sin(r)
cos = ma.cos(r)
tang = ma.tan(r)
#----------------------------------------------------salida-------------------------------------------------------------
print("logaritmo natural",round (res,3))
print("logaritmo base 10",round (res2,3))
print("raiz cuadrada",round (res3,3))
print("seno en radianes",round (sen,3))
print("coseno en radianes",round (cos,3))
print("tangente en radianes",round (tang,3))
print("hecho por joseph castilla,2022")