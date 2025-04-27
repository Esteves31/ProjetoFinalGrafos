
# Gerador de Grafos

Este projeto permite gerar, visualizar e manipular grafos a partir de arquivos CSV contendo vértices e arestas. Ele oferece funcionalidades para converter dados em Matrizes de Adjacência, Matrizes de Incidência e Listas de Adjacência, além de gerar representações gráficas dos grafos.

## Estrutura do Projeto

```plaintext
gerador-grafos/
│
├── resources/
│   ├── nodes.csv       # Arquivo com os vértices (nós) do grafo
│   └── edges.csv       # Arquivo com as arestas do grafo
│
├── src/
│   ├── main.py         # Arquivo principal contendo a lógica do programa
│   └── grafos.py       # Funções para manipulação e geração dos grafos
│
├── README.md           # Este arquivo
└── requirements.txt     # Dependências do projeto
```

## Como Rodar o Projeto

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu computador usando o comando abaixo:

```bash
git clone https://github.com/SEU_USUARIO/gerador-grafos.git
cd gerador-grafos
```

### 2. Instalar Dependências

Este projeto utiliza o Python e depende de algumas bibliotecas externas. Para instalar as dependências, siga os passos abaixo.

#### Usando o `pip` (instalar as dependências globalmente ou em um ambiente virtual):

Se você estiver utilizando um ambiente virtual, primeiro ative-o:

```bash
# Para Linux/macOS:
source venv/bin/activate

# Para Windows:
venv\Scripts\activate
```

Depois, instale as dependências com:

```bash
pip install -r requirements.txt
```

### 3. Arquivos de Entrada

O projeto espera dois arquivos CSV para funcionar corretamente:

- **nodes.csv**: Contém os vértices (nós) do grafo. A primeira linha deve ser o cabeçalho (`label,id`), e as linhas subsequentes devem conter o ID de cada nó.
  
- **edges.csv**: Contém as arestas do grafo. A primeira linha deve ser o cabeçalho (`source,target,type,weight,label`), e as linhas subsequentes devem conter as informações das arestas.

Estes arquivos podem ser encontrados na pasta `resources/`. Caso você precise de um exemplo para criar os seus próprios arquivos CSV, confira abaixo um modelo básico para cada um:

#### nodes.csv
```plaintext
label,id
NodeA,1
NodeB,2
NodeC,3
NodeD,4
```

#### edges.csv
```plaintext
source,target,type,weight,label
1,2,directed,1.0,EdgeAB
2,3,directed,1.0,EdgeBC
3,4,directed,1.0,EdgeCD
```

### 4. Executando o Projeto

Após ter as dependências instaladas e os arquivos de entrada prontos, você pode executar o programa utilizando o seguinte comando:

```bash
python src/main.py
```

O programa apresentará um menu interativo onde você poderá escolher entre:

1. Mostrar Matrizes (Adjacência e Incidência)
2. Mostrar Lista de Adjacência
3. Criar e Mostrar o Grafo (a partir das Matrizes ou Lista de Adjacência)
4. Sair

### 5. Visualização

Se você escolher a opção para gerar o grafo, o programa criará uma visualização e a salvará como imagem. As imagens geradas estarão no diretório atual e serão salvas com nomes como `graph_adj.png`, `graph_inc.png` ou `graph_lst.png`, dependendo da escolha.

## Dependências

O projeto utiliza as seguintes bibliotecas:

- `networkx` - Para manipulação e visualização de grafos.
- `matplotlib` - Para gerar gráficos e salvar as visualizações.

As dependências estão listadas no arquivo `requirements.txt`.

## Contribuindo

Se você deseja contribuir com o projeto, siga os passos abaixo:

1. Fork este repositório.
2. Crie uma nova branch para suas alterações (`git checkout -b feature/nome-da-feature`).
3. Faça suas alterações e commit com mensagens claras.
4. Envie um pull request para a branch `main`.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
