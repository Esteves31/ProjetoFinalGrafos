import os
from graph_utils import *
from file_utils import *

def menu():
    print("Bem-vindo ao Gerador de Grafos!")

    # Passo 1: Obter os caminhos dos arquivos
    arquivo_vertices = input("Digite o caminho para o arquivo de vértices (nodes.csv): ")
    arquivo_arestas = input("Digite o caminho para o arquivo de arestas (edges.csv): ")

    if not os.path.exists(arquivo_vertices) or not os.path.exists(arquivo_arestas):
        print("Erro: Um ou mais arquivos não encontrados.")
        return

    # Lê os arquivos
    nodes = ler_vertices(arquivo_vertices)
    edges = ler_arestas(arquivo_arestas)

    # Passo 2: Mostrar opções
    while True:
        print("\nEscolha uma das opções:")
        print("1. Mostrar Matrizes (Adjacência e Incidência)")
        print("2. Mostrar Lista de Adjacência")
        print("3. Criar e Mostrar Grafo (a partir das Matrizes ou Lista de Adjacência)")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            # Mostrar Matrizes
            adjacence_matrix = construir_matriz_adjacencia(nodes, edges)
            incidence_matrix = build_incidence_matrix(nodes, edges)
            print("\nMatriz de Adjacência:")
            for linha in adjacence_matrix:
                print(linha)
            print("\nMatriz de Incidência:")
            for linha in incidence_matrix:
                print(linha)

        elif escolha == '2':
            # Mostrar Lista de Adjacência
            adjacency_list = build_adjacency_list(nodes, edges)
            print("\nLista de Adjacência:")
            for node, neighbors in adjacency_list.items():
                print(f"{node} -> {neighbors}")

        elif escolha == '3':
            # Criar o Grafo
            print("\nEscolha a origem do grafo:")
            print("1. A partir da Matriz de Adjacência")
            print("2. A partir da Matriz de Incidência")
            print("3. A partir da Lista de Adjacência")
            escolha_grafo = input("Digite o número da opção desejada: ")

            if escolha_grafo == '1':
                adjacency_matrix = construir_matriz_adjacencia(nodes, edges)
                G = graph_from_adjacency_matrix(nodes, adjacency_matrix, edges)
                plot_graph(G, title="Grafo da matriz de adjacencia", save_as="graph_adj.png")

            elif escolha_grafo == '2':
                incidence_matrix = build_incidence_matrix(nodes, edges)
                G = graph_from_incidence_matrix(nodes, incidence_matrix, edges)
                plot_graph(G, title="Grafo da matriz de incidencia", save_as="graph_inc.png")

            elif escolha_grafo == '3':
                adjacency_list = build_adjacency_list(nodes, edges)
                G = graph_from_adjacency_list(adjacency_list)
                plot_graph(G, title="Grafo da lista de adjacencia", save_as="graph_lst.png")
            else:
                print("Opção inválida!")

        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
