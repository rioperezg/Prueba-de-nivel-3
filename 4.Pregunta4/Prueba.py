import random
import math
def leer_numero(ini, fin, mensaje):
    while True:
        try:
            num = int(input(mensaje))
        except ValueError:
            print("Error: Debe introducir un numero entero")
        else:
            if num >= ini and num <= fin:
                return num
            else:
                print("Error: El numero debe estar entre {} y {}".format(ini, fin))
def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    lista = []
    for i in range(numeros):
        numero = random.uniform(0, 100)
        if modo == 1:
            print("{} => {}".format(numero, math.ceil(numero)))
            lista.append(math.ceil(numero))
        elif modo == 2:
            print("{} => {}".format(numero, math.floor(numero)))
            lista.append(math.floor(numero))
        else:
            print("{} => {}".format(numero, round(numero)))
            lista.append(round(numero))
    return lista