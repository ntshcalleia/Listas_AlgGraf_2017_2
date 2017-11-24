# IMPRIME APENAS UMA ORDENAÇÃO HEAD TO TAIL, A LISTA PODE TER OUTRAS

def busca_prof(G, raiz, caminho, livre):
    livre[raiz] = False
    for v in G[raiz]: # Para cada vizinho da raíz
        if livre[v]: # livre[v]: Flag que indica se vértice já está no caminho
            caminho.append(v)
            if len(caminho) != len(G):
                busca_prof(G, v, caminho, livre)
            if len(caminho) == len(G): # Precisamos checar de novo se achamos a
                return caminho # resposta depois de sair do nested busca_prof().
    caminho.pop()
    livre[raiz] = True


def head_to_tail(lista):
    aux = 0
    ordenado = None
    livre = {}
    G = {}

    # Inicia listas de adjacências:
    for palavra in lista: # Palavras são vértices
        G[palavra] = set()

    # Transforma lista em grafo direcionado:
    for i in range(len(lista)):
        livre[lista[i]] = True
        for j in range(len(lista)):
            if (i == j):
                continue
            palavra1 = lista[i].lower()
            palavra2 = lista[j].lower()
            if palavra1.endswith(palavra2[0]):
                G[lista[i]].add(lista[j])
            if palavra2.endswith(palavra1[0]):
                G[lista[j]].add(lista[i])

    # Tenta fazer busca_prof() usando todos os vértices como raíz
    while ordenado == None and aux < len(G):
        ordenado = busca_prof(G, lista[aux], [lista[aux]], livre)
        aux += 1

    if ordenado == None:
        return -1
    return ordenado

def main():
    path = input("Arquivo:\n")
    with open(path, "r") as arq:
        n = arq.readline()
        lista = []
        for i in range(int(n)):
            lista.append(arq.readline().strip()) # .strip remove o "\n"

    print(head_to_tail(lista))

if __name__ == '__main__':
    main()

# Não tratei erros porque estou assumindo que a entrada vai estar no formato
# correto.
