class nodoLista(object):
    info, sig = None, None
class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0
    def criterio(dato, campo = None):
        dic = {}
        if(hasattr(dato, "__dict__")):
            dic = dato.__dict__
        if campo is None or campo not in dic:
            return dato
        else:
            return dic[campo]    
    def insertar(lista, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        if (lista.inicio is None) or (Lista.criterio(lista.inicio.info, campo) > Lista.criterio(dato, campo)):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while(act is not None and Lista.criterio(act.info, campo) < Lista.criterio(dato, campo)):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tamaño += 1
    def lista_vacia(lista):
        return lista.inicio is None
    def eliminar(lista, clave, campo=None):
        dato = None
        if(Lista.criterio(lista.inicio.info, campo) != Lista.criterio(clave, campo)):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamaño -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while(actual is not None and Lista.criterio(actual.info, campo) != Lista.criterio(clave, campo)):
                anterior = anterior.sig
                actual = actual.sig
            if (actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamaño -= 1
        return dato
    def tamaño(lista):
        return lista.tamaño
    def buscar(lista, buscado, campo=None):
        aux = lista.inicio
        while(aux is not None and Lista.criterio(aux.info, campo) != Lista.criterio(buscado, campo)):
            aux = aux.sig
        return aux
    def barrido(lista):
        aux = lista.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
            