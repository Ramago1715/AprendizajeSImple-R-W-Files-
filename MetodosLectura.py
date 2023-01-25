def leerarchivo(archivo,formato):
    f = open(archivo,formato)
    lineas = []
    for linea in f:
        lineas.append(linea.split())
    print(len(lineas),lineas)

leerarchivo("frases_informatica.txt","rt")
