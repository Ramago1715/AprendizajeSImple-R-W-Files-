from MetodosLaberinto import *
from colorama import Back,Fore
import time 

muro = ["1,0","1,1","1,2","2,2","2,3","3,3","3,2","4,2"]
entrada = ("0,0")
camino = []
salida = ("4,4")
tamaño = int(input("De cuanto quieres que sea el laberinto (n X n ) "))
X = 0
Y = 0
monigote = entrada
# print(monigote)
# Y =+ 1
# monigote = str(X)+","+str(Y)
# print(monigote)


salir = False
laberinto = generar_laberinto(tamaño,muro,entrada,salida,camino)
printear_laberinto(laberinto)

print(muro)
while salir == False:
    if monigote == salida:
      salir = True
    #Ir a la derecha
    elif str(X)+","+str(Y+1) not in muro and str(X)+","+str(Y+1) not in camino:
       Y = Y+1
       camino.append(str(X)+","+str(Y))
       monigote = camino[-1]
       laberinto = generar_laberinto(tamaño,muro,entrada,salida,camino)
       printear_laberinto(laberinto)
       time.sleep(1)
    #Ir abajo
    elif str(X)+","+str(X+1) not in muro or str(X)+","+str(X+1) not in camino:
       X = X+1
       camino.append(str(X)+","+str(Y))
       monigote = camino[-1]
       laberinto = generar_laberinto(tamaño,muro,entrada,salida,camino)
       printear_laberinto(laberinto)
       time.sleep(1)
    #Ir a la Izquierda
    elif str(X)+","+str(Y-1) not in muro or str(X)+","+str(Y-1) not in camino:
       Y = Y-1
       camino.append(str(X)+","+str(Y))
       monigote = camino[-1]
       laberinto = generar_laberinto(tamaño,muro,entrada,salida,camino)
       printear_laberinto(laberinto)
       time.sleep(1)
    #IR arriba
    elif str(X)+","+str(X-1) not in muro or str(X)+","+str(X-1) not in camino:
       X = X-1
       camino.append(str(X)+","+str(Y))
       monigote = camino[-1]
       laberinto = generar_laberinto(tamaño,muro,entrada,salida,camino)
       printear_laberinto(laberinto)
       time.sleep(1)