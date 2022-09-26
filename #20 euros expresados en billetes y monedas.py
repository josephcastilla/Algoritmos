print("\033[1;31;40m"+"EUROS EXPRESADOS EN BILLETES Y MONEDAS"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
euros = int (input ("Digita cantidad de euros: "))
#-------------------------------------------------operaciones-----------------------------------------------------------
m1=euros
b500=(m1-m1%500)//500
m1=m1%500
b200=(m1-m1%200)//200
m1=m1%200
b100=(m1-m1%100)//100
m1=m1%100
b50=(m1-m1%50)//50
m1=m1%50
b20=(m1-m1%20)//20
m1=m1%20
b10=(m1-m1%10)//10
m1=m1%10
b5=(m1-m1%5)//5
m1=m1%5
m2=(m1-m1%2)//2
m1=m1%2
#----------------------------------------------------salida-------------------------------------------------------------
print ("billetes de 10: " ,b10)
print ("billetes de 100: " ,b100)
print ("billetes de 20: " ,b20)
print ("billetes de 200: " ,b200)
print ("billetes de 5: " ,b5)
print ("billetes de 50: " ,b50)
print ("billetes de 500: " ,b500)
print ("monedas de 1: " ,m1)
print ("monedas de 2: " ,m2)
print ("hecho por joseph castilla,2022")