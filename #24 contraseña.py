print("\033[1;31;40m"+"CONTRASEÑA CORRECTA O INCORRECTA"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
c = "contraseña"
password = input("Introduce la contraseña: ")
#----------------------------------------------salida/operaciones-------------------------------------------------------
if c == password.lower(): print("La contaseña es correcta")
else:   print("La contraseña es incorrecta")
print("hecho por joseph castilla,2022")