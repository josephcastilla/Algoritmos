print("\033[1;31;40m"+"CONVERSOR DE KM,YD,IN"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
a=int (input ("digitar metros: "))
o=0
print("\033[;31m"+"1.metros a kilometros(km) \n2.metros a yardas(yd) \n3.metros a pulgadas(in)"+'\033[0;m')
o = int(input("Digite tipo de conversion: ") )
#-------------------------------------------------operaciones-----------------------------------------------------------
if o == 1:  print(round (a/1000,3),"kilometros")
elif o == 2:    print(round (a/0.9144,3),"yardas")
elif o == 3:    print(round (a*39.3701,3),"pulgadas")
#----------------------------------------------------salida-------------------------------------------------------------
print("hecho por joseph castilla,2022")