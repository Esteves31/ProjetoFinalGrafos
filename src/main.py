from file_utils import carregar_grafos, carregar_grafos_salvos, excluir_um_grafo, exportar_grafos, mostrar_grafos_carregados, salvar_grafos
from graph_utils import adjacentes_lst, build_adjacency_list, build_incidence_matrix, calcula_distancia_arestas, caminho_simples_bfs_lst, ciclo_em_v_bfs, construir_matriz_adjacencia, diferenca_simetrica, excentricidade_todos_vertices, existe_aresta_lst, find_kspanning_trees, find_tree_centers, fundir_vertices, graph_from_adjacency_list, grau_lst, graus_lst, held_karp_hamiltonian_from_list, intersecao, is_eulerian_from_list, is_spanning_tree, is_subgraph, is_tree, is_tree_from_list, n_arestas_lst, n_vertices_lst, plot_graph, prim_mst, print_keys, print_matriz, raio_arvore, remover_aresta, remover_vertice, uniao, é_subgrafo_bfs_lst


def menu():
    print("Bem-vindo ao Gerador de Grafos!")
    grafos = dict()
    num_grafos = 0
    while True:
        print("\nOpções:")
        print("\t1) Carregar Grafos")
        print("\t2) Salvar Grafos")
        print("\t3) Vizualizar Grafos")
        print("\t4) Executar funções")
        print("\t5) Sair")
        opc = input("Digite a opção desejada: ")

        if opc == '1':
            print("\nOpções para carregar:")
            print("\t1) Carregar com .csv")
            print("\t2) Carregar grafos salvos")
            print("\t3) Excluir algum grafo")
            print("\t4) Voltar")
            opc_carregar = input("Digite a opção desejada: ")
            if(opc_carregar == '1'):
                carregar_grafos(grafos, num_grafos)
            elif opc_carregar == '2':
                print("Digite 'Voltar' para cancelar a operação.")
                arquivo_salvo = input("Digite o nome do arquivo: ")
                if arquivo_salvo == 'Voltar': 
                    continue
                grafos, num_grafos = carregar_grafos_salvos(arquivo_salvo)
            elif opc_carregar == '3':
                grafos = excluir_um_grafo(grafos)
        elif opc == '2':
            print("\nOpções para salvar:")
            print("\t1) Salvar em .pkl")
            print("\t2) Exportar para todos os grafos para .csv")
            print("\t3) Voltar")
            op = input("Digite a opção desejada: ")
            if op == '1':
                salvar_grafos(grafos, num_grafos)
            elif op == "2":
                exportar_grafos(grafos)
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
            print("Opções de funções:")
            print("\t1) Número de vértices de um grafo")
            print("\t2) Número de arestas de um grafo")
            print("\t3) Vértices adjacentes")
            print("\t4) Verificar aresta entre 2 vértices")
            print("\t5) Grau de um vértice")
            print("\t6) Grau de todos os vértices")
            print("\t7) Caminho entre dois vértices")
            print("\t8) Ciclo em um vértice")
            print("\t9) Verificar se G1 é subgrafo de G2")
            print("\t10) União entre grafos")
            print("\t11) Interseção")
            print("\t12) Dif. Simétrica")
            print("\t13) Remover Vertice")
            print("\t14) Remover Aresta")
            print("\t15) Fundir Vértices")
            print("\t16) Verificar se grafo é Euleriano")
            print("\t17) Verificar se grafo tem circuito Hamiltoniano")
            print("\t18) Verificar se A1 é uma árvore que seja um subgrafo de G")
            print("\t19) Verificar se A1 é uma árvore de abrangência.")
            print("\t20) Verificar se grafo G é uma árvore")
            print("\t21) Verificar centros de uma árvore")
            print("\t22) Verificar excentricidade")
            print("\t23) Verificar raio")
            print("\t24) Buscar árvores de abrangência")
            print("\t25) Distância entre duas árvores")
            print("\t26) Gerar a árvore geradora mínima com raiz em v")
            print("\t27) Voltar")
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
                print("Nome do grafo G1:")
                print_keys(grafos)
                g1 = input()
                print("Nome do grafo G2:")
                print_keys(grafos)
                g2 = input()
                v1, e1 = grafos[g1]['Vertices'], grafos[g1]['Arestas']
                v2, e2 = grafos[g2]['Vertices'], grafos[g2]['Arestas']
                v_uni, e_uni = uniao(v1, e1, v2, e2)
                print("De um nome para o grafo resultante: ")
                g_result = input()
                if g_result == '':
                    g_result = str(num_grafos)
                    num_grafos += 1
                grafos[g_result] = {
                    'Vertices': v_uni,
                    'Arestas': e_uni
                }   
            elif opc_func == "11":
                print("Nome do grafo G1:")
                print_keys(grafos)
                g1 = input()
                print("Nome do grafo G2:")
                print_keys(grafos)
                g2 = input()
                v1, e1 = grafos[g1]['Vertices'], grafos[g1]['Arestas']
                v2, e2 = grafos[g2]['Vertices'], grafos[g2]['Arestas']
                v_int, e_int = intersecao(v1, e1, v2, e2)
                print("De um nome para o grafo resultante: ")
                g_result = input()
                if g_result == '':
                    g_result = str(num_grafos)
                    num_grafos += 1
                grafos[g_result] = {
                    'Vertices': v_int,
                    'Arestas': e_int
                }            
            elif opc_func == "12":
                print("Nome do grafo G1:")
                print_keys(grafos)
                g1 = input()
                print("Nome do grafo G2:")
                print_keys(grafos)
                g2 = input()
                v1, e1 = grafos[g1]['Vertices'], grafos[g1]['Arestas']
                v2, e2 = grafos[g2]['Vertices'], grafos[g2]['Arestas']
                v_diff, e_diff = diferenca_simetrica(v1, e1, v2, e2)
                print("De um nome para o grafo resultante: ")
                g_result = input()
                if g_result == '':
                    g_result = str(num_grafos)
                    num_grafos += 1
                grafos[g_result] = {
                    'Vertices': v_diff,
                    'Arestas': e_diff
                }            
            elif opc_func == "13":
                print("Nome do grafo:")
                print_keys(grafos)
                g = input()
                v = input("Digite o vértice a ser removido: ")
                v1, e1 = grafos[g]['Vertices'], grafos[g]['Arestas']
                v_res, e_res = remover_vertice(v1, e1, v)
                grafos[g] = {
                    'Vertices': v_res,
                    'Arestas': e_res
                }
            elif opc_func == "14":
                print("Nome do grafo:")
                print_keys(grafos)
                g = input()
                u = input("Digite o vértice de origem da aresta: ")
                v = input("Digite o vértice de destino da aresta: ")
                lbl = input("Digite o rótulo da aresta (caso tenha, senão deixe em branco): ")
                e = (u, v, lbl)
                v1, e1 = grafos[g]['Vertices'], grafos[g]['Arestas']
                v_res, e_res = remover_aresta(v1, e1, e)
                g_result = input("Digite o nome do novo grafo: ")
                if g_result == '':
                    g_result = str(num_grafos)
                    num_grafos += 1
                grafos[g] = {
                    'Vertices': v_res,
                    'Arestas': e_res
                }
            elif opc_func == "15":
                print("Nome do grafo:")
                print_keys(grafos)
                g = input()
                vi = input("Digite o primeiro vértice a ser fundido: ")
                vj = input("Digite o segundo vértice a ser fundido: ")
                g_result = input("Digite o nome do novo grafo: ")
                v1, e1 = grafos[g]['Vertices'], grafos[g]['Arestas']
                v_res, e_res = fundir_vertices(v1, e1, vi, vj)
                if g_result == '':
                    g_result = str(num_grafos)
                    num_grafos += 1
                grafos[g_result] = {
                    'Vertices': v_res,
                    'Arestas': e_res
                }
            elif opc_func == "16": 
                print_keys(grafos)
                g = input("Nome do grafo: ")
                L = build_adjacency_list(grafos[g]['Vertices'], grafos[g]['Arestas'])
                print(f"O grafo '{g}' é euleriano? {'Sim' if is_eulerian_from_list(L) else 'Não'}")
            elif opc_func == '17':
                print_keys(grafos)
                g = input("Nome do grafo: ")
                L = build_adjacency_list(grafos[g]['Vertices'], grafos[g]['Arestas'])
                tem, ciclo = held_karp_hamiltonian_from_list(L)
                if tem:
                    print("Ciclo Hamiltoniano encontrado:")
                    for u, v in ciclo:
                        print(f"{u} -> {v}")
                else:
                    print("Não há ciclo Hamiltoniano.")

            elif opc_func == "18":
                print("Diga qual grafo G deseja verificar: ")
                print_keys(grafos)
                g = input()
                print("Digite qual árvore A que deseja utilizar: ")
                print_keys(grafos)
                a = input()
                result = is_tree_from_list(build_adjacency_list(grafos[a]['Vertices'], grafos[a]['Arestas'])) and \
                is_subgraph(grafos[g]['Vertices'], grafos[g]['Arestas'], grafos[a]['Vertices'], grafos[a]['Arestas'])
                print(f"A é uma árvore subgrafo de G? {'Sim' if result else 'Não'}")
            elif opc_func == "19":
                print("Diga qual grafo G deseja verificar: ")
                print_keys(grafos)
                g = input()
                print("Digite qual árvore A que deseja utilizar: ")
                print_keys(grafos)
                a = input()
                result = is_spanning_tree(grafos[g]['Vertices'], grafos[g]['Arestas'], grafos[a]['Vertices'], grafos[a]['Arestas'])
                print(f"A1 é uma árvore de abrangência de G? {'Sim' if result else 'Não'}")
            elif opc_func == "20":
                print("Diga qual grafo G deseja verificar: ")
                print_keys(grafos)
                g = input()
                result = is_tree(grafos[g]['Vertices'], grafos[g]['Arestas'])
                print(f"G é uma árvore? {'Sim' if result else 'Não'}")
            
            elif opc_func == "21":
                print("Qual árvore você deseja verificar os centros? ")
                print_keys(grafos)
                a = input()
                if is_tree(grafos[a]["Vertices"], grafos[a]["Arestas"]):
                    result = find_tree_centers(grafos[a]["Vertices"], grafos[a]['Arestas'])
                    print(f"Os centros são: {result}")
                else:
                    print("O grafo inserido não é uma árvore")

            elif opc_func == "22":
                print('Em qual grafo você deseja calcular a excentricidade?')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                excs = excentricidade_todos_vertices(L)
                print("Excentricidade de cada vértice:")
                for v, exc in excs.items():
                    print(f"\t{v}: {exc}")

            elif opc_func == "23":
                print('Em qual grafo você deseja calcular o raio?')
                print_keys(grafos)
                opc_grafos = input()
                L = build_adjacency_list(grafos[opc_grafos]['Vertices'], grafos[opc_grafos]['Arestas'])
                raio = raio_arvore(L)
                print(f"Raio do grafo: {raio}")

            elif opc_func == '24':
                print('Em qual grafo G deseja fazer a busca? ')
                print_keys(grafos)
                g = input()
                print("Qual árvore A deseja utilizar para fazer a busca?")
                print_keys(grafos)
                a = input()
                if is_tree(grafos[a]['Vertices'], grafos[a]["Arestas"]):
                    k = int(input("Quantas árvores de abrangência deseja gerar? "))
                    result = find_kspanning_trees(grafos[g]['Vertices'], grafos[g]['Arestas'], grafos[a]['Arestas'], k)
                    print(f"As árvores de abrangência encontradas foram: \n\t{result}")
                else:
                    print("A não é uma árvore")
            elif opc_func == "25":
                print('Qual a árvore A1?')
                print_keys(grafos)
                a1 = input()
                print('Qual a árvore A2?')
                print_keys(grafos)
                a2 = input()
                if is_tree(grafos[a1]['Vertices'],grafos[a1]['Arestas']) and is_tree(grafos[a2]['Vertices'],grafos[a2]['Arestas']):
                    L1 = build_adjacency_list(grafos[a1]['Vertices'],grafos[a1]['Arestas'])
                    L2 = build_adjacency_list(grafos[a2]['Vertices'],grafos[a2]['Arestas'])
                    result = calcula_distancia_arestas(L1, L2)
                    print(f"Distancia entre A1 e A2 é: {result}")
                else:   
                    print("A1 ou A2 não é uma árvore.") 
            elif opc_func == "26":
                print('Qual a árvore A?')
                print_keys(grafos)
                a1 = input()
                v = input("Qual raiz desejada?")
                nome_grafo = input("De um nome para o grafo resultante: ")
                mst = prim_mst(grafos[a1]["Vertices"], grafos[a1]["Arestas"], v)
                if nome_grafo == '':
                    nome_grafo = str(num_grafos)
                    num_grafos += 1
                grafos[nome_grafo] = {
                    'Vertices': mst["Vertices"],
                    'Arestas': mst["Arestas"]
                }

        elif opc=='5': break
        else: print('Inválido')

if __name__=='__main__':
    menu()