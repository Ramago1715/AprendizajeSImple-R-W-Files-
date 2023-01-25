def leerarchivo():
    f = open("star_wars.txt",)
    lineas = []
    for linea in f:
        lineas.append(linea.split())
    print(len(lineas),lineas)

leerarchivo()