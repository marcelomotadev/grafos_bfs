from collections import deque

def bfs_com_distancia(lista_vizinhos, vertice_inicial, vertice_destino):
    visitados = set()
    fila = deque()
    fila.append((vertice_inicial, 0))  # Tupla (vértice, distância)
    visitados.add(vertice_inicial)

    while fila:
        vertice_atual, distancia_atual = fila.popleft()
        if vertice_atual == vertice_destino:
            return distancia_atual  # Se o vértice de destino for encontrado, retorne a distância

        for vizinho in lista_vizinhos.get(vertice_atual, []):
            if vizinho not in visitados:
                fila.append((vizinho, distancia_atual + 1))
                visitados.add(vizinho)

    # Se o vértice de destino não for alcançado, retorne -1 ou outro valor adequado
    return -1

# Vértices de origem e destino
vertice_origem = 'A'
vertice_destino = 'T'

lista_vizinhos = { 
  'A': ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 
  'B': ['A', 'G', 'H'],
  'C': ['A', 'D', 'I'], 
  'D': ['A', 'C', 'I', 'N', 'L'], 
  'E': ['A', 'F'], 
  'F': ['A', 'E', 'J'], 
  'G': ['A', 'B', 'I', 'J', 'K'], 
  'H': ['A', 'B', 'I'], 
  'I': ['A', 'C', 'D', 'H', 'N', 'G', 'R', 'Q'], 
  'J': ['G', 'F'], 
  'K': ['G', 'P', 'Q', 'O'], 
  'L': ['D', 'M'], 
  'M': ['L', 'N'], 
  'N': ['I', 'D', 'M', 'S'], 
  'O': ['K'], 
  'P': ['K', 'U'], 
  'Q': ['K', 'U', 'I'], 
  'R': ['I', 'S', 'V', 'U'], 
  'S': ['R', 'T', 'N'], 
  'T': ['S'], 
  'U': ['R', 'Q', 'P', 'W'], 
  'V': ['R', 'W'], 
  'W': ['V', 'U', 'X', 'Z', 'Y'], 
  'X': ['W', 'Y'], 
  'Y': ['X', 'Z', 'W'], 
  'Z': ['W', 'Y']
}

# Encontre a distância entre os vértices
distancia = bfs_com_distancia(lista_vizinhos, vertice_origem, vertice_destino)

if distancia != -1:
    print(f"A distância entre {vertice_origem} e {vertice_destino} é {distancia}.")
else:
    print(f"Não há caminho entre {vertice_origem} e {vertice_destino}.")
