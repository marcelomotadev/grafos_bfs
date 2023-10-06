from collections import deque

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

# Vértices de origem e destino
vertice_origem = 'N'
vertice_destino = 'O'

lista_vizinhos = { 
  'A': ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 
  'B': ['A', 'G', 'H'],
  'C': ['A', 'I', 'N'], 
  'D': ['A', 'I', 'N', 'L'], 
  'E': ['A', 'F'], 
  'F': ['A', 'E', 'J'], 
  'G': ['A', 'B', 'I', 'J', 'K'], 
  'H': ['A', 'B', 'I'], 
  'I': ['A', 'C', 'D', 'H', 'G', 'R', 'Q'], 
  'J': ['G', 'F'], 
  'K': ['G', 'P', 'Q', 'O'], 
  'L': ['D', 'M'], 
  'M': ['L', 'N'], 
  'N': ['D', 'M', 'S'], 
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
distancia = bfs_com_caminho(lista_vizinhos, vertice_origem, vertice_destino)

def caminho(lista):
    resultado = ' > '.join(lista)
    return resultado

if distancia != -1:
    print(f"A distância entre {vertice_origem} e {vertice_destino} é: {len(distancia) - 1} e o caminho é: {caminho(distancia)}.")
else:
    print(f"Não há caminho entre {vertice_origem} e {vertice_destino}.")
