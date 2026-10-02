def normalizar(cadena):
    cadena = cadena.lower()
    cadena = cadena.strip()
    for letra in cadena:        #con el replace no hace falta el bucle
        if letra in "áéíóúüï":
            cadena = cadena.replace("á", "a")
            cadena = cadena.replace("é", "e")
            cadena = cadena.replace("í", "i")
            cadena = cadena.replace("ó", "o")
            cadena = cadena.replace("ú", "u")
            cadena = cadena.replace("ü", "u")
            cadena = cadena.replace("ï", "i")
    print(cadena)
    return(cadena)

def enmascarar(palabra, l_adivinadas):
    palabra2 = ""
    for letra in palabra:
        if letra in l_adivinadas:
            palabra2 += letra
        else:
            palabra2 +="_"
    print(palabra2)
    return(palabra2)


def ha_ganado(p_secreta, p_jugador):
    if p_secreta == p_jugador:
        res = True
    else: 
        res = False
    print(res)
    return(res)