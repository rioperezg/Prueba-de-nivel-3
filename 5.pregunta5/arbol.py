class nodoArbol:
    def __init__(self, info):
        self.info = info
        self.izquierdo = None
        self.derecho = None

def arbol_vacio(raiz):
    return raiz is None

def insertar_nodo(raiz, elemento):
    if raiz is None:
        return nodoArbol(elemento)
    if elemento < raiz.info:
        raiz.izquierdo = insertar_nodo(raiz.izquierdo, elemento)
    else:
        raiz.derecho = insertar_nodo(raiz.derecho, elemento)
    return raiz

def buscar(raiz, clave):
    if raiz is None or raiz.info == clave:
        return raiz
    if clave < raiz.info:
        return buscar(raiz.izquierdo, clave)
    else:
        return buscar(raiz.derecho, clave)

def reemplazar(nodo):
    # busca el mayor en subárbol izquierdo
    padre = nodo
    reemplazo = nodo.izquierdo
    while reemplazo.derecho is not None:
        padre = reemplazo
        reemplazo = reemplazo.derecho
    # si reemplazo tiene hijo izquierdo, lo conecta a su padre
    if padre != nodo:
        padre.derecho = reemplazo.izquierdo
    return reemplazo

def eliminar_nodo(raiz, clave):
    if raiz is None:
        return None
    if clave < raiz.info:
        raiz.izquierdo = eliminar_nodo(raiz.izquierdo, clave)
    elif clave > raiz.info:
        raiz.derecho = eliminar_nodo(raiz.derecho, clave)
    else:
        # encontrado
        if raiz.izquierdo is None:
            return raiz.derecho
        if raiz.derecho is None:
            return raiz.izquierdo
        # dos hijos: usar reemplazar
        rep = reemplazar(raiz)
        raiz.info = rep.info
        # eliminar nodo reemplazo
        raiz.izquierdo = eliminar_nodo(raiz.izquierdo, rep.info)
    return raiz

def preorden(raiz):
    if raiz:
        print(raiz.info)
        preorden(raiz.izquierdo)
        preorden(raiz.derecho)

def inorden(raiz):
    if raiz:
        inorden(raiz.izquierdo)
        print(raiz.info)
        inorden(raiz.derecho)

def postorden(raiz):
    if raiz:
        postorden(raiz.izquierdo)
        postorden(raiz.derecho)
        print(raiz.info)

def por_nivel(raiz):
    """Realiza el barrido por niveles del árbol usando Cola dinámica."""
    if arbol_vacio(raiz):
        return
    pendientes = Cola()
    pendientes.arribo(raiz)
    while not pendientes.cola_vacia():
        nodo = pendientes.atencion()
        print(nodo.info)
        if nodo.izquierdo is not None:
            pendientes.arribo(nodo.izquierdo)
        if nodo.derecho is not None:
            pendientes.arribo(nodo.derecho)


class nodoCola(object):
    info, sig = None, None
class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamaño = 0
    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamaño += 1
    def atencion(cola):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
            cola.tamaño -= 1
        return dato
    def cola_vacia(cola):
        return cola.frente is None
    def en_frente(cola):
        return cola.frente.info
    def tamaño(cola):
        return cola.tamaño
    def mover_al_final(cola):
        dato = Cola.atencion(cola)
        Cola.arribo(cola,dato)
        return dato
    # Primera forma barrido, ineficiente(n^2)
    def barrido(cola):
        caux = Cola()
        while(not Cola.cola_vacia(cola)):
            dato = Cola.atencion(cola)
            print(dato)
            Cola.arribo(caux, dato)
        while(not Cola.cola_vacia(caux)):
            dato = Cola.atencion(caux)
            Cola.arribo(cola,dato)
    # Segunda forma barrido, eficiente(n)
    def barrido2(cola):
        i = 0
        while(i < Cola.tamaño(cola)):
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1