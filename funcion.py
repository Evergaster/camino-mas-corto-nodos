class Vertice:
    def __init__(self, destino, costo):
        """
        Inicializa un vértice con un destino y un costo.
        
        Parámetros:
        destino (Nodo): El nodo al que conecta este vértice.
        costo (int): El costo de la arista que conecta con el destino.
        """
        self.destino = destino  # El nodo al que conecta el vértice
        self.costo = costo      # El costo de la arista

class Nodo:
    def __init__(self, nombre):
        """
        Inicializa un nodo con un nombre y una lista de vértices (aristas).
        
        Parámetros:
        nombre (str): El nombre del nodo.
        """
        self.nombre = nombre            # El nombre del nodo
        self.vertices = []              # Lista de vértices (aristas) conectadas al nodo

    def agregar_vertice(self, destino, costo):
        """
        Agrega un vértice (arista) al nodo actual, conectándolo con otro nodo.

        Parámetros:
        destino (Nodo): El nodo al que conecta la arista.
        costo (int): El costo de la arista que conecta con el destino.
        """
        self.vertices.append(Vertice(destino, costo))

class Grafo:
    def __init__(self):
        """
        Inicializa un grafo vacío. El grafo se representa como un diccionario de nodos.
        """
        self.nodos = {}  # Diccionario de nodos, donde la clave es el nombre del nodo

    def agregar_nodo(self, nombre):
        """
        Agrega un nodo al grafo si no existe ya.

        Parámetros:
        nombre (str): El nombre del nodo a agregar.
        """
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)

    def agregar_arista(self, origen, destino, costo):
        """
        Agrega una arista entre dos nodos, de 'origen' a 'destino' con un costo.
        Esto es para un grafo no dirigido, por lo que la arista se agrega en ambos sentidos.

        Parámetros:
        origen (str): El nombre del nodo de origen.
        destino (str): El nombre del nodo de destino.
        costo (int): El costo de la arista entre el origen y el destino.
        """
        self.agregar_nodo(origen)  # Asegura que el nodo de origen existe
        self.agregar_nodo(destino) # Asegura que el nodo de destino existe

        nodo_origen = self.nodos[origen]  # Obtiene el nodo de origen
        nodo_destino = self.nodos[destino]  # Obtiene el nodo de destino

        # Añade la arista al nodo de origen y al de destino (grafo no dirigido)
        nodo_origen.agregar_vertice(nodo_destino, costo)
        nodo_destino.agregar_vertice(nodo_origen, costo)

    def encontrar_todos_caminos(self, inicio, fin):
        """
        Encuentra todos los caminos posibles entre dos nodos utilizando
        búsqueda en profundidad (DFS) y devuelve una lista de caminos con su costo.

        Parámetros:
        inicio (str): El nombre del nodo de inicio.
        fin (str): El nombre del nodo de fin.

        Retorna:
        list: Lista de tuplas, cada una conteniendo un camino (lista de nodos) y su costo.
        """
        def dfs(actual, destino, visitados, camino_actual, costo_actual):
            """
            Función recursiva para realizar la búsqueda en profundidad (DFS) desde un nodo actual
            hasta el nodo de destino, explorando todas las rutas posibles.

            Parámetros:
            actual (Nodo): El nodo actual en la búsqueda.
            destino (Nodo): El nodo de destino.
            visitados (set): Conjunto de nodos visitados para evitar ciclos.
            camino_actual (list): Lista de nodos en el camino actual.
            costo_actual (int): El costo acumulado hasta el nodo actual.
            """
            if actual == destino:
                # Si el nodo actual es el destino, se agrega el camino encontrado
                # y su costo a la lista de caminos.
                caminos.append((list(camino_actual), costo_actual))
                return

            visitados.add(actual)  # Marca el nodo como visitado

            # Recorre todos los vértices (aristas) del nodo actual
            for vertice in actual.vertices:
                if vertice.destino not in visitados:
                    # Si el destino del vértice no ha sido visitado, sigue explorando
                    camino_actual.append(vertice.destino.nombre)  # Agrega el nodo al camino
                    dfs(vertice.destino, destino, visitados, camino_actual, costo_actual + vertice.costo)
                    camino_actual.pop()  # Retrocedemos, eliminamos el nodo del camino

            visitados.remove(actual)  # Desmarca el nodo como visitado para otras exploraciones

        # Si alguno de los nodos de inicio o fin no existe, muestra un error.
        if inicio not in self.nodos or fin not in self.nodos:
            print("Uno o ambos nodos no existen en el grafo.")
            return []

        nodo_inicio = self.nodos[inicio]  # Obtiene el nodo de inicio
        nodo_fin = self.nodos[fin]        # Obtiene el nodo de fin
        caminos = []                      # Lista para almacenar los caminos encontrados
        dfs(nodo_inicio, nodo_fin, set(), [inicio], 0)  # Inicia la búsqueda desde el nodo de inicio
        return caminos

    def __str__(self, inicio, fin):
        """
        Retorna una representación en cadena del grafo, mostrando todos los caminos
        entre dos nodos especificados, así como el camino más corto.

        Parámetros:
        inicio (str): El nombre del nodo de inicio.
        fin (str): El nombre del nodo de fin.

        Retorna:
        str: Una cadena con los caminos y el camino más corto entre los nodos.
        """
        caminos = self.encontrar_todos_caminos(inicio, fin)

        if not caminos:
            # Si no se encuentran caminos, se informa al usuario.
            print(f"No se encontraron caminos entre {inicio} y {fin}.")
            return

        # Muestra todos los caminos encontrados y sus costos.
        print(f"Todos los caminos entre {inicio} y {fin}:")
        for camino, costo in caminos:
            print(f"Camino: {' -> '.join(camino)}, Costo: {costo}")

        # Encuentra el camino más corto utilizando la función 'min' con base en el costo.
        camino_mas_corto = min(caminos, key=lambda x: x[1])
        print("\nEl camino más corto:")
        # Muestra el camino más corto y su costo.
        print(f"Camino: {' -> '.join(camino_mas_corto[0])}, Costo: {camino_mas_corto[1]}")
