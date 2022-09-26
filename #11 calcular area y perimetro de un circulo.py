print("\033[1;31;40m"+"CALCULAR AREA Y PERIMETRO DE UN CIRCULO"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
r =float (input ("ingresa valor de radio: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
import math
a2= math.pi * (r * r)
p= (2 * math.pi * r)
#----------------------------------------------------salida-------------------------------------------------------------
print ("el area es",round (a2,3))
print ("el perimetro es",round (p,3))
input ("hecho por joseph castilla,2022")