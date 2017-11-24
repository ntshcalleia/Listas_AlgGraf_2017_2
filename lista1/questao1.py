# ENTRADA: Matriz de adjacências de um grafo
# SAÍDA: Lista de adjacências do grafo

# http://danielamaral.wdfiles.com/local--files/agmmo/Grafo.png
ENTRADA_EXEMPLO = [[0, 1, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 0],
                   [0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 1, 1],
                   [1, 1, 0, 1, 0, 0],
                   [0, 0, 0, 1, 0, 0]]

def matriz_para_lista(matriz):
    lista_adjacencias = [None]
    n = len(matriz) # n = número de vértices

    for i in range(n):
        lista_adjacencias.append([])

    for i in range(n):
        for j in range(i + 1, n):
            print("Valor na posição {},{}: {}".format(i, j, matriz[i][j]))
            if matriz[i][j]:
                v = i + 1
                w = j + 1
                lista_adjacencias[v].append(w)
                lista_adjacencias[w].append(v)
    return lista_adjacencias

print(matriz_para_lista(ENTRADA_EXEMPLO))

# ALGORITMO:
# inicia lista_adjacencias
# para cada linha v na matriz:
#   para cada coluna w na matriz tal que w > v:
#       se matriz[v][w] == 1
#           lista_adjacencias[v].append(w)
#           lista_adjacencias[w].append(v)

# Para funcionar para digrafos, precisamos remover a linha 26 e consultar toda a
# matriz do grafo (na linha 20, consultar no range(0, n)). Se quisermos adj+ e
# adj-, podemos iniciar duas listas de adj e, quando encontrar uma aresta, fazer
# adj-[v].append(w) e adj+[w].append(v)
#
# Sobre a complexidade, como precisamos consultar cada valor da matriz (nessa
# implementação não, mas a complexidade assintótica continua a mesma), ela é
# O(n*n). Não temos como encontrar uma complexidade menor que essa, ou seja,
# esse é o limite inferior desse problema
