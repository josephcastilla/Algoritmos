print("\033[1;31;40m"+"DESCOMPONER NUMEROS U/D/C/UM"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
n = int (input ('digite numero de 4 cifras: '))
#-------------------------------------------------operaciones-----------------------------------------------------------
umil=(n%10000-n%1000)//1000
cen=(n%1000-n%100)//100
dec=(n%100-n%10)//10
u=n%10
#----------------------------------------------------salida-------------------------------------------------------------
print ("unidades",u)
print ("decenas:",dec)
print ("centenas:",cen)
print ("unidades de mil:",umil)
print("hecho por joseph castilla,2022")