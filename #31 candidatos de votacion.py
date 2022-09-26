print("\033[1;31;40m"+"CANDIDATOS DE VOTACION"+'\033[0;m')
print("\033[;36m"+"ELECCIONES \ncandidato rojo (a) \ncandidato verde (b) \ncandidato azul (c) "+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
c=input("Elegir un candidato: ")
#----------------------------------------------salida/operaciones-------------------------------------------------------
if c=="a":
    print("Usted ha votado por el partido rojo")
elif c=="b":
    print("Usted ha votado por el partido verde")
elif c=="c":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")
print("hecho por joseph castilla,2022")