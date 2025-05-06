"""
Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea- toria– que resuelva las siguientes actividades:
 
realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
 determinar si un número está cargado en el árbol o no;
 eliminar tres valores del árbol;
 determinar la altura del subárbol izquierdo y del subárbol derecho;
 determinar la cantidad de ocurrencias de un elemento en el árbol;
 contar cuántos números pares e impares hay en el árbol
"""
import random
from arbol import (
    nodoArbol, arbol_vacio, insertar_nodo, buscar,
    eliminar_nodo, preorden, inorden, postorden, por_nivel
)

# Función para calcular la altura de un árbol
def altura(raiz):
    if raiz is None:
        return 0
    return 1 + max(altura(raiz.izquierdo), altura(raiz.derecho))

# Cuenta cuántas veces aparece `valor` en el árbol
def contar_ocurrencias(raiz, valor):
    if raiz is None:
        return 0
    cuenta = 1 if raiz.info == valor else 0
    cuenta += contar_ocurrencias(raiz.izquierdo, valor)
    cuenta += contar_ocurrencias(raiz.derecho, valor)
    return cuenta

# Cuenta cuántos nodos pares e impares hay
def contar_pares_impares(raiz):
    if raiz is None:
        return 0, 0
    p_izq, i_izq = contar_pares_impares(raiz.izquierdo)
    p_der, i_der = contar_pares_impares(raiz.derecho)
    if raiz.info % 2 == 0:
        return p_izq + p_der + 1, i_izq + i_der
    else:
        return p_izq + p_der, i_izq + i_der + 1

if __name__ == "__main__":
    # 1) Generar y cargar 1000 números aleatorios en el árbol
    root = None
    secundarios = []
    for _ in range(1000):
        n = random.randint(0, 1000)
        secundarios.append(n)
        root = insertar_nodo(root, n)

    # 2) Barridos
    print("=== Preorden ===")
    preorden(root)
    print("\n=== Inorden ===")
    inorden(root)
    print("\n=== Postorden ===")
    postorden(root)
    print("\n=== Por Nivel ===")
    por_nivel(root)

    # 3) Buscar un número (tomamos uno de los generados y otro inexistente)
    prueba1 = random.choice(secundarios)
    prueba2 = 2000  # seguro no está entre 0–1000
    print(f"\nBuscar {prueba1}:",
          "Sí está" if buscar(root, prueba1) else "No está")
    print(f"Buscar {prueba2}:",
          "Sí está" if buscar(root, prueba2) else "No está")

    # 4) Eliminar tres valores aleatorios del árbol
    a_eliminar = random.sample(secundarios, 3)
    print("\nEliminando:", a_eliminar)
    for v in a_eliminar:
        root = eliminar_nodo(root, v)

    # 5) Alturas de subárboles
    alt_izq = altura(root.izquierdo)
    alt_der = altura(root.derecho)
    print(f"\nAltura subárbol izquierdo: {alt_izq}")
    print(f"Altura subárbol derecho:   {alt_der}")

    # 6) Contar ocurrencias de un valor
    valor_o = random.choice(secundarios)
    ocurr = contar_ocurrencias(root, valor_o)
    print(f"\nOcurrencias de {valor_o}: {ocurr}")

    # 7) Contar pares e impares
    pares, impares = contar_pares_impares(root)
    print(f"\nTotal pares:   {pares}")
    print(f"Total impares: {impares}")


