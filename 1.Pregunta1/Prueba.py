###################
# Implementacion de clase cola y funciones:
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

###################
# ARBOLES BINARIOS
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

# Ejemplo de uso:
# raiz = insertar_nodo(None, 10)
# insertar_nodo(raiz, 5); insertar_nodo(raiz, 15); ...
# por_nivel(raiz)

"""
Nick Fury, líder de la agencia S.H.I.E.L.D., tiene la difícil tarea de decidir qué vengador asignará a cada nueva misión (por ahora 
considere que solo se asignará un superhéroe por cada misión). Teniendo en cuenta el listado de superhéroes es el siguiente:

Nombre

Iron Man

The incredible Hulk

Khan

Thor

Captain América

Capitana Marvel

Ant-Man

Nick Fury

The Winter Soldier


Nos solicita desarrollar un árbol de decisión para resolver esta tarea con los siguientes requerimientos:

cada nodo hoja del árbol debe ser un superhéroe y en cada nodo intermedio inclusive la raíz debe haber una pregunta. Si la respuesta 
es sí, se debe desplazar hacia el subárbol izquierdo, si es no al subárbol derecho. Además, debéis desarrollar una función que 
determine el superhéroe para una misión;
Khan es ideal para misiones intergalácticas en equipo;
Ant-Man es excelente en misiones de recuperación donde sea necesario no se detectado;
para misiones de destrucción Hulk es una excelente opción;
el Capitán América es un supersoldado de ética incorruptible ideal para comandar misiones de defensa y de recuperación;
Capitana Marvel es muy poderosa y puede viajar por las distintas galaxias;
Khan es muy hábil y puede ser útil para varias misiones;
para misiones de recuperación donde requiera infiltrarse con personas del lugar, The Winter Soldier es la persona indicada;
Iron Man es un líder para planear misiones de defensa, además es un genio y domina el manejo de tecnología avanzada, cuenta con un 
traje muy poderoso;
cuando se requiere elegir cuál será la próxima acción para tomar y moverse rápidamente de un lugar a otro, es el propio Nick Fury es 
la opción más lógica;
Thor tiene el poder para destruir ejércitos completos;
no se debe utilizar árbol balanceado.



La idea es: nodo intermedio = pregunta, y nodo hoja = Superheroe. Se podria hacer una funcion con altura.
ó hijo izq = superheroe, hijo dcho = siguiente pregunta

"""
# Construcción de un árbol de decisión para asignar Vengadores

def altura_arbol(raiz):
    """Devuelve la altura del árbol."""
    if raiz is None:
        return 0
    return 1 + max(altura_arbol(raiz.izquierdo), altura_arbol(raiz.derecho))

def construir_arbol_decision():
    """
    Construye manualmente el árbol de decisión con preguntas en nodos internos
    y héroes en hojas. Hijo izquierdo = respuesta 'sí'; hijo derecho = 'no'.
    """
    # Crear todos los nodos
    root = nodoArbol("¿Es misión intergaláctica?")
    equipo = nodoArbol("¿Requiere trabajo en equipo?")
    destruccion = nodoArbol("¿Es misión de destrucción?")
    infiltracion = nodoArbol("¿Requiere paso desapercibido?")
    defensa = nodoArbol("¿Es misión de defensa o recuperación?")
    planificacion = nodoArbol("¿Necesita tecnología avanzada?")
    accion_rapida = nodoArbol("¿Necesita acción rápida?")

    # Hojas
    root.izquierdo = equipo               # sí → ¿trabajo en equipo?
    root.derecho   = destruccion          # no → ¿destrucción?

    equipo.izquierdo = nodoArbol("Khan")             # sí→Khan
    equipo.derecho   = nodoArbol("Capitana Marvel") # no→Capitana Marvel

    destruccion.izquierdo = nodoArbol("Thor")        # sí→Thor
    destruccion.derecho   = infiltracion            # no→¿infiltración?

    infiltracion.izquierdo = nodoArbol("The Winter Soldier")  # sí→Winter Soldier
    infiltracion.derecho   = nodoArbol("Ant-Man")             # no→Ant-Man

    defensa.izquierdo = nodoArbol("Capitán América")  # sí+tecnología=no→CapAm
    defensa.derecho   = nodoArbol("Iron Man")         # sí+tech=IronMan

    planificacion.izquierdo = defensa     # sí→¿defensa?
    planificacion.derecho   = nodoArbol("Nick Fury")     # no→Nick Fury

    accion_rapida.izquierdo = planificacion  # sí→planificación/defensa
    accion_rapida.derecho   = nodoArbol("Nick Fury") # no→Nick Fury

    # Conectar el subárbol de decisión final
    infiltracion.derecho = accion_rapida  # tras infiltración=no→acción rápida

    return root

def elegir_heroe(raiz):
    """
    Recorre el árbol de decisión interactivo:
    en cada nodo pregunta al usuario y baja por izquierda (sí) o derecha (no).
    Devuelve la hoja alcanzada (nombre de héroe).
    """
    nodo = raiz
    while nodo:
        # Si es hoja (ambos hijos None), devolvemos el héroe
        if nodo.izquierdo is None and nodo.derecho is None:
            return nodo.info
        # Preguntar al usuario
        resp = input(nodo.info + " (s/n): ").strip().lower()
        if resp == 's':
            nodo = nodo.izquierdo
        else:
            nodo = nodo.derecho

if __name__ == "__main__":
    arbol = construir_arbol_decision()
    print("Altura del árbol de decisión:", altura_arbol(arbol))
    heroe = elegir_heroe(arbol)
    print("Héroe recomendado:", heroe)


