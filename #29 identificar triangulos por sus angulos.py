print("\033[1;31;40m"+"IDENTIFICAR TIPOS DE TRIANGULOS CON SUS ANGULOS"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
k=int(input("digite un angulo: "))
l=int(input("digite segundo angulo: "))
g=int(input("digite tercer angulo: "))
#----------------------------------------------salida/operaciones-------------------------------------------------------
if (k==0) or (g==0) or (l==0):
    print("indeterminado")
elif (k==90) or (g==90) or (l==90):
    print("es un triangulo rectangulo")
elif (k<90)and (g<90) and (l<90):
    print("es un triangulo acutangulo")
elif (k>90) or (g>90) or (l>90):
    print("es un triangulo obtusangulo")
print("hecho por joseph castilla,2022")