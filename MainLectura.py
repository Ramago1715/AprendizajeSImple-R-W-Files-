#leer frases
#usar split() para separar las frases en sus palabras en una lista
#meter todas esas palabras en un diccionario como key
#y como valor metemos una lista metemos todas las palabras que van despues de esta(repetidas incluidas)
from MetodosLectura import *



depurar_frase("frases_informatica.txt","archivolimpio.txt")
diccionario_relleno,final = meter_palabras_en_diccionario("archivolimpio.txt")
generar_palabras(diccionario_relleno,final)

