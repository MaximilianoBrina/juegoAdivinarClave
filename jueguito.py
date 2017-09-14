def generarClave():
    from random import sample
    clave = sample(range(9), 5)
    return clave
""""
# 2 # Puede devolver dos veces el mismo nro
from random import randint
clave=[]
for i in range(5):
    clave.append(randint(1,9))
return clave
"""

def claveIngresadaPorUsuario():
    claveUsuario = []
    claveIngresadaPorUsuario = input("Ingresar clave de 5 numeros (entre 0 y 9):") #AGREGAR VALIDACION 5 CARACTERES, LOS 5 SON NROS.
    for i in claveIngresadaPorUsuario:
        claveUsuario.append(int(i))
    return claveUsuario


def juego():
    clave = generarClave()
    print(clave)
    for i in range(10):
        print("Intento nro. ", i + 1)
        if i == 9:
            print("Perdiste")
            print("La clave era ", clave)
            print("")
            input("")
            exit()
        claveUsuario = claveIngresadaPorUsuario()
        if clave == claveUsuario:
            print("Ganaste en ", i, "intentos!")
            input("")
            exit()
        else:
            for i in range(0,5):
                if claveUsuario[i] in clave:
                    if claveUsuario[i] != clave[i]:
                        claveUsuario[i] = "+"
                else:
                    claveUsuario[i] = "x"
            print("")
            print(claveUsuario)
            print("'x' significa que el numero ingresado no pertenece a la clave")
            print("'+' significa que el numero ingresado pertenece a la clave pero esta en una posicion incorrecta")
            print("")


def intro():
    print("                 _ _       _               _              _                    ")
    print("        /\      | (_)     (_)             | |            | |                   ")
    print("       /  \   __| |___   ___ _ __   __ _  | | __ _    ___| | __ ___   _____    ")
    print("      / /\ \ / _` | \ \ / / | '_ \ / _` | | |/ _` |  / __| |/ _` \ \ / / _ \   ")
    print("     / ____ \ (_| | |\ V /| | | | | (_| | | | (_| | | (__| | (_| |\ V /  __/	  ")
    print("    /_/    \_\__,_|_| \_/ |_|_| |_|\__,_| |_|\__,_|  \___|_|\__,_| \_/ \___|   ")
    print("")
    print("Diez intentos para adivinar la clave")
    print("")
    input("EMPEZAR")
    juego()


intro()