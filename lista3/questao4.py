# O problema de saber se uma string pode ser convertida em outra pode ser
# dividido em subproblemas: um caractere pode ser convertido em outro?
# Fazer essa pergunta para todas as duplas de caracteres

# Se representarmos os caracteres como um grafo g, onde uv existe se u pode ser
# diretamente convertido em v, o subproblema pode ser interpretado como:
# Existe um caminho em g que liga u e v?

class Grafo:
    def __init__(self):
        self.adj_saida = {}
        self.adj_entrada = {}

    def adicionaVertice(self, v):
        if v not in self.adj_entrada:
            self.adj_entrada[v] = []
        if v not in self.adj_saida:
            self.adj_saida[v] = []

    def adicionaAresta(self, u, v):
        self.adicionaVertice(u)
        self.adicionaVertice(v)

        self.adj_saida[u].append(v)
        self.adj_saida[u].extend(self.adj_saida[v])
        self.adj_entrada[v].append(u)
        for w in self.adj_entrada[u]:
            if v not in self.adj_saida[w]:
                self.adj_saida[w].append(v)

    # BFS para ver se v é atingível a partir de u
    def converteChar(self, u, v):
        '''visitado, pilha = [], [u]
        while pilha:
            vertice = pilha.pop()
            if vertice in self.adj:
                for vizinho in self.adj[vertice]:
                    if vizinho == v:
                        return True
                    if vizinho not in visitado:
                        visitado.append(vizinho)
                        pilha.append(vizinho)'''
        if u in self.adj_saida:
            if v in self.adj_saida[u]:
                return True

        return False

    def converteString(self, str1, str2):
        if len(str1) != len(str2):
            return 'nao'

        for i in range(0, len(str1)):
            if str1[i] == str2[i]:
                continue
            if not self.converteChar(str1[i], str2[i]):
                return 'nao'

        return 'sim'

def main():
    grafo = Grafo()

    arq = input("Digite o nome ou endereço do arquivo: ")

    with open(arq) as f:
        n, m = f.readline().split()
        n = int(n)
        m = int(m)

        # Inicia lista de adjacências
        for i in range(0, n):
            u, v = f.readline().split()
            grafo.adicionaAresta(u, v)

        for i in range(0, m):
            str1, str2 = f.readline().split()
            print(grafo.converteString(str1, str2))


if __name__ == '__main__':
    main()