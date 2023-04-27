"""
Crea un script llamado generador.py que cumpla las siguientes necesidades:

Debe incluir una función llamada leer_numero(). Esta función tomará 3 valores: ini, fin y mensaje. El objetivo es leer por pantalla 
un número >= que ini y <= que fin. Además a la hora de hacer la lectura se mostrará en el input el mensaje enviado a la función. 
Finalmente se devolverá el valor. Esta función tiene que devolver un número, y tiene que repetirse hasta que el usuario no lo escriba 
bien (lo que incluye cualquier valor que no sea un número del ini al fin).
Una vez la tengas creada, deberás crear una nueva función llamada generador, no recibirá ningún parámetro. Dentro leerás dos números 
con la función leer_numero():
El primer numero será llamado numeros, deberá ser entre 1 y 20, ambos incluidos, y se mostrará el mensaje ¿Cuantos números quieres 
generar? [1-20]:
El segundo número será llamado modo y requerirá un número entre 1 y 3, ambos incluidos. El mensaje que mostrará será: ¿Cómo quieres 
redondear los números? [1]Al alza [2]A la baja [3]Normal:.
Una vez sepas los números a generar y cómo redondearlos, tendrás que realizar lo siguiente:
Generarás una lista de números aleatorios decimales entre 0 y 100 con tantos números como el usuario haya indicado.
A cada uno de esos números deberás redondearlos en función de lo que el usuario ha especificado en el modo.
Para cada número muestra durante el redondeo, el número normal y después del redondeo.
Finalmente devolverás la lista de números redondeados.
El objetivo de este ejercicio es  la reutilización de código y los módulos random y math.
"""
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