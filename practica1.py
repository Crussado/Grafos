#! /usr/bin/python

# 1ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos
# Grafos simples dirigidos

import sys

def control_aristas(aristas, arista):
    return not arista in aristas

def control_vertices(vertices, arista):
    return arista[0] in vertices and arista[1] in vertices

'''
Lee un grafo desde entrada estandar y devuelve su representacion como lista.
Ejemplo Entrada: 
    3
    A
    B
    C
    A B
    B C
    C B
Ejemplo retorno: 
    (['A','B','C'],[('A','B'),('B','C'),('C','B')])
'''
def lee_grafo_stdin():
    cant_vert = int(input('Ingrese cant de vertice\n'))
    vertices = []

    for i in range(cant_vert):
        vertices += [input('Ingrese un vértice: ')]

    entrada = input('Ingrese las aristas, fin para terminar\n')
    aristas = []
    while entrada != 'fin':
        aux = entrada.split()
        arista = (aux[0], aux[2])
        if control_vertices(vertices, arista) and control_aristas(aristas, arista):
            aristas += [arista]
        entrada = input()

    return (vertices, aristas)

    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
def lee_grafo_archivo(file_path):
    vertices = []
    aristas = []
    f = open(file_path, 'r')
    cant = int(f.readline())

    for i in range(cant):
        vertices += [f.readline()]

    linea = f.readline()
    while linea:
        aux = linea.split()
        arista = (aux[0], aux[2])
        if control_vertices(vertices, arista) and control_aristas(aristas, arista):
            aristas += [arista]
        linea = f.readline()

    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
def imprime_grafo_lista(grafo):
    print(grafo)

    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de incidencia.
    '''
def lista_a_incidencia(grafo_lista):
    vertices, aristas = grafo_lista
    cant = len(vertices)
    matriz = []

    for arista in aristas:
        fila = [0 * cant]
        saliente = vertices.index(arista[0])
        entrante = vertices.index(arista[1])
        fila[entrante] = 1
        fila[saliente] = -1
        matriz += [fila]

    return (vertices, matriz)

    '''
    Transforma un grafo representado una matriz de incidencia a su 
    representacion por listas.
    '''
def incidencia_a_lista(grafo_incidencia):
    vertices, matriz = grafo_incidencia
    aristas = []

    for linea in matriz:
        saliente = vertices[linea.index(-1)]
        entrante = vertices[linea.index(1)]
        aristas += (saliente, entrante)

    return (vertices, aristas)


    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de incidencia.
    '''
def imprime_grafo_incidencia(grafo_incidencia):
    print(grafo_incidencia)

    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de adyacencia.
    '''
def lista_a_adyacencia(grafo_lista):
    vertices, aristas = grafo_lista
    matriz = []
    cant = len(vertices)

    for vertice in vertices:
        linea = [0 * cant]
        for saliente, entrante in aristas:
            if vertice == saliente:
                linea[vertices.index(entrante)] = 1
        matriz += [linea]

    return (vertices, matriz)

    '''
    Transforma un grafo representado una matriz de adyacencia a su 
    representacion por listas.
    '''
def adyacencia_a_lista(grafo_adyacencia):
    vertices, matriz = grafo_adyacencia
    aristas = []
    cant = len(vertices)

    for index in range(cant):
        vertice = vertices[index]
        linea = matriz[index]
        for i in range(cant):
            if linea[i]:
                aristas += [(vertice, vertices[i])]

    return (vertices, aristas)

    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de adyacencia.
    '''
def imprime_grafo_adyacencia(grafo_adyacencia):
    print(grafo_adyacencia)

#################### FIN EJERCICIO PRACTICA ####################
grafo_adyacencia1 = (
    ['A', 'B', 'C', 'D'], 
    [[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],]
)

grafo_adyacencia2 = (
    ['A', 'B', 'C', 'D'], 
    [[0, 2, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],]
)

# import sys
def lee_entrada_0():
	count = 0
	for line in sys.stdin:
		count = count + 1
		print ('Linea: [{0}]'.format(line.strip()))
	print ('leidas {0} lineas'.format(count))

def lee_entrada_1():
	count = 0
	try:
		while True:
			line = input().strip()
			count = count + 1
			print ('Linea: [{0}]'.format(line))
	except EOFError:
		pass
	print ('leidas {0} lineas'.format(count))

def lee_archivo(file_path):
	print ('leyendo archivo: {0}'.format(file_path))
	count = 0

	with open(file_path, 'r') as f:
		first_line = f.readline()
		print ('primer linea: [{}]'.format(first_line))
		for line in f:
			count = count + 1
			#print 'Linea: [{0}]'.format(line)	
	print ('leidas {0} lineas'.format(count))


def main():
	lee_grafo_stdin()

if __name__ == '__main__':
    main()
