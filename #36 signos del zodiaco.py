print("\033[1;31;40m"+"SIGNOS DEL ZODIACO"+'\033[0;m')
#---------------------------------------------------entrada-------------------------------------------------------------
d=int(input("digite dia: "))
m=input("digite mes: ")
#-------------------------------------------salida/operaciones----------------------------------------------------------
if  m=="1" and d>=9 or m=="2" and d<=15:  print("capricornio")
elif m=="2" and d>=16 or m=="3" and d<=11:  print("acuario")
elif m=="3" and d>=12 or m=="4" and d<=18:  print("piscis")
elif m=="3" and d>=27 or m=="3" and d<=28:  print("cetus")
elif m=="4" and d>=19 or m=="5" and d<=13:  print("aries")
elif m=="5" and d>=14 or m=="6" and d<=19:  print("tauro")
elif m=="6" and d>=20 or m=="7" and d<=20:  print("geminis")
elif m=="7" and d>=21 or m=="8" and d<=9:  print("cancer")
elif m=="8" and d>=10 or m=="9" and d<=15:  print("leo")
elif m=="9" and d>=16 or m=="10" and d<=30:  print("virgo")
elif m=="10" and d>=31 or m=="11" and d<=22:  print("libra")
elif m=="11" and d>=23 or m=="11" and d<=29:  print("escorpio")
elif m=="11" and d>=30 or m=="12" and d<=17:  print("ofiuco")
elif m=="12" and d>=18 or m=="1" and d<=8:  print("sagitario")
print("hecho por joseph castilla")

optimizar