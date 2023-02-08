# CADENAS DE MARKOV
## FUNCIONES
### depurar_frase
##### Pide 2 parametros esta funcion uno es el archivo que quieres depurar y el otro es un archivo vacio en cual va a pasar a ser nuestro archivo limpio
### meter_palabras_en_diccionario
##### Esta funcion te pide tan solo un parametro que es el archvio ya depurado, lo abre y pasando linea por linea divide cada linea en palabras con el metodo split, y se alamcenan en una lista, dependiendo de la posicion de las palabras en esa lista de clasifican en diferentes sitios, despues la funcion borra el archivo porque ya no lo necesitamos, devuelve el diccionario rellenado y un array con los valores de la key final
### generar_palabras
##### Esta funcion recoge el diccionario rellenado y el array de final para ir comparando si la palabra actual concuerda con algun valor del final, esta funcion tiene un bucle grande para moverse entre frases y otro dentro para recorrer cada palabra, si es la primera palabra de esa frase usa una palabra de la key INICIO, despues genera una palabra que este como valor en la key de la palabra anterior generada, asi hasta llegar a la ultima que genera una de la key FINAL, en el caso de que no cuadre ninguna palabra de final genera una que tenga sentido con la actual
