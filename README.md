# Proyecto de Grafos

Este proyecto implementa un grafo y permite agregar nodos y aristas, así como encontrar todos los caminos entre dos nodos.

## Archivos

### `funcion.py`

Este archivo define las clases `Vertice`, `Nodo` y `Grafo` para representar un grafo.

#### Clases

##### `Vertice`
Representa una arista en el grafo.

- **Atributos:**
  - `destino`: Nodo destino del vértice.
  - `costo`: Costo de la arista.

- **Métodos:**
  - `__init__(self, destino, costo)`: Inicializa un vértice con el nodo destino y el costo.

##### `Nodo`
Representa un nodo en el grafo.

- **Atributos:**
  - `nombre`: Nombre del nodo.
  - `vertices`: Lista de vértices conectados al nodo.

- **Métodos:**
  - `__init__(self, nombre)`: Inicializa un nodo con un nombre.
  - `agregar_vertice(self, destino, costo)`: Agrega un vértice al nodo.

##### `Grafo`
Representa un grafo.

- **Atributos:**
  - `nodos`: Diccionario de nodos en el grafo.

- **Métodos:**
  - `__init__(self)`: Inicializa un grafo vacío.
  - `agregar_nodo(self, nombre)`: Agrega un nodo al grafo.
  - `agregar_arista(self, origen, destino, costo)`: Agrega una arista entre dos nodos en el grafo.
  - `encontrar_todos_caminos(self, inicio, fin)`: Encuentra todos los caminos entre dos nodos.
  - `__str__(self, inicio, fin)`: Imprime todos los caminos entre dos nodos y el camino más corto.

### `index.py`

Este archivo contiene un script para interactuar con el usuario y construir un grafo.

#### Funciones

##### `main()`
Función principal que ejecuta el script.

- **Descripción:**
  - Solicita al usuario la cantidad de nodos y aristas para construir un grafo.
  - Permite al usuario ingresar los nodos y aristas.
  - Imprime todos los caminos entre dos nodos especificados por el usuario.
  - Permite al usuario continuar agregando nodos y aristas o salir del programa.

- **Flujo:**
  1. Solicita la cantidad de nodos y los nombres de los nodos.
  2. Solicita la cantidad de aristas y los detalles de las aristas (origen, destino, costo).
  3. Solicita el nodo de inicio y el nodo de fin.
  4. Imprime todos los caminos entre el nodo de inicio y el nodo de fin.
  5. Pregunta al usuario si desea continuar o salir.

### Ejecución

Para ejecutar el script, simplemente corre el archivo `index.py`:

```sh
python [index.py](http://_vscodecontentref_/0)