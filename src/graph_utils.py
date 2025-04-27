import networkx as nx
import matplotlib.pyplot as plt

def construir_matriz_adjacencia(nodes, edges):
    """Constrói a matriz de adjacência."""
    n = len(nodes)
    matriz = [[0] * n for _ in range(n)]  # Inicializa com zeros
    indice = {vertice: i for i, vertice in enumerate(nodes)}  # Mapeia IDs para índices
    
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
    adjacency_list = {node: [] for node in nodes}
    for source, target, label in edges:
        adjacency_list[source].append((target, label))
        adjacency_list[target].append((source, label))  # Comente esta linha se quiser grafo dirigido
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
