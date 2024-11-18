from funcion import Grafo
import os
g = Grafo()

while True:
    cantNodos = int(input("Ingrese la cantidad de nodos: "))
    for i in range(cantNodos):
        nodo = input(f"Ingrese el nombre del nodo {i+1}: ")
        g.agregar_nodo(nodo)

    cantAristas = int(input("Ingrese la cantidad de aristas: "))
    for i in range(cantAristas):
        origen, destino, costo = input(f"Ingrese la arista {i+1} (origen destino costo): ").split()
        g.agregar_arista(origen, destino, int(costo))

    inicio = input("Ingrese el nodo de inicio: ")
    fin = input("Ingrese el nodo de fin: ")
    print(g.__str__(inicio, fin))
    continuar = input("Desea continuar? (s/n): ")
    if continuar.lower() != "s":
        break
    os.system("clear")



