print("\033[1;31;40m"+"CALCULAR AREA Y PERIMETRO DE TRIANGULO"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
a=int (input ("digite la base: "))
b=int (input ("digite la altura: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
ar= (a*b)/2
p= (a**2+b**2)
p2=p**0.5
pr=p2+a+b
#----------------------------------------------------salida-------------------------------------------------------------
print ("el area es: ",ar,"²")
print ("el perimetro es: ", pr)
print("hecho por joseph castilla")