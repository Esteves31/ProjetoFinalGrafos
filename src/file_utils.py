import csv
import os
import pickle
from graph_utils import print_keys
import csv

def ler_vertices(arquivo_vertices):
    """
    Lê o arquivo de vértices e retorna uma lista ordenada de tuplas (label, id).
    Aceita qualquer ordem de colunas, desde que haja 'label' e 'id' (qualquer capitalização).
    """
    with open(f'resources\\{arquivo_vertices}.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        cabecalho = next(reader)
        # Normaliza para minúsculas
        cabecalho_lower = [col.lower() for col in cabecalho]
        print(cabecalho_lower)
        try:
            idx_label = cabecalho_lower.index('label')
            idx_id = cabecalho_lower.index('id')
        except ValueError:
            raise ValueError("Colunas 'label' e/ou 'id' não encontradas no arquivo.")
        # Armazena tuplas (label, id)
        vertices = [
            (linha[idx_label], linha[idx_id])
            for linha in reader
            if linha and len(linha) > max(idx_label, idx_id)
        ]
        # Ordena por id (ou por label, se preferir)
        return sorted(vertices, key=lambda x: x[1])

def ler_arestas(arquivo_arestas, vertices):
    """
    Lê o arquivo de edges e retorna tuplas:
    ((source_label, source_id), (target_label, target_id), label, weight),
    independentemente da ordem das colunas.
    """
    # Cria um dicionário para mapear id -> label
    id_to_label = {id_: label for label, id_ in vertices}

    with open(f'resources\\{arquivo_arestas}.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        cabecalho = next(reader)
        # Descobre a posição de cada campo (case-insensitive)
        cabecalho_lower = [col.lower() for col in cabecalho]
        idx_source = cabecalho_lower.index('source')
        idx_target = cabecalho_lower.index('target')
        try:
            idx_label = cabecalho_lower.index('label')
        except ValueError:
            idx_label = None
        try:
            idx_weight = cabecalho_lower.index('weight')
        except ValueError:
            idx_weight = None

        edges = []
        for linha in reader:
            if not linha or len(linha) < 2:
                continue
            # Pega os ids
            source_id = linha[idx_source]
            target_id = linha[idx_target]
            # Busca os labels
            source_label = id_to_label.get(source_id, '')
            target_label = id_to_label.get(target_id, '')
            # Label da aresta
            label = linha[idx_label] if idx_label is not None and len(linha) > idx_label else ''
            # Peso
            if idx_weight is not None and len(linha) > idx_weight:
                try:
                    weight = float(linha[idx_weight])
                except (ValueError, IndexError):
                    weight = 0.0
            else:
                weight = 0.0
            edges.append((
                (source_label, source_id),
                (target_label, target_id),
                label,
                weight
            ))
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
    edges = ler_arestas(arquivo_arestas, nodes)

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
    """
    Salva o grafo em dois arquivos CSV: vertices.csv e arestas.csv,
    com cabeçalhos padronizados e todos os campos relevantes.
    """
    import os, csv
    pasta = os.path.join("resources", nome_grafo)
    os.makedirs(pasta, exist_ok=True)
    # Salva vértices
    with open(os.path.join(pasta, "vertices.csv"), mode="w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Label", "ID"])
        for v in vertices:
            # Se for dicionário
            if isinstance(v, dict):
                writer.writerow([v['label'], v['id']])
            # Se for tupla/lista
            elif isinstance(v, (tuple, list)) and len(v) == 2:
                writer.writerow([v[0], v[1]])
            else:
                raise ValueError("Formato de vértice não reconhecido: {}".format(v))
    # Salva arestas (igual ao seu)
    with open(os.path.join(pasta, "arestas.csv"), mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Source", "Target", "Type", "Weight", "Label"])
        for a in arestas:
            if len(a) == 4:
                u, v, label, weight = a
            elif len(a) == 3:
                u, v, label = a
                weight = 1
            else:
                continue
            writer.writerow([u[1], v[1], "Undirected", weight, label])
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
    
    if int(qtdn) == len(grafos):
        for grafo in grafos:
            salvar_grafo_em_csv(grafo, grafos[grafo]["Vertices"], grafos[grafo]["Arestas"] )
    else:
        print_keys(grafos)
        for i in range(int(qtdn)):
            g = input(f"{i+1}: Digite o nome do grafo que deseja exportar: ")
            salvar_grafo_em_csv(g, grafos[g]["Vertices"], grafos[g]["Arestas"])