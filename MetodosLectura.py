def depurar_frase(archivo,depurado):
    si = '.?,¿!-_<>' #guardo los caracteres que quiero quitar
    texto_limpio = open(depurado, 'a')
    with open(archivo) as texto:
        for linea in texto: #recorro linea por linea del archivo sucio
            linea_limpia = linea.translate(str.maketrans(" "," ", si)) #use este metodo para que cada linea sustituya lo que hay en la variable si por lo que hay entre los parentesis
            texto_limpio.write(linea_limpia)
    texto_limpio.close()

    
def meter_palabras_en_diccionario(f):
    import os
    from collections import defaultdict
    x = open(f,"r")
    lineas = defaultdict(list) #inicializo el diccionario con el valor como lista
    for linea in x:
        frase = linea.split() #guardo las palabras de una linea separas en un array
        for i in range(0,len(frase)-1): #recorremos el array donde hemos guardado las palabras
            if i == 0: #si es la primera la metemos en inicio
                lineas["<<INICIO>>"].append(frase[i])
            if i == len(frase)-2: #si es la ultima la metemos en final
                lineas["<<FINAL>>"].append(frase[i+1])
            lineas[frase[i]].append(frase[i+1]) #y aunque la hayamos metido en final o en inicio la metemos en una clave suya propia
            final = lineas["<<FINAL>>"]
    x.close()
    os.remove("archivolimpio.txt")
    return lineas,final



def generar_palabras(diccionario,final):
    import random
    palabras_generadas = open("palabras_generada.txt","a")
    can_frases = int(input("Cuantas frases quieres que haya? "))
    can_palabras =  100#int(input("Cuantas palabras quieres que haya en cada frase? "))
     #for para moverse de linea en linea el condicional es para que no haga un salto de linea en la primera
    for frases in range(0,can_frases):
       
        if frases != 0:
            palabras_generadas.write("\n")
         #for para moverse de palabra en palabra de una misma linea   
        for palabras in range(0,can_palabras):
            #si es la primera palabra selecciona las palabras guardadas en la clave <<INICIO>> del diccionario
            if palabras == 0:

                valor_random = random.randint(0, len(diccionario["<<INICIO>>"])-1) #genero un numero random entre 0 y el tamaño de la clave inicio (-1 porque python acaba uno antes y si no da un error)
                palabra = (diccionario["<<INICIO>>"] [valor_random]) #guardo el valor de la posicion que haya tocado de la clave inicio
                palabras_generadas.write(palabra) #La escribo en el archivo
                palabras_generadas.write(" ") # y le pongo un espacio
            if palabras != 0 and palabras != can_palabras-1 and len(diccionario[palabra]) != 0: #el segundo condicional esta porque a veces pillaba palabras sin valor y daba un error en la libreria de random

                valor_random = random.randint(0, len(diccionario[palabra])-1)#genero un numero random entre 0 y el tamaño de la clave inicio (-1 porque python acaba uno antes y si no da un error)
                palabra_internas = (diccionario[palabra] [valor_random])#guardo el valor de la posicion que haya tocado de la clave  del valor anterior
                palabras_generadas.write(palabra_internas)
                palabra = palabra_internas # guardo el valor de palabra interna para saber en que clave buscar del diccionario
                palabras_generadas.write(" ")
            if palabras == can_palabras-1: 

                prueba = 2
                for y in final:

                    if y in diccionario[palabra]:
                        valor_random = random.randint(0, len(diccionario["<<FINAL>>"])-1)
                        palabra_final = (diccionario["<<FINAL>>"] [valor_random])
                        palabras_generadas.write(palabra_final)
                        palabras_generadas.write(".")
                        prueba = 0

                if prueba == 2 and len(diccionario[palabra]) != 0: #esta fuera del for para que no tenga que comprobarlo todo el rato

                    valor_random = random.randint(0, len(diccionario[palabra])-1)
                    palabra_internas = (diccionario[palabra] [valor_random])
                    palabras_generadas.write(palabra_internas)
                    palabras_generadas.write(".")
           
    palabras_generadas.close

    
