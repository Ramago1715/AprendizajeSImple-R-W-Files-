def lectura_archvio(archivo):
    f = open(archivo,encoding="windows-1252")
    return f
    
def depurar_frase(archivo):
    texto_limpio = archivo
    textolimp = texto_limpio.translate(str.maketrans('.?,-`´></,','',string.punctuation))
    print(texto_limpio)

def meter_palabras_en_diccionario(f):
    from collections import defaultdict
    lineas = defaultdict(list)
    for linea in f:
            frase = linea.split()
            for i in range(0,len(frase)-1):
                    if i == 0:
                        lineas["INICIO"].append(frase[i])
                    lineas[frase[i]].append(frase[i+1])
    print(lineas)

#al crear las frases no pueden ser frases repetidas ni que existen en el doc original
#random.choice(lista)
