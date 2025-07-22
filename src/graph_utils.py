from itertools import combinations
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


def uniao(vertices1, arestas1, vertices2, arestas2):
    vertices = list(set(vertices1).union(vertices2))
    arestas = list(set(arestas1).union(arestas2))
    return vertices, arestas

def intersecao(vertices1, arestas1, vertices2, arestas2):
    """Retorna a interseção de vértices e arestas usando set, considerando grafos não direcionados."""
    # Interseção de vértices como set
    vertices = list(set(vertices1).intersection(vertices2))
    # Normaliza arestas para ignorar orientação
    def normalizar(e):
        u, v, lbl = e
        return (min(u, v), max(u, v), lbl)
    set1 = {normalizar(e) for e in arestas1}
    set2 = {normalizar(e) for e in arestas2}
    # Interseção dos sets
    arestas = list(set1.intersection(set2))
    return vertices, arestas

def diferenca_simetrica(vertices1, arestas1, vertices2, arestas2):
    vertices = list(set(vertices1).union(vertices2))
    arestas = list(set(arestas1).symmetric_difference(arestas2))
    return vertices, arestas

def remover_vertice(vertices, arestas, vi):
    if vi not in vertices:
        print(f"Vértice {vi} não existe.")
        return vertices[:], arestas[:]
    new_vertices = [v for v in vertices if v != vi]
    new_arestas = [e for e in arestas if vi not in (e[0], e[1])]
    return new_vertices, new_arestas

def remover_aresta(vertices, arestas, ei):
    if ei not in arestas:
        print(f"Aresta {ei} não existe.")
        return vertices[:], arestas[:]
    new_arestas = [e for e in arestas if e != ei]
    return vertices[:], new_arestas

def fundir_vertices(vertices, arestas, vi, vj):
    if vi not in vertices or vj not in vertices:
        print(f"Vértices {vi} e/ou {vj} não existem.")
        return vertices[:], arestas[:]

    novo = f"{vi}_{vj}"
    new_vertices = [v for v in vertices if v != vi and v != vj]
    new_vertices.append(novo)

    new_arestas = set()
    for a, b, label in arestas:
        a_new = novo if a == vi or a == vj else a
        b_new = novo if b == vi or b == vj else b
        new_arestas.add((a_new, b_new, label))
    return new_vertices, list(new_arestas)


def is_connected(adj_list):
    visited = set()
    start = next(iter(adj_list))
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(nei for nei, _ in adj_list[node] if nei not in visited)
    return len(visited) == len(adj_list)

def grau_lst(v, L):
    return len(L.get(v, []))

def is_eulerian_from_list(adj_list):
    """Verifica se o grafo (representado por lista de adjacência) é euleriano."""
    if not is_connected(adj_list):
        return False
    return all(grau_lst(v, adj_list) % 2 == 0 for v in adj_list)

def graph_intersection_from_list(L1, L2):
    intersec = {}
    for node in L1:
        if node in L2:
            viz1 = set((v, lbl) for v, lbl in L1[node])
            viz2 = set((v, lbl) for v, lbl in L2[node])
            comuns = viz1 & viz2
            if comuns:
                intersec[node] = list(comuns)
    return intersec

def held_karp_hamiltonian_from_list(adj_list):
    nodes = list(adj_list.keys())
    n = len(nodes)
    node_idx = {node: i for i, node in enumerate(nodes)}
    idx_node = {i: node for i, node in enumerate(nodes)}

    dp = {}

    for k in range(1, n):
        if nodes[k] in [v for v, _ in adj_list[nodes[0]]]:
            dp[(1 << 0) | (1 << k), k] = [0, k]

    for subset_size in range(3, n + 1):
        for subset in combinations(range(n), subset_size):
            if 0 not in subset:
                continue
            bits = sum(1 << i for i in subset)
            for k in subset:
                if k == 0:
                    continue
                prev_bits = bits & ~(1 << k)
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    if (prev_bits, m) in dp and nodes[k] in [v for v, _ in adj_list[nodes[m]]]:
                        new_path = dp[(prev_bits, m)] + [k]
                        dp[(bits, k)] = new_path

    full_bits = (1 << n) - 1
    for k in range(1, n):
        if (full_bits, k) in dp and nodes[0] in [v for v, _ in adj_list[nodes[k]]]:
            path = dp[(full_bits, k)] + [0]
            path_nodes = [nodes[i] for i in path]
            edges = [(path_nodes[i], path_nodes[i+1]) for i in range(len(path_nodes)-1)]
            return True, edges

    return False, []


def is_subgraph(nodes, edges, subnodes, subedges):
    sub_adjacency_list = build_adjacency_list(subnodes, subedges)
    sub_graph = graph_from_adjacency_list(sub_adjacency_list)
    main_adjacency_list = build_adjacency_list(nodes, edges)
    main_graph = graph_from_adjacency_list(main_adjacency_list)

    n = len(nodes)
    m = len(edges)
    sub_n = len(subnodes)
    sub_m = len(subedges)

    if sub_n > n or sub_m > m:
        return False

    for i in range(n - sub_n + 1):
        for j in range(m - sub_m + 1):
            subgraph_found = True
            for k in range(sub_n):
                if nodes[i + k] not in subnodes:
                    subgraph_found = False
                    break

    return subgraph_found

def is_tree_from_list(adj_list):
    n_vertices = len(adj_list)
    n_arestas = sum(len(neis) for neis in adj_list.values()) // 2  # grafo não-direcionado

    return is_connected(adj_list) and n_arestas == n_vertices - 1


def is_spanning_tree(nodes, edges, tree_nodes, tree_edges):
    L_tree = build_adjacency_list(tree_nodes, tree_edges)
    if is_tree_from_list(L_tree):
        return set(tree_nodes) == set(nodes) and set(tree_edges).issubset(set(edges))
    return False

def is_tree(nodes, edges):
    n = len(nodes)
    m = len(edges)

    if m != n - 1:
        return False

    if n == 0 or n == 1:
        return True

    adjacency_list = build_adjacency_list(nodes, edges)
    visited = set()
    queue = deque()

    start_node = nodes[0]
    queue.append(start_node)
    visited.add(start_node)

    while queue:
        node = queue.popleft()

        for neighbor, _ in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return len(visited) == n

def find_tree_centers(nodes, edges):
    """
    Encontra o(s) centro(s) de uma árvore usando o algoritmo de poda de folhas.
    Retorna uma lista contendo os IDs dos nós centrais.
    """
    n = len(nodes)

    if n <= 2:
        return nodes

    adj = build_adjacency_list(nodes, edges)
    degrees = {node: len(adj[node]) for node in nodes}

    # 1. Encontrar a primeira camada de folhas
    leaves = deque()
    for node in nodes:
        if degrees[node] == 1:
            leaves.append(node)

    # 2. Remover as folhas camada por camada até restarem 1 ou 2 nós
    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_in_this_layer = len(leaves)
        remaining_nodes -= leaves_in_this_layer

        for _ in range(leaves_in_this_layer):
            leaf = leaves.popleft()
            # O vizinho de uma folha é o único elemento em sua lista de adjacência
            for neighbor, _ in adj[leaf]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    leaves.append(neighbor)

    centers = list(leaves)
    return centers

def find_cycle(adj, start_node, parent, visited, path):
    visited.add(start_node)
    path.append(start_node)

    for neighbor in adj.get(start_node, []):
        if neighbor not in visited:
            result = find_cycle(adj, neighbor, start_node, visited, path)
            if result:
                return result
        elif neighbor != parent and neighbor in path:
            # Cycle detected
            cycle_start_index = path.index(neighbor)
            return path[cycle_start_index:] + [neighbor] # Return the cycle including the start node again

    path.pop() # Backtrack
    return None


#Encontra k árvores de abrangencia diferentes de A1, adicionando uma aresta de G
#que não está em A1, detectando o ciclo formado, e removendo uma aresta diferente desse ciclo.
def find_kspanning_trees(vertices, arestas, arestas_abrangencia, k):
    if not is_spanning_tree(vertices, arestas, vertices, arestas_abrangencia):
         print("A floresta de abrangência inicial não é válida.")
         return []

    spanning_trees = []
    initial_tree_edges = set(arestas_abrangencia)
    graph_edges = set(arestas)


    edges_to_add = list(graph_edges - initial_tree_edges)

    if not edges_to_add:
        print("Não há arestas para adicionar para formar novas árvores de abrangência.")
        return []

    temp_graph_adj = build_adjacency_list(vertices, arestas_abrangencia)

    for new_edge in edges_to_add:
        if len(spanning_trees) >= k:
            break

        u, v = new_edge

        temp_adj_copy = {node: neighbors[:] for node, neighbors in temp_graph_adj.items()}

        if u in temp_adj_copy and v not in temp_adj_copy[u]:
             temp_adj_copy[u].append(v)
        if v in temp_adj_copy and u not in temp_adj_copy[v]:
             temp_adj_copy[v].append(u)


        visited = set()
        path = []
        cycle = find_cycle(temp_adj_copy, u, None, visited, path)


        if cycle and new_edge in cycle or (v,u) in cycle:

            cycle_edges = set()
            for i in range(len(cycle) - 1):
                edge = tuple(sorted((cycle[i], cycle[i+1])))
                cycle_edges.add(edge)

            edges_in_cycle_and_tree = list(cycle_edges.intersection(initial_tree_edges))


            for edge_to_remove in edges_in_cycle_and_tree:
                if len(spanning_trees) >= k:
                    break

                new_tree_edges = list(initial_tree_edges - {edge_to_remove} | {new_edge})


                if is_spanning_tree(vertices, arestas, vertices, new_tree_edges) and set(new_tree_edges) not in [set(t) for t in spanning_trees]:
                    spanning_trees.append(new_tree_edges)
                    print(f"\nFound Spanning Tree {len(spanning_trees)}:")
                    print(new_tree_edges)

    return spanning_trees

def calcula_distancia_arestas(A1, A2):
    arestas_a1 = set() # funcao set() gera um array vazio
    for u in A1:
        for v in A1[u]:
            # funcao frozenset() é para evitar duplicata ({u,v} e {v,u} são iguais)
            arestas_a1.add(frozenset({u, v}))

    arestas_a2 = set()
    for u in A2:
        for v in A2[u]:
            arestas_a2.add(frozenset({u, v}))

    # distância é o número de arestas que estão em A1 mas não em A2, mais as que estão em A2 mas não em A1
    # funcao symmetric_diference() retorna um array contendo todos os itens nao-repetidos dos dois arrays
    distancia = len(arestas_a1.symmetric_difference(arestas_a2))

    # dividimos por 2 porque cada aresta não compartilhada foi contada duas vezes (u,v e v,u)
    return distancia // 2