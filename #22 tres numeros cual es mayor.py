print("\033[1;31;40m"+"NUMERO MAYOR DE 3"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
n1 = int(input("Digite primer numero: "))
n2 = int(input ("Digite segundo numero: "))
n3 = int (input ("Digite tercer numero: "))
#----------------------------------------------salida/operaciones-------------------------------------------------------
if n1 > n2 and n1 > n3: print("el numero mayor es: ", n1)
elif n2 > n1 and n2 > n3:   print ("el numero mayor es: ", n2)
elif n3 > n1 and n3 > n2:   print("el numero mayor es: ", n3)
else:   print ("hay 2 numeros iguales")
print("hecho por joseph castilla,2022")