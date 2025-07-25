import heapq
from itertools import combinations
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def get_vertex_id(v):
    """Extrai o id do vértice, seja tupla, dict ou valor simples."""
    if isinstance(v, dict):
        return v['id']
    elif isinstance(v, (tuple, list)) and len(v) == 2:
        return v[1]
    else:
        return v

def get_vertex_label(v):
    """Extrai o label do vértice, seja tupla, dict ou valor simples."""
    if isinstance(v, dict):
        return v['label']
    elif isinstance(v, (tuple, list)) and len(v) == 2:
        return v[0]
    else:
        return v

# Utilitário para extrair vértices de uma aresta
def get_vertices(edge):
    """Retorna os vértices de uma aresta (assume formato (u, v, ...))."""
    return edge[0], edge[1]

def get_label(edge):
    """Retorna o label da aresta, se existir."""
    if len(edge) > 2:
        return edge[2]
    return None

def get_weight(edge):
    """Retorna o peso da aresta, se existir."""
    if len(edge) > 3:
        return edge[3]
    return None

def print_matriz(matriz):
    for row in matriz:
        print(" ".join(f"{val:>4}" for val in row))

def print_adjacency_list(adj):
    max_label_len = max(len(str(node)) for node in adj)
    for node, neighbors in adj.items():
        label = str(node).ljust(max_label_len)
        if neighbors:
            neigh_str = ", ".join(f"{dest}(lbl={lbl})" for dest, lbl in neighbors)
        else:
            neigh_str = "<nenhum>"
        print(f"{label} -> {neigh_str}")

def print_adjacency_list_peso(adj):
    # Calcula o maior comprimento de label do nó para alinhamento
    max_label_len = max(len(str(node)) for node in adj)
    for node, neighbors in adj.items():
        label = str(node).ljust(max_label_len)
        if neighbors:
            # Espera-se que cada vizinho seja (dest, peso, lbl)
            neigh_str = ", ".join(
                f"{dest}(w={peso}, lbl={lbl})" for dest, peso, lbl in neighbors
            )
        else:
            neigh_str = "<nenhum>"
        print(f"{label} -> {neigh_str}")

def construir_matriz_adjacencia(nodes, edges):
    n = len(nodes)
    matriz = [[0] * n for _ in range(n)]
    indice = {v: i for i, v in enumerate(nodes)}
    for edge in edges:
        origem, destino = get_vertices(edge)
        if origem in indice and destino in indice:
            i = indice[origem]
            j = indice[destino]
            matriz[i][j] = 1
            matriz[j][i] = 1  # Não direcionado
    return matriz

def build_incidence_matrix(nodes, edges):
    n = len(nodes)
    m = len(edges)
    incidence_matrix = [[0] * m for _ in range(n)]
    node_index = {node: idx for idx, node in enumerate(nodes)}
    for edge_idx, edge in enumerate(edges):
        source, target = get_vertices(edge)
        if source in node_index:
            incidence_matrix[node_index[source]][edge_idx] = 1
        if target in node_index:
            incidence_matrix[node_index[target]][edge_idx] = 1
    return incidence_matrix

def build_adjacency_list(nodes, edges):
    ids = [get_vertex_id(v) for v in nodes]
    adjacency_list = {vid: [] for vid in ids}
    for edge in edges:
        u, v = get_vertices(edge)
        uid = get_vertex_id(u)
        vid = get_vertex_id(v)
        label = get_label(edge)
        adjacency_list[uid].append((vid, label))
        adjacency_list[vid].append((uid, label))  # Não direcionado
    return adjacency_list

def build_adjacency_matrix(nodes, edges):
    ids = [get_vertex_id(v) for v in nodes]
    n = len(ids)
    idx = {vid: i for i, vid in enumerate(ids)}
    matriz = [[0] * n for _ in range(n)]
    for edge in edges:
        u, v = get_vertices(edge)
        uid = get_vertex_id(u)
        vid = get_vertex_id(v)
        i, j = idx[uid], idx[vid]
        matriz[i][j] = 1
        matriz[j][i] = 1  # Não direcionado
    return matriz

def construir_lista_adjacencia_peso(vertices, arestas):
    """ Constrói uma lista de adjacência ponderada a partir das arestas.
        Retorna: {v: [(vizinho, peso, label), ...]}
    """
    from collections import defaultdict
    adj = defaultdict(list)
    for u, v, label, weight in arestas:
        adj[u].append((v, weight, label))
        adj[v].append((u, weight, label))  # Se o grafo for não-direcionado
    return adj

def graph_from_adjacency_matrix(nodes, adjacency_matrix, edges):
    G = nx.Graph()
    for i, node in enumerate(nodes):
        G.add_node(node)
    edge_labels_dict = {(get_vertices(e)): get_label(e) for e in edges}
    edge_labels_dict.update({(b, a): lbl for (a, b), lbl in edge_labels_dict.items()})
    n = len(nodes)
    for i in range(n):
        for j in range(i, n):
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
    for j in range(m):
        connected_nodes = []
        for i in range(n):
            if incidence_matrix[i][j] == 1:
                connected_nodes.append(nodes[i])
        if len(connected_nodes) == 2:
            source, target = connected_nodes
            label = get_label(edges[j])
            G.add_edge(source, target, label=label)
    return G

def graph_from_adjacency_list(adjacency_list):
    G = nx.Graph()
    for node, neighbors in adjacency_list.items():
        G.add_node(node)
        for neighbor, label in neighbors:
            if not G.has_edge(node, neighbor):
                G.add_edge(node, neighbor, label=label)
    return G

def plot_graph(G, title="Grafo", node_color='skyblue', edge_color='gray', edge_label_color='red', layout_k=0.9, save_as=None):
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

# Funções de contagem
def n_vertices_adj(A): return len(A)
def n_vertices_inc(I): return len(I)
def n_vertices_lst(L): return len(L)
def n_arestas_adj(A): n = len(A); total = sum(A[i][j] for i in range(n) for j in range(n)); return total // 2
def n_arestas_inc(I): return len(I[0])
def n_arestas_lst(L): total = sum(len(v) for v in L.values()); return total // 2

# Funções de vizinhança
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

# Funções de existência de aresta
def existe_aresta_adj(u, v, nodes, A):
    i, j = nodes.index(u), nodes.index(v)
    return bool(A[i][j])

def existe_aresta_inc(u, v, nodes, I):
    iu, iv = nodes.index(u), nodes.index(v)
    for col in zip(*I):
        if col[iu] and col[iv]:
            return True
    return False

def existe_aresta_lst(u, v, L):
    return any(nei == v for nei, _ in L.get(u, []))

# Grau
def grau_adj(v, nodes, A): return sum(A[nodes.index(v)])
def grau_inc(v, nodes, I): return sum(I[nodes.index(v)])
def grau_lst(v, L): return len(L.get(v, []))

def graus_adj(nodes, A): return {v: grau_adj(v, nodes, A) for v in nodes}
def graus_inc(nodes, I): return {v: grau_inc(v, nodes, I) for v in nodes}
def graus_lst(L): return {v: len(neis) for v, neis in L.items()}

# Caminho simples BFS
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

def caminho_menor_peso_dijkstra(orig, dest, L):
    """
    L: { (label, id): [ ((label_viz, id_viz), peso, label_aresta), ... ] }
    orig, dest: id (string ou número)
    Retorna: (caminho, labels_arestas, peso_total) ou None
    """
    # Encontrar o vértice de origem e destino pelas IDs
    def find_vertex_by_id(id_):
        for v in L:
            if v[1] == id_:
                return v
        return None

    v_orig = find_vertex_by_id(orig)
    v_dest = find_vertex_by_id(dest)
    if v_orig is None or v_dest is None:
        return None

    heap = [(0, v_orig, [v_orig], [])]  # (peso acumulado, vértice atual, caminho, labels_arestas)
    visited = set()

    while heap:
        peso, v, path, labels = heapq.heappop(heap)
        if v[1] == dest:
            return path, labels, peso
        if v in visited:
            continue
        visited.add(v)
        for nxt, peso_aresta, label_aresta in L.get(v, []):
            if nxt not in visited:
                heapq.heappush(heap, (
                    peso + float(peso_aresta),
                    nxt,
                    path + [nxt],
                    labels + [label_aresta]
                ))
    return None

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

# Ciclo em v
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

def ciclo_em_v_adj(v0, nodes, A):
    return ciclo_em_v_bfs(v0, matriz_para_lista(nodes, A))

def ciclo_em_v_inc(v0, nodes, M):
    return ciclo_em_v_bfs(v0, incidencia_para_lista(nodes, M))

# Subgrafo
def é_subgrafo_bfs_lst(Lsub, Lsup):
    visited = set()
    for start in Lsub:
        if start not in visited:
            queue = deque([start])
            visited.add(start)
            while queue:
                u = queue.popleft()
                sub_vizinhos = [v for v, _ in Lsub[u]]
                for v in sub_vizinhos:
                    sup_vizinhos = [x for x, _ in Lsup.get(u, [])]
                    if v not in sup_vizinhos:
                        return False
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
    return True

def subgrafo_matriz(nodes1, A1, nodes2, A2):
    return é_subgrafo_bfs_lst(matriz_para_lista(nodes1, A1), matriz_para_lista(nodes2, A2))

def subgrafo_incidencia(nodes1, M1, nodes2, M2):
    return é_subgrafo_bfs_lst(incidencia_para_lista(nodes1, M1), incidencia_para_lista(nodes2, M2))

# Excentricidade e raio
def excentricidade_todos_vertices(L):
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
    excentricidades = excentricidade_todos_vertices(L)
    return min(excentricidades.values())

def print_keys(grafos):
    keys = list(grafos.keys())
    if keys:
        for k in keys:
            print(f"-> {k}")

# Operações de conjunto
def uniao(vertices1, arestas1, vertices2, arestas2):
    vertices = list(set(vertices1).union(vertices2))
    def norm(e): return (min(e[0], e[1]), max(e[0], e[1]))
    set1 = {norm(e) for e in arestas1}
    set2 = {norm(e) for e in arestas2}
    arestas = list(set1.union(set2))
    return vertices, [(u, v, '') for u, v in arestas]

def intersecao(vertices1, arestas1, vertices2, arestas2):
    vertices = list(set(vertices1).intersection(vertices2))
    def norm(e): return (min(e[0], e[1]), max(e[0], e[1]))
    set1 = {norm(e) for e in arestas1}
    set2 = {norm(e) for e in arestas2}
    arestas = list(set1.intersection(set2))
    return vertices, [(u, v, '') for u, v in arestas]

def diferenca_simetrica(vertices1, arestas1, vertices2, arestas2):
    vertices = list(set(vertices1).union(vertices2))
    def norm(e): return (min(e[0], e[1]), max(e[0], e[1]))
    set1 = {norm(e) for e in arestas1}
    set2 = {norm(e) for e in arestas2}
    arestas = list(set1.symmetric_difference(set2))
    return vertices, [(u, v, '') for u, v in arestas]

# Remover vértice/aresta
def remover_vertice(vertices, arestas, vi):
    if vi not in vertices:
        print(f"Vértice {vi} não existe.")
        return vertices[:], arestas[:]
    new_vertices = [v for v in vertices if v != vi]
    new_arestas = [e for e in arestas if vi not in (e[0], e[1])]
    return new_vertices, new_arestas

def remover_aresta(vertices, arestas, ei):
    def norm(e): return (min(e[0], e[1]), max(e[0], e[1]))
    ei_norm = norm(ei)
    new_arestas = [e for e in arestas if norm(e) != ei_norm]
    return vertices[:], new_arestas

# Fundir vértices
def fundir_vertices(vertices, arestas, vi, vj):
    if vi not in vertices or vj not in vertices:
        print(f"Vértices {vi} e/ou {vj} não existem.")
        return vertices[:], arestas[:]
    novo = f"{vi}_{vj}"
    new_vertices = [v for v in vertices if v != vi and v != vj]
    new_vertices.append(novo)
    new_arestas = set()
    for e in arestas:
        a, b = e[0], e[1]
        label = get_label(e)
        a_new = novo if a == vi or a == vj else a
        b_new = novo if b == vi or b == vj else b
        if a_new != b_new:
            new_arestas.add((a_new, b_new, label))
    return new_vertices, list(new_arestas)

# Conectividade e propriedades
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

def is_eulerian_from_list(adj_list):
    if not is_connected(adj_list):
        return False
    return all(grau_lst(v, adj_list) % 2 == 0 for v in adj_list)

def is_tree_from_list(adj_list):
    n_vertices = len(adj_list)
    n_arestas = sum(len(neis) for neis in adj_list.values()) // 2
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
    n = len(nodes)
    if n <= 2:
        return nodes
    adj = build_adjacency_list(nodes, edges)
    degrees = {node: len(adj[node]) for node in nodes}
    leaves = deque()
    for node in nodes:
        if degrees[node] == 1:
            leaves.append(node)
    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_in_this_layer = len(leaves)
        remaining_nodes -= leaves_in_this_layer
        for _ in range(leaves_in_this_layer):
            leaf = leaves.popleft()
            for neighbor, _ in adj[leaf]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    leaves.append(neighbor)
    centers = list(leaves)
    return centers

def find_cycle(adj, start, parent, visited, path):
    visited.add(start)
    path.append(start)
    for neighbor, _ in adj[start]:
        if neighbor not in visited:
            result = find_cycle(adj, neighbor, start, visited, path)
            if result:
                return result
        elif neighbor != parent and neighbor in path:
            idx = path.index(neighbor)
            return path[idx:] + [neighbor]
    path.pop()
    return None

def held_karp_hamiltonian_from_list(adj_list):
    """
    Resolve o problema do ciclo Hamiltoniano usando Held-Karp (bitmask DP).
    adj_list: {nó: [(vizinho, label), ...]}
    Retorna: (True, lista_de_arestas) se existe ciclo Hamiltoniano, senão (False, [])
    """
    nodes = list(adj_list.keys())
    n = len(nodes)
    node_idx = {node: i for i, node in enumerate(nodes)}
    idx_node = {i: node for i, node in enumerate(nodes)}
    dp = {}

    # Inicialização: caminhos de 2 vértices começando do nó 0
    for k in range(1, n):
        if nodes[k] in [v for v, _ in adj_list[nodes[0]]]:
            dp[(1 << 0) | (1 << k), k] = [0, k]

    # Subconjuntos de tamanho 3 até n
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

    # Reconstrução do ciclo
    full_bits = (1 << n) - 1
    for k in range(1, n):
        if (full_bits, k) in dp and nodes[0] in [v for v, _ in adj_list[nodes[k]]]:
            path = dp[(full_bits, k)] + [0]
            path_nodes = [nodes[i] for i in path]
            edges = [(path_nodes[i], path_nodes[i+1]) for i in range(len(path_nodes)-1)]
            return True, edges
    return False, []


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

def find_kspanning_trees(vertices, arestas, arestas_abrangencia, k):
    """
    vertices: lista de vértices do grafo G
    arestas: lista de arestas do grafo G (tuplas, pode ter label/peso)
    arestas_abrangencia: lista de arestas de uma árvore de abrangência inicial
    k: número de árvores de abrangência diferentes a encontrar
    """
    def norm(e):  # Normaliza para comparar arestas sem direção
        return tuple(sorted(get_vertices(e)))
    if not is_spanning_tree(vertices, arestas, vertices, arestas_abrangencia):
        print("A floresta de abrangência inicial não é válida.")
        return []
    spanning_trees = []
    initial_tree_edges = set(map(norm, arestas_abrangencia))
    graph_edges = set(map(norm, arestas))
    edges_to_add = list(graph_edges - initial_tree_edges)
    if not edges_to_add:
        print("Não há arestas para adicionar para formar novas árvores de abrangência.")
        return []
    temp_graph_adj = build_adjacency_list(vertices, arestas_abrangencia)
    for new_edge in edges_to_add:
        if len(spanning_trees) >= k:
            break
        u, v = new_edge
        # Cria cópia da lista de adjacência e adiciona a nova aresta
        temp_adj_copy = {node: neighbors[:] for node, neighbors in temp_graph_adj.items()}
        temp_adj_copy[u].append((v, ''))
        temp_adj_copy[v].append((u, ''))
        # Busca ciclo
        visited = set()
        path = []
        cycle = find_cycle(temp_adj_copy, u, None, visited, path)
        if cycle:
            # Gera conjunto de arestas do ciclo
            cycle_edges = set()
            for i in range(len(cycle) - 1):
                edge = tuple(sorted((cycle[i], cycle[i+1])))
                cycle_edges.add(edge)
            # Remove a nova aresta do ciclo
            cycle_edges.discard(new_edge)
            # Para cada aresta do ciclo que está na árvore, tente trocar
            for edge_to_remove in cycle_edges:
                if len(spanning_trees) >= k:
                    break
                new_tree_edges = list((initial_tree_edges - {edge_to_remove}) | {new_edge})
                # Reconstrua as arestas originais (com label/peso) para checar se é árvore de abrangência
                def find_original(e):
                    for a in arestas:
                        if norm(a) == e:
                            return a
                    for a in arestas_abrangencia:
                        if norm(a) == e:
                            return a
                    return (e[0], e[1], '')
                new_tree_full = [find_original(e) for e in new_tree_edges]
                if is_spanning_tree(vertices, arestas, vertices, new_tree_full) and set(new_tree_edges) not in [set(map(norm, t)) for t in spanning_trees]:
                    spanning_trees.append(new_tree_full)
    return spanning_trees

# Distância de arestas entre duas listas de adjacência
def calcula_distancia_arestas(A1, A2):
    arestas_a1 = set()
    for u in A1:
        for v, _ in A1[u]:
            arestas_a1.add(frozenset({u, v}))
    arestas_a2 = set()
    for u in A2:
        for v, _ in A2[u]:
            arestas_a2.add(frozenset({u, v}))
    distancia = len(arestas_a1.symmetric_difference(arestas_a2))
    return distancia // 2

def prim_mst_from_list(L, raiz_id):
    """
    L: { (label, id): [ ((label_viz, id_viz), peso, label_aresta), ... ] }
    raiz_id: id do vértice inicial (não a tupla, só o id)
    Retorna: dict com chaves "Vertices" e "Arestas" no mesmo formato das chaves de L.
    """
    # Mapeia id para objeto vértice original (tupla)
    id_to_vertex = {v[1]: v for v in L}
    raiz = id_to_vertex.get(raiz_id)
    if raiz is None:
        raise ValueError(f"Raiz com id {raiz_id} não encontrada nos vértices.")

    visitados = set([raiz_id])
    heap = []
    mst_arestas = []
    mst_vertices = set([raiz_id])

    # Adiciona as arestas iniciais da raiz
    for viz, peso, label in L[raiz]:
        heapq.heappush(heap, (peso, raiz, viz, label))

    while heap and len(visitados) < len(L):
        peso, u, v, label = heapq.heappop(heap)
        v_id = v[1]
        if v_id in visitados:
            continue
        visitados.add(v_id)
        mst_vertices.add(v_id)
        mst_arestas.append((u, v, label, peso))
        for viz, p, l in L[v]:
            if viz[1] not in visitados:
                heapq.heappush(heap, (p, v, viz, l))

    # Retorna os vértices e arestas no mesmo formato das chaves de L
    return {
        "Vertices": sorted([id_to_vertex[vid] for vid in mst_vertices], key=lambda x: x[1]),
        "Arestas": mst_arestas
    }