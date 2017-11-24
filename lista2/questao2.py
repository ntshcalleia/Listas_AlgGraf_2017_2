
class Grafo:
    def __init__(self, n_vertices):
        self.V = n_vertices
        self.adj = []
        for i in range(n_vertices):
            self.adj.append([])

    def adiciona_aresta(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def busca_prof(self, u, visitado, pai, low, pe):
        for v in self.adj[u]:
                if not visitado[v]:
                    pe[self.V] = pe[self.V] + 1
                    pe[v] = pe[self.V]
                    pai[v] = u
                    visitado[v] = True
                    self.busca_prof(v, visitado, pai, low, pe)
                    if pe[low[v]] < pe[low[u]]:
                        low[u] = low[v]
                elif pe[low[v]] < pe[low[u]] and pai[u] != v:
                    low[u] = low[v]

    def busca_pontes(self):
        pontes = []
        visitado = [True] + [False] * (self.V - 1)
        pe = [1] + [0] * (self.V - 1) + [1]
        pai = [-1] * self.V
        low = [0] * self.V
        for i in range(self.V):
            low[i] = i
        self.busca_prof(0, visitado, pai, low, pe)

        for v in range(self.V):
            if low[v] == v and pai[v] >= 0:
                pontes.append((pai[v], v))

        return pontes

def main():
    G = Grafo(6)
    arestas = [(0,1), (0,2), (2,3), (2,4), (4,5), (2,5), (0,4)]
    for aresta in arestas:
        G.adiciona_aresta(aresta[0], aresta[1])

    print("Pontes:")
    print(G.busca_pontes())


if __name__ == '__main__':
    main()