print("\033[1;31;40m"+"CALCULAR AREA Y PERIMETRO DE UN TRIANGULO"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
a=int (input ("digite primer lado: "))
b=int (input ("digite segundo lado: "))
c=int (input ("digite angulo c: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
import math
h=(a**2-b**2)
h2=h**0.5
ar=(b*h2)/2
pr= (a+b+h2)
#----------------------------------------------------salida-------------------------------------------------------------
print ("la altura es: ",round (h2,3))
print ("el area es: ",round (ar,3),"²")
print ("el perimetro es: ",round (pr,3))
print ("hecho por joseph castilla,2022")