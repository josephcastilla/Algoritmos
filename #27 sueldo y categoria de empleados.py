print("\033[1;31;40m"+"SUELDO Y CATEGORIA DE EMPLEADOS"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
print("\033[;36m"+"#1.Categoria a \n#2.Categoria b \n#3.Categoria c \n#4.Categoria d \n#5.Categoria e"+'\033[0;m')
w = float (input ("digite # categoria: "))
z = float (input ("digite sueldo: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
k=0
if w==1:
    k=z*0.15
if w==2:
    k=z*0.10
if w==3:
    k=z*0.08
if w==4:
    k=z*0.05
if w==5:
    k=z*0
zk=z+k
#----------------------------------------------------salida-------------------------------------------------------------
print ("aumento:  ", k)
print ("nuevo sueldo: ", zk)
print("hecho por joseph castilla,2022")