print("\033[1;31;40m"+"IDENTIFICAR TIPOS DE TRIANGULOS"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
k=int(input("digite primer lado: "))
l=int(input("digite segundo lado: "))
g=int(input("digite tercer lado: "))
#----------------------------------------------salida/operaciones-------------------------------------------------------
if (k==l) and (k==g):
    print("es un triangulo equilatero")
elif (k==0) or (g==0) or (l==0):
    print("indeterminado")
elif (k!=l)and (k!=g) and (g!=l):
    print("es un triangulo escaleno")
else:   print("es un triangulo isoceles")
print("hecho por joseph castilla,2022")