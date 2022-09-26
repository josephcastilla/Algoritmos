print("\033[1;31;40m"+"INDENTIFICAR NUMEROS, LETRAS Y SIMBOLOS"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
x = input("Digite numero, letra o simbolo: ")
#----------------------------------------------salida/operaciones-------------------------------------------------------
if(ord(x) >= 48 and ord(x) <= 57):
    print("Es un numero")
elif (ord(x) >= 65 and ord(x) <= 90):
    print("Es una letra")
elif (ord(x) >= 97 and ord(x) <= 122):
    print("Es una letra")
else:
    print("Es un simbolo")
    print("hecho por joseph castilla,2022")