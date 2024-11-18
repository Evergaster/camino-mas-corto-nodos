class Vertice:
    def __init__(self, destino, costo):
        self.destino = destino
        self.costo = costo


class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vertices = []

    def agregar_vertice(self, destino, costo):
        self.vertices.append(Vertice(destino, costo))


class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)

    def agregar_arista(self, origen, destino, costo):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)

        nodo_origen = self.nodos[origen]
        nodo_destino = self.nodos[destino]
        nodo_origen.agregar_vertice(nodo_destino, costo)
        nodo_destino.agregar_vertice(nodo_origen, costo)

    def encontrar_todos_caminos(self, inicio, fin):
        def dfs(actual, destino, visitados, camino_actual, costo_actual):

            if actual == destino:
                caminos.append((list(camino_actual), costo_actual))
                return

            visitados.add(actual)

            for vertice in actual.vertices:
                if vertice.destino not in visitados:
                    camino_actual.append(vertice.destino.nombre)
                    dfs(vertice.destino, destino, visitados, camino_actual, costo_actual + vertice.costo)
                    camino_actual.pop()  # Retrocedemos


            visitados.remove(actual)

        if inicio not in self.nodos or fin not in self.nodos:
            print("Uno o ambos nodos no existen en el grafo.")
            return []

        nodo_inicio = self.nodos[inicio]
        nodo_fin = self.nodos[fin]
        caminos = []
        dfs(nodo_inicio, nodo_fin, set(), [inicio], 0)
        return caminos

    def __str__(self, inicio, fin):
        caminos = self.encontrar_todos_caminos(inicio, fin)

        if not caminos:
            print(f"No se encontraron caminos entre {inicio} y {fin}.")
            return

        print(f"Todos los caminos entre {inicio} y {fin}:")
        for camino, costo in caminos:
            print(f"Camino: {' -> '.join(camino)}, Costo: {costo}")

        # Encontramos el camino más corto
        camino_mas_corto = min(caminos, key=lambda x: x[1])
        print("\nEl camino más corto:")
        print(f"Camino: {' -> '.join(camino_mas_corto[0])}, Costo: {camino_mas_corto[1]}")
