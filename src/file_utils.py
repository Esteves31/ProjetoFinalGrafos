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
