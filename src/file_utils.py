import pickle
from graph_utils import print_keys


def ler_vertices(arquivo_vertices):
    """Lê o arquivo de vértices e retorna uma lista ordenada de IDs."""
    with open(arquivo_vertices, 'r') as f:
        linhas = f.readlines()[1:]  # Pula o cabeçalho ("label,id")
        nodes = [linha.strip().split(';')[1] for linha in linhas if linha.strip()]  # Pega a coluna ID (índice 1)
    return sorted(nodes)

def ler_arestas(arquivo_arestas):
    """Lê o arquivo de edges e retorna pares (source, target)."""
    with open(arquivo_arestas, 'r') as f:
        linhas = f.readlines()[1:]  # Pula o cabeçalho ("source,target,type,weight,label")
        edges = [linha.strip().split(';') for linha in linhas if linha.strip()]
        # Pega source, target e label
        edges = [(linha[0], linha[1], linha[4]) for linha in edges]
    return edges

def carregar_grafos(grafos, num_grafos):
    print("Caso não deseje cancelar, digite 'Voltar' a qualquer momento: ")
    
    arquivo_vertices = input("Caminho do arquivo de vértices (Ex: .\\nodes.csv): ")
    if arquivo_vertices == "Voltar":
        return
    
    arquivo_arestas = input("Caminho do arquivo de arestas (Ex: .\\edges.csv): ")
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

def carregar_grafos_salvos():
    arquivo_salvo = input("Digite o caminho do arquivo: ")

    with open(arquivo_salvo, "rb") as gfs_pkl:
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
    salvar_grafo = input("Digite o caminho que deseja salvar os grafos: ")
    with open(salvar_grafo, "wb") as gfs:
        pickle.dump(grafos_salvos, gfs)

    print("Grafos salvos!")
