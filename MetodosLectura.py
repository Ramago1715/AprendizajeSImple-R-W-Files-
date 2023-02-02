def depurar_frase(archivo,documento_limpio):
    si = '.?,¿!-_<>'
    texto_limpio = open(documento_limpio, 'a')
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
                lineas["INICIO"].append(frase[i])
            lineas[frase[i]].append(frase[i+1])
    print(lineas)
    x.close()
    os.remove("archivolimpio.txt")
    
    

#al crear las frases no pueden ser frases repetidas ni que existen en el doc original
#random.choice(lista)
