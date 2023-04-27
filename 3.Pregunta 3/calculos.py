""""
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las 
siguientes instrucciones. Observa si el comportamiento es el esperado:

from operaciones import *

 

a, b, c, d = (10, 5, 0, "Hola")

 

print( "{} + {} = {}".format(a, b, suma(a, b) ) )

print( "{} - {} = {}".format(b, d, resta(b, d) ) )

print( "{} * {} = {}".format(b, b, producto(b, b) ) )

print( "{} / {} = {}".format(a, c, division(a, c) ) )
"""
from operaciones import suma, resta, producto, division
