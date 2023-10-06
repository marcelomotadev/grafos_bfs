from collections import deque
from Graph import Graph

def bfs_com_caminho(lista_vizinhos, vertice_inicial, vertice_destino):
    visitados = set()
    fila = deque()
    fila.append((vertice_inicial, [vertice_inicial]))  # Tupla (vértice, caminho)
    visitados.add(vertice_inicial)

    while fila:
        vertice_atual, caminho_atual = fila.popleft()
        if vertice_atual == vertice_destino:
            return caminho_atual  # Se o vértice de destino for encontrado, retorne o caminho

        for vizinho in lista_vizinhos.get(vertice_atual, []):
            if vizinho not in visitados:
                novo_caminho = caminho_atual + [vizinho]
                fila.append((vizinho, novo_caminho))
                visitados.add(vizinho)

    # Se o vértice de destino não for alcançado, retorne -1 ou outro valor adequado
    return -1

def connect_vertices(graph, edge_dict):
  for vertices in edge_dict.values():
    for i in range(len(vertices)):
      for j in range(i + 1, len(vertices)):
        v = vertices[i]
        w = vertices[j]
        graph.add_edge(v, w)

if __name__ == '__main__':
    file = 'db.txt'

    edge_dict = {}

    with open(file, 'r') as file:
        content = file.read().splitlines()
        
    for line in content:
        left, right = map(str, line.split())
        
        if right not in edge_dict:
            edge_dict[right] = []
        edge_dict[right].append(left)

    graph = Graph()
    
    connect_vertices(graph, edge_dict)
    
    vertice_origem = 'N'
    vertice_destino = 'O'
    
    distancia = bfs_com_caminho(graph.adj_list, vertice_origem, vertice_destino)
    
    def caminho(lista):
        resultado = ' > '.join(lista)
        return resultado

    if distancia != -1:
        print(f"A distância entre {vertice_origem} e {vertice_destino} é: {len(distancia) - 1} e o caminho é: {caminho(distancia)}.")
    else:
        print(f"Não há caminho entre {vertice_origem} e {vertice_destino}.")
        
    print(f'Número de pesquisadores: {graph.num_vertices()}.')
    print(f'Número de colaborações: {graph.num_edges()}.')
    print(f'{graph.get_max_degree()[0]} foi/foram pesquisador que mais colaborou com {graph.get_max_degree()[1]} colaborações.')
    print(f'{graph.get_min_degree()[0]} foi/foram pesquisador que menos colaborou com {graph.get_min_degree()[1]} colaborações.')
    print(f'Número de subredes de colaboração: {graph.components()}.')
    
