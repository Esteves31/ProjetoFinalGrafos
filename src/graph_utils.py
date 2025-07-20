import networkx as nx
import matplotlib.pyplot as plt

def print_matriz(matriz):
    for i, row in enumerate(matriz):
        row_str = " ".join(f"{val:>4}" for val in row)
        print(row_str)

def print_adjacency_list(adj):
    """Imprime a lista de adjacência de forma legível, com vizinhos e labels."""
    # Determina largura máxima de rótulo de nó para alinhamento
    max_label_len = max(len(str(node)) for node in adj)
    for node, neighbors in adj.items():
        label = str(node).ljust(max_label_len)
        if neighbors:
            neigh_str = ", ".join(f"{dest}(lbl={lbl})" for dest, lbl in neighbors)
        else:
            neigh_str = "<nenhum>"
        print(f"{label} -> {neigh_str}")

def construir_matriz_adjacencia(nodes, edges):
    """Constrói a matriz de adjacência."""
    n = len(nodes)
    matriz = [[0] * n for _ in range(n)]  # Inicializa com zeros
    indice = {v: i for i, v in enumerate(nodes)}  # Mapeia IDs para índices
    
    for origem, destino, _ in edges:
        if origem in indice and destino in indice:  # Verifica se os IDs existem
            i = indice[origem]
            j = indice[destino]
            matriz[i][j] = 1  # Grafo direcionado
            matriz[j][i] = 1  # Descomente para grafo não direcionado

    return matriz

def build_incidence_matrix(nodes, edges):
    n = len(nodes)
    m = len(edges)
    incidence_matrix = [[0] * m for _ in range(n)]
    node_index = {node: idx for idx, node in enumerate(nodes)} 
    
    for edge_idx, (source, target, _) in enumerate(edges):
        if source in node_index:
            incidence_matrix[node_index[source]][edge_idx] = 1
        if target in node_index:
            incidence_matrix[node_index[target]][edge_idx] = 1
    return incidence_matrix

def build_adjacency_list(nodes, edges):
    """Constrói uma lista de adjacência, incluindo vértices que aparecem apenas em arestas."""
    adjacency_list = {node: [] for node in nodes}
    for source, target, label in edges:
        # Garante que qualquer vértice presente nas arestas exista no dicionário
        if source not in adjacency_list:
            adjacency_list[source] = []
        if target not in adjacency_list:
            adjacency_list[target] = []
        adjacency_list[source].append((target, label))
        adjacency_list[target].append((source, label))  # para grafo não direcionado
    return adjacency_list

def graph_from_adjacency_matrix(nodes, adjacency_matrix, edges):
    G = nx.Graph()
    for i, node in enumerate(nodes):
        G.add_node(node)

    edge_labels_dict = {(source, target): label for source, target, label in edges}
    edge_labels_dict.update({(target, source): label for source, target, label in edges})  # Para grafos não direcionados

    n = len(nodes)
    for i in range(n):
        for j in range(i, n):  # Se for grafo não direcionado
            if adjacency_matrix[i][j] == 1:
                label = edge_labels_dict.get((nodes[i], nodes[j]), '')
                G.add_edge(nodes[i], nodes[j], label=label)
    return G

def graph_from_incidence_matrix(nodes, incidence_matrix, edges):
    G = nx.Graph()
    for i, node in enumerate(nodes):
        G.add_node(node)

    n = len(nodes)
    m = len(incidence_matrix[0])

    for j in range(m):  # Cada coluna é uma aresta
        connected_nodes = []
        for i in range(n):
            if incidence_matrix[i][j] == 1:
                connected_nodes.append(nodes[i])

        if len(connected_nodes) == 2:
            source, target = connected_nodes
            _, _, label = edges[j]  # Como cada coluna representa uma aresta na ordem do edges
            G.add_edge(source, target, label=label)
    return G

def graph_from_adjacency_list(adjacency_list):
    G = nx.Graph()  # Usa nx.DiGraph() se for dirigido

    for node, neighbors in adjacency_list.items():
        G.add_node(node)
        for neighbor, label in neighbors:
            if not G.has_edge(node, neighbor):  # Evitar adicionar aresta duplicada (para grafos não direcionados)
                G.add_edge(node, neighbor, label=label)
    return G

def plot_graph(G, title="Grafo", node_color='skyblue', edge_color='gray', edge_label_color='red', layout_k=0.9, save_as=None):
    """Plota o grafo fornecido com opções de customização."""
    
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, k=layout_k)

    nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=700)
    nx.draw_networkx_edges(G, pos, edge_color=edge_color)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    edge_labels = nx.get_edge_attributes(G, 'label')
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color=edge_label_color)

    plt.title(title)
    plt.axis('off')

    if save_as:
        plt.savefig(save_as)
        print(f"Imagem salva como '{save_as}'")
    else:
        plt.show()

def n_vertices_adj(A):          # matriz de adjacência
    return len(A)

def n_vertices_inc(I):          # matriz de incidência
    return len(I)

def n_vertices_lst(L):          # lista de adjacência
    return len(L)

# 2.2
def n_arestas_adj(A):
    n = len(A)
    total = sum(A[i][j] for i in range(n) for j in range(n))
    return total // 2

def n_arestas_inc(I):
    return len(I[0])            # colunas = arestas

def n_arestas_lst(L):
    total = sum(len(v) for v in L.values())
    return total // 2           # não-dirigido

# 2.3
def adjacentes_adj(v, nodes, A):
    idx = nodes.index(v)
    return [nodes[j] for j, x in enumerate(A[idx]) if x]

def adjacentes_inc(v, nodes, I):
    idx = nodes.index(v)
    m = len(I[0])
    viz = set()
    for e in range(m):
        if I[idx][e]:
            for u_i, linha in enumerate(I):
                if u_i != idx and linha[e]:
                    viz.add(nodes[u_i])
    return list(viz)

def adjacentes_lst(v, L):
    return [u for u, _ in L.get(v, [])]

# 2.4
def existe_aresta_adj(u, v, nodes, A):
    i, j = nodes.index(u), nodes.index(v)
    return bool(A[i][j])

def existe_aresta_inc(u, v, nodes, I):
    iu, iv = nodes.index(u), nodes.index(v)
    for col in zip(*I):              # percorre colunas
        if col[iu] and col[iv]:
            return True
    return False

def existe_aresta_lst(u, v, L):
    return any(nei == v for nei, _ in L.get(u, []))

# 2.5
def grau_adj(v, nodes, A):
    return sum(A[nodes.index(v)])

def grau_inc(v, nodes, I):
    return sum(I[nodes.index(v)])

def grau_lst(v, L):
    return len(L.get(v, []))

# 2.6
def graus_adj(nodes, A):
    return {v: grau_adj(v, nodes, A) for v in nodes}

def graus_inc(nodes, I):
    return {v: grau_inc(v, nodes, I) for v in nodes}

def graus_lst(L):
    return {v: len(neis) for v, neis in L.items()}

# 2.7
from collections import deque

def caminho_simples_bfs_lst(orig, dest, L):
    queue = deque([(orig, [orig])])
    visited = {orig}
    while queue:
        v, path = queue.popleft()
        if v == dest:
            return path
        for nxt, _ in L.get(v, []):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None

# Wrappers para outras representações

def caminho_simples_bfs_adj(orig, dest, nodes, A):
    return caminho_simples_bfs_lst(orig, dest, matriz_para_lista(nodes, A))


def caminho_simples_bfs_inc(orig, dest, nodes, M):
    return caminho_simples_bfs_lst(orig, dest, incidencia_para_lista(nodes, M))

def matriz_para_lista(nodes, A):
    L = {v: [] for v in nodes}
    n = len(nodes)
    for i in range(n):
        for j in range(i, n):
            if A[i][j]:
                u, v = nodes[i], nodes[j]
                L[u].append((v, ''))
                if u != v:
                    L[v].append((u, ''))
    return L

def incidencia_para_lista(nodes, I):
    L = {v: [] for v in nodes}
    m = len(I[0])
    for e in range(m):
        extremos = [nodes[i] for i, linha in enumerate(I) if linha[e]]
        if len(extremos) == 2:
            u, v = extremos
            L[u].append((v, ''))
            L[v].append((u, ''))
    return L

# 2.8

def ciclo_em_v_bfs(v0, L):
    queue = deque([(v0, [v0])])
    visited = set()

    while queue:
        atual, caminho = queue.popleft()
        visited.add(atual)
        
        for vizinho, _ in L.get(atual, []):
            if vizinho == v0 and len(caminho) >= 3:
                return caminho + [v0]

            if vizinho not in visited:
                queue.append((vizinho, caminho + [vizinho]))
                
    return None

# Wrappers para ciclo em matriz e incidência

def ciclo_em_v_adj(v0, nodes, A): 
    return ciclo_em_v_bfs(v0, matriz_para_lista(nodes, A))

def ciclo_em_v_inc(v0, nodes, M): 
    return ciclo_em_v_bfs(v0, incidencia_para_lista(nodes, M))

def é_subgrafo_bfs_lst(Lsub, Lsup):
    visited = set()
    for start in Lsub:
        if start not in visited:
            queue = deque([start])
            visited.add(start)
            while queue:
                u = queue.popleft()
                # Extrai apenas os vértices de Lsub[u], ignorando o label
                sub_vizinhos = [v for v, _ in Lsub[u]]
                for v in sub_vizinhos:
                    # Também extrai apenas os vértices de Lsup[u], ignorando o label
                    sup_vizinhos = [x for x, _ in Lsup.get(u, [])]
                    if v not in sup_vizinhos:
                        return False
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
    return True


# Wrappers
def subgrafo_matriz(nodes1,A1,nodes2,A2): 
    return é_subgrafo_bfs_lst(matriz_para_lista(nodes1,A1), 
                              matriz_para_lista(nodes2,A2))

def subgrafo_incidencia(nodes1,M1,nodes2,M2): 
    return é_subgrafo_bfs_lst(incidencia_para_lista(nodes1,M1), 
                              incidencia_para_lista(nodes2,M2))

def excentricidade_todos_vertices(L):
    """
    Calcula a excentricidade de cada vértice em uma árvore.
    """
    excentricidades = {}
    for v in L:
        dist = {v: 0}
        queue = deque([v])
        while queue:
            u = queue.popleft()
            for w, _ in L[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        excentricidades[v] = max(dist.values())
    return excentricidades

def raio_arvore(L):
    """
    Calcula o raio da árvore (menor excentricidade).
    L: lista de adjacência
    Retorna: int (raio)
    """
    excentricidades = excentricidade_todos_vertices(L)
    return min(excentricidades.values())

def print_keys(grafos):
    keys = list(grafos.keys())
    if keys:
        for k in keys:
            print(f"-> {k}")