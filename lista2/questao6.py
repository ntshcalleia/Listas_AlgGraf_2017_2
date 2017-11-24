class Grafo:
    def __init__(self, n_vertices):
        self.V = n_vertices
        self.adj = []
        for i in range(n_vertices):
            self.adj.append([])

    def adiciona_aresta(self, u, v, p):
        self.adj[u].append([v, p])
        self.adj[v].append([u, p])

    def dijkstra_modificado(self, inicio, destino):
        def menor_vertice(vizinhanca):
            menor = vizinhanca[0]
            for v in vizinhanca:
                if d[v] < d[menor]:
                    menor = v
            return menor

        visitado = [False] * self.V
        menor_adj = [-1] * self.V
        d = [float("inf")] * self.V
        vizinhanca = []
        caminho = []
        for i in range(self.V):
            caminho.append([])
        vizinhanca.append(inicio)
        d[inicio] = 0
        caminho[inicio].append(inicio)

        while len(vizinhanca):
            u = menor_vertice(vizinhanca)
            vizinhanca.remove(u)
            caminho[u] = caminho[menor_adj[u]] + [u]
            for v in self.adj[u]:
                v, peso = v[0], v[1]
                temp_dist = d[u] + peso
                if temp_dist < d[v]:
                    d[v] = temp_dist
                    menor_adj[v] = u
                if not visitado[v]:
                    visitado[v] = True
                    vizinhanca.append(v)

            if len(caminho[destino]):
                break

        return d[destino], caminho[destino]




def main():
    g = Grafo(6)
    arestas = [(0,1,10), (0,2,5), (0,5,2), (2,1,17), (2,3,0), (2,4,12), (3,4,5), (3,5,3)]
    for aresta in arestas:
        g.adiciona_aresta(aresta[0], aresta[1], aresta[2])

    print(g.dijkstra_modificado(1, 5))


if __name__ == '__main__':
    main()