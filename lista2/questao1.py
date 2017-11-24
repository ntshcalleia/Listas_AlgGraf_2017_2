# ALGORITMO que encontra uma das árvores geradoras com menor altura:
# Fazer BL com todos os vértices
# Resposta vai ser a BL com menor altura
# Complexidade: O(N(N + M))

class Grafo: # Não-direcionado
    def __init__(self, n_vertices):
        self.V = n_vertices
        self.adj = []
        for i in range(n_vertices): # Inicia lista de adjs
            self.adj.append([])

    def adiciona_aresta(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def busca_largura(self, r):
        nivel = [-1] * self.V
        nivel[r] = 0
        pilha = [r]
        visitado = [False] * self.V
        a = Arvore(self.V, r)

        while pilha:
            v = pilha.pop(0)
            visitado[v] = True
            for u in self.adj[v]:
                if not visitado[u]: # Foda-se aresta que não é de árvore
                    visitado[u] = True
                    nivel[u] = nivel[v] + 1
                    a.altura = max(nivel[u], a.altura) # Atualiza altura da árvore
                    pilha.append(u)
                    a.adiciona_aresta(u, v)
        return a

class Arvore(Grafo): # Grafo com atributos altura e raíz
    def __init__(self, n_vertices, r):
        super(Arvore, self).__init__(n_vertices)
        self.raiz = r
        self.altura = 0

def main():
    # Inicializa o grafo
    g = Grafo(6)
    arestas = [(0,1), (0,2), (0,5), (2,1), (2,3), (2,4), (3,4), (3,5)]
    for aresta in arestas:
        g.adiciona_aresta(aresta[0], aresta[1])

    # Busca a resposta
    resposta = Arvore(g.V, -1) # Vai ser uma arvore A com V(A) = V(G)
    resposta.altura = float("inf")
    for i in range(g.V): # O(N(M + N))
        nova_bl = g.busca_largura(i) # Faz BL com todas as raízes
        if nova_bl.altura < resposta.altura:
            resposta = nova_bl

    # Imprime a resposta
    print("A menor árvore geradora enraizada desse grafo tem altura {} e sua raíz é o vértice {}:".format(resposta.altura, resposta.raiz))
    print(resposta.adj)


if __name__ == '__main__':
    main()