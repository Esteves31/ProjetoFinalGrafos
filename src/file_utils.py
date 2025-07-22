import csv
import os
import pickle
from graph_utils import print_keys


def ler_vertices(arquivo_vertices):
    """Lê o arquivo de vértices e retorna uma lista ordenada de IDs."""
    with open(f'resources\\{arquivo_vertices}.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()[1:]  # Pula o cabeçalho ("label,id")
        nodes = [linha.strip().split(';')[1] for linha in linhas if linha.strip()]  # Pega a coluna ID (índice 1)
    return sorted(nodes)

def ler_arestas(arquivo_arestas):
    """Lê o arquivo de edges e retorna pares (source, target)."""
    with open(f'resources\\{arquivo_arestas}.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()[1:]  # Pula o cabeçalho ("source,target,type,weight,label")
        edges = [linha.strip().split(';') for linha in linhas if linha.strip()]
        # Pega source, target e label
        edges = [(linha[0], linha[1], linha[4]) for linha in edges]
    return edges

def carregar_grafos(grafos, num_grafos):
    print("Caso não deseje cancelar, digite 'Voltar' a qualquer momento: ")
    
    arquivo_vertices = input("Nome do arquivo de vértices em '.\\resources' (Ex: nodes): ")
    if arquivo_vertices == "Voltar":
        return
    
    arquivo_arestas = input("Nome do arquivo de arestas em '.\\resources' (Ex: edges): ")
    if arquivo_arestas == "Voltar":
        return
    
    nome_grafo = input("Dê um nome ao grafo (Ex: Grafo_Teste): ")
    if nome_grafo == "Voltar":
        return
    
    if nome_grafo == '':
        nome_grafo = str(num_grafos)
        num_grafos += 1

    nodes = ler_vertices(arquivo_vertices)
    edges = ler_arestas(arquivo_arestas)

    grafos[nome_grafo] = {
        'Vertices': nodes,
        'Arestas': edges
    }

def carregar_grafos_salvos(arquivo_salvo):

    with open(f'.\\resources\\grafos_salvos\\{arquivo_salvo}.pkl', "rb") as gfs_pkl:
        grafos_salvos = pickle.load(gfs_pkl)

    print("Grafos carregados com sucesso!")
    print("Grafos carregados: ")
    print_keys(grafos_salvos['grafos'])
    return grafos_salvos['grafos'], grafos_salvos['num_grafos']

def mostrar_grafos_carregados(grafos:dict):
    for grafo in grafos.keys():
        print(f"{grafo}: ")
        print(f"\tVertices: {grafos[grafo]['Vertices']} ")
        print(f"\tArestas: {grafos[grafo]['Arestas']} ")

def salvar_grafos(grafos, num_grafos):
    grafos_salvos = {
        'grafos': grafos,
        'num_grafos': num_grafos
    }
    print("Digite 'Voltar' para cancelar a operação.")
    salvar_grafo = input("Digite o caminho que deseja salvar os grafos: ")

    if salvar_grafo == 'Voltar':
        return
    
    with open(f'resources/grafos_salvos/{salvar_grafo}.pkl', "wb") as gfs:
        pickle.dump(grafos_salvos, gfs)

    print("Grafos salvos!")

def salvar_grafo_em_csv(nome_grafo, vertices, arestas):
    pasta = os.path.join("resources", nome_grafo)
    os.makedirs(pasta, exist_ok=True)

    with open(os.path.join(pasta, "vertices.csv"), mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Label", "ID"])
        for i, v in enumerate(vertices, 1):
            writer.writerow([v, i])


    with open(os.path.join(pasta, "arestas.csv"), mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Source", "Target", "Type", "Weight", "Label"])
        for a in arestas:
            u, v, label = a
            writer.writerow([u, v, label, 1, label])

    print(f"Grafo '{nome_grafo}' salvo em 'resources/{nome_grafo}/'")

def excluir_um_grafo(grafos: dict):
    if not grafos:
        print("Nenhum grafo carregado.")
        return grafos

    print("Qual grafo deseja excluir:")
    print_keys(grafos)
    g_excluir = input("Nome do grafo: ")

    if g_excluir not in grafos:
        print(f"Grafo '{g_excluir}' não encontrado.")
        return grafos

    confirma = input(f"Tem certeza que deseja excluir o grafo '{g_excluir}'? (s/n): ").lower()
    if confirma == 's':
        grafos.pop(g_excluir)
        print(f"Grafo '{g_excluir}' excluído com sucesso.")
    else:
        print("Operação cancelada.")
    
    return grafos

def exportar_grafos(grafos: dict):
    print("Digite 'Voltar' para cancelar a operação.")
    qtdn = (input(f"Quantos grafos você vai querar exportar ({len(grafos)}): "))

    if(qtdn == "Voltar"):
        return
    
    if int(qtdn)== len(grafos):
        for grafo in grafos:
            salvar_grafo_em_csv(grafo, grafos[grafo]["Vertices"], grafos[grafo]["Arestas"] )
    else:
        print_keys(grafos)
        for i in range(qtdn):
            g = input(f"{i+1}: Digite o nome do grafo que deseja exportar: ")
            salvar_grafo_em_csv(g, grafos[g]["Vertices"], grafos[g]["Arestas"])