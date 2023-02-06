def depurar_frase(archivo,depurado):
    si = '.?,¿!-_<>'
    texto_limpio = open(depurado, 'a')
    with open(archivo) as texto:
        for linea in texto:
            linea_limpia = linea.translate(str.maketrans(" "," ", si))
            texto_limpio.write(linea_limpia)
    texto_limpio.close()

    
def meter_palabras_en_diccionario(f):
    import os
    from collections import defaultdict
    x = open(f,"r")
    lineas = defaultdict(list)
    for linea in x:
        frase = linea.split()
        for i in range(0,len(frase)-1):
            if i == 0:
                lineas["<<INICIO>>"].append(frase[i])
            if i == len(frase)-2:
                lineas["<<FINAL>>"].append(frase[i+1])
            lineas[frase[i]].append(frase[i+1])
            final = lineas["<<FINAL>>"]
    x.close()
    os.remove("archivolimpio.txt")
    return lineas,final



def generar_palabras(diccionario,final):
    import random
    palabras_generadas = open("palabras_generada.txt","a")
    can_frases = int(input("Cuantas frases quieres que haya? "))
    can_palabras =  100#int(input("Cuantas palabras quieres que haya en cada frase? "))
    for frases in range(0,can_frases):
        if frases != 0:
            palabras_generadas.write("\n")
            
        for palabras in range(0,can_palabras):
            if palabras == 0:
                valor_random = random.randint(0, len(diccionario["<<INICIO>>"])-1)
                palabra = (diccionario["<<INICIO>>"] [valor_random])
                palabras_generadas.write(palabra)
                palabras_generadas.write(" ")
            if palabras != 0 and palabras != can_palabras-1 and len(diccionario[palabra]) != 0:
                valor_random = random.randint(0, len(diccionario[palabra])-1)
                palabra_internas = (diccionario[palabra] [valor_random])
                palabras_generadas.write(palabra_internas)
                palabra = palabra_internas
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
                if prueba == 2 and len(diccionario[palabra]) != 0:
                    valor_random = random.randint(0, len(diccionario[palabra])-1)
                    palabra_internas = (diccionario[palabra] [valor_random])
                    palabras_generadas.write(palabra_internas)
                    palabras_generadas.write(".")
