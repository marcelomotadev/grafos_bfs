from collections import deque

def bfs(lista_vizinhos, vertice_inicial):
    visitados = set()
    fila = deque()
    fila.append(vertice_inicial)
    visitados.add(vertice_inicial)

    while fila:
        vertice_atual = fila.popleft()
        print(vertice_atual, end=' ')  # Você pode fazer qualquer ação desejada com o vértice aqui

        for vizinho in lista_vizinhos.get(vertice_atual, []):
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)

# Vértice inicial para começar a busca
vertice_inicial = 'A'

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

# Aplicar o algoritmo BFS
print("Resultado da busca em largura a partir de", vertice_inicial, ":")
bfs(lista_vizinhos, vertice_inicial)