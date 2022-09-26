print("\033[1;31;40m"+"OPERACIONES BASICAS (+,-,*,/)"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
n1=float(input("Digite #: ") )
n2=float(input("digite #: ") )
o=0
print("\033[;31m"+"1.Suma \n2.Resta \n3.Multiplicacion  \n4.Divicion"+'\033[0;m')
o = int(input("Digite tipo de operacion: ") )
#-----------------------------------------------salida/operaciones------------------------------------------------------
if o == 1:  print("Resultado: ",n1+n2)
elif o == 2:    print("Resultado: ",n1-n2)
elif o == 3:    print("Resultado: ",n1*n2)
elif o == 4:    print("Resultado: ",n1/n2)
print("hecho por joseph castilla,2022")