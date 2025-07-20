from file_utils import carregar_grafos, carregar_grafos_salvos, mostrar_grafos_carregados, salvar_grafos
from graph_utils import adjacentes_lst, build_adjacency_list, build_incidence_matrix, caminho_simples_bfs_lst, ciclo_em_v_bfs, construir_matriz_adjacencia, excentricidade_todos_vertices, existe_aresta_lst, graph_from_adjacency_list, grau_lst, graus_lst, n_arestas_lst, n_vertices_lst, plot_graph, print_keys, print_matriz, raio_arvore, é_subgrafo_bfs_lst


def menu():
    print("Bem-vindo ao Gerador de Grafos!")
    # arquivo_vertices = input("Caminho do arquivo de vértices (nodes.csv): ")
    # arquivo_arestas = input("Caminho do arquivo de arestas (edges.csv): ")
    # arquivo_vertices = '.\\nodes_teste.csv'
    # arquivo_arestas = '.\\edges_teste.csv'
    # nodes = ler_vertices(arquivo_vertices)
    # edges = ler_arestas(arquivo_arestas)
    # A = construir_matriz_adjacencia(nodes, edges)
    # M = build_incidence_matrix(nodes, edges)
    # L = build_adjacency_list(nodes, edges)
    grafos = dict()
    num_grafos = 0
    while True:
        print("\nOpções:")
        print("\t1) Carregar Grafos")
        print("\t2) Salvar Grafos")
        print("\t3) Vizualizar Grafos")
        print("\t4) Carregar Grafos")
        print("\t5) Carregar Grafos")
        print("\t6) Carregar Grafos")
        print("\t7) Sair")
        opc = input("Digite a opção desejada: ")

        if opc == '1':
            print("\nOpções para carregar:")
            print("\t1) Carregar com .csv")
            print("\t2) Carregar grafos salvos")
            print("\t3) Voltar")
            opc_carregar = input("Digite a opção desejada: ")
            if(opc_carregar == '1'):
                carregar_grafos(grafos, num_grafos)
            elif opc_carregar == '2':
               grafos, num_grafos = carregar_grafos_salvos()
        elif opc == '2':
            salvar_grafos(grafos, num_grafos)
        elif opc == '3':
            print("\nPossiveis vizualizações:")
            print("\t1) Ver grafos carregados")
            print("\t2) Ver matriz de Adjacência")
            print("\t3) Ver matriz de Incidência")
            print("\t4) Ver Lista de Adjacência")
            print("\t5) Plotar grafos")
            print("\t6) Voltar")
            opc_vizu = input("Digite a opção desejada: ")
            if opc_vizu == '1':
                mostrar_grafos_carregados(grafos)
            elif opc_vizu == '2':
                print("\nDigite o nome do grafo que deseja visualizar:")
                print_keys(grafos)
                opc_grafos = input()
                A = construir_matriz_adjacencia(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                print_matriz(A)
            elif opc_vizu == '3':
                print("\nDigite o nome do grafoz que deseja visualizar:")
                print_keys(grafos)
                opc_grafos = input()
                I = build_incidence_matrix(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                print_matriz(I)
            elif opc_vizu == '4':
                print("\nDigite o nome do grafo que deseja visualizar:")
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                print_matriz(L)
            elif opc_vizu == '5':
                print("\nDigite o nome do grafo que deseja visualizar:")
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                G = graph_from_adjacency_list(L)
                plot_graph(G)
        elif opc=='4':
            print("opções de funções:")
            print("\t1) Número de vértices de um grafo")
            print("\t2) Número de arestas de um grafo")
            print("\t3) Vértices adjacentes")
            print("\t4) Verificar aresta entre 2 vértices")
            print("\t5) Grau de um vértice")
            print("\t6) Grau de todos os vértices")
            print("\t7) Caminho entre dois vértices")
            print("\t8) Ciclo em um vértice")
            print("\t9) Verificar se G1 é subgrafo de G2")
            print("\t10) Verificar se G1 é subgrafo de G2")
            print("\t11) Verificar se G1 é subgrafo de G2")
            print("\t12) Verificar se G1 é subgrafo de G2")
            print("\t13) União entre grafos")
            print("\t14) Interseção")
            print("\t15) Dif. Simétrica")
            print("\t16) Remover Vertice")
            print("\t17) Remover Aresta")
            print("\t18) Fundir Vértices")
            print("\t19) Voltar")
            opc_func = input("Digite a opção desejada: ")
            if opc_func == "1":
                print('Em qual grafo você deseja realizar as operações:')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                print(f"Número de vértices do grafo {opc_grafos}: |V| = {n_vertices_lst(L)}")
            elif opc_func == "2":
                print('Em qual grafo você deseja realizar as operações:')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                print(f"Número de arestas do grafo {opc_grafos}: |V| = {n_arestas_lst(L)}")
            elif opc_func == "3":
                print('Em qual grafo você deseja realizar as operações:')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                v = input("Digite o vértice para encontrar os adjacentes: ")
                print(f"Vértices adjacentes a {v}: {adjacentes_lst(v, L)}")
            elif opc_func == "4":
                print('Em qual grafo você deseja realizar as operações:')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                u = input("Digite o vértice u: ")
                v = input("Digite o vértice v: ")
                print(f"Existe aresta entre {u} e {v}? {existe_aresta_lst(u, v, L)}")
            elif opc_func == "5":
                print('Em qual grafo você deseja realizar as operações:')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                v = input("Digite o vértice para obter o grau: ")
                print(f"Grau de {v}: {grau_lst(v, L)}")
            elif opc_func == "6":
                print('Em qual grafo você deseja realizar as operações:')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                graus = graus_lst(L)
                print("Graus dos vértices:")
                for v, g in graus.items():
                    print(f"{v}: {g}")
            elif opc_func == "7":
                print('Em qual grafo você deseja realizar as operações:')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                orig = input("Vértice de origem: ")
                dest = input("Vértice de destino: ")
                caminho = caminho_simples_bfs_lst(orig, dest, L)
                if caminho:
                    print(f"Caminho simples entre {orig} e {dest}: {caminho}")
                else:
                    print("Nenhum caminho encontrado.")
            elif opc_func == "8":
                print('Em qual grafo você deseja realizar as operações:')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                v = input("Vértice para busca de ciclo: ")
                ciclo = ciclo_em_v_bfs(v, L)
                if ciclo:
                    print(f"Ciclo encontrado: {ciclo}")
                else:
                    print("Nenhum ciclo encontrado.")
            elif opc_func == "9":
                print("Nome do grafo G1 (subgrafo):")
                print_keys(grafos)
                g1 = input()
                print("Nome do grafo G2 (supergrafo):")
                print_keys(grafos)
                g2 = input()
                L1 = build_adjacency_list(grafos[g1]['Vertices'], grafos[g1]['Arestas'])
                L2 = build_adjacency_list(grafos[g2]['Vertices'], grafos[g2]['Arestas'])
                print(f"G1 é subgrafo de G2? {é_subgrafo_bfs_lst(L1, L2)}")
            elif opc_func == "10":
                print("Opção não implementada: União entre grafos")
            elif opc_func == "11":
                print("Opção não implementada: Interseção entre grafos")
            elif opc_func == "12":
                print("Opção não implementada: Diferença simétrica entre grafos")
            elif opc_func == "13":
                print("Opção não implementada: Remover vértice")
            elif opc_func == "14":
                print("Opção não implementada: Remover aresta")
            elif opc_func == "15":
                print("Opção não implementada: Fundir vértices")
            elif opc_func == "16":
                print("Voltando ao menu principal.")
            elif opc_func == "20":
                print('Em qual grafo você deseja calcular a excentricidade?')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                excs = excentricidade_todos_vertices(L)
                print("Excentricidade de cada vértice:")
                for v, exc in excs.items():
                    print(f"{v}: {exc}")
            elif opc_func == "21":
                print('Em qual grafo você deseja calcular o raio?')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                raio = raio_arvore(L)
                print(f"Raio do grafo: {raio}")
        elif opc=='4':
            pass
        elif opc=='6': break
        else: print('Inválido')

if __name__=='__main__':
    menu()