LIVRE = 0
PAREDE = 1
PORTAL = 2

def busca_larg(matriz, raiz_i, raiz_j, n_linhas, n_colunas, portais):
    fila = []
    fila.append([raiz_i, raiz_j, 0])
    naoEncontreiCaminho = True
    livre = []

    def processa_vizinho(i, j):
        livre[i][j] = False
        fila.append([i, j, altura + 1])

    # Inicializa livre
    for i in range(n_colunas):
        aux = []
        for j in range(n_linhas):
            aux.append(True)
        livre.append(aux)
    livre[raiz_i][raiz_j] = False

    while naoEncontreiCaminho:
        v = fila.pop(0)
        i, j, altura = v[0], v[1], v[2]
        # Checa se chegou no destino:
        if i == (n_linhas - 1) and j == (n_colunas - 1):
            return altura

        # Se portal, checa o outro portal
        if matriz[i][j] == PORTAL:
            if portais[0] == [i, j] and livre[portais[1][0]][portais[1][1]]:
                altura = altura - 1
                processa_vizinho(portais[1][0], portais[1][1])
            elif livre[portais[0][0]][portais[1][1]]:
                altura = altura - 1
                processa_vizinho(portais[0][0], portais[0][1])

        # Checa vizinho da direita:
        if (j + 1) < n_colunas and matriz[i][j + 1] != PAREDE and livre[i][j + 1]:
            processa_vizinho(i, j + 1)
        # Checa vizinho de baixo:
        if (i + 1) < n_linhas and matriz[i + 1][j] != PAREDE and livre[i + 1][j]:
            processa_vizinho(i + 1, j)
        # Checa vizinho da esquerda:
        if j != 0 and matriz[i][j - 1] != PAREDE and livre[i][j - 1]:
            processa_vizinho(i, j - 1)
        # Checa vizinho de cima:
        if i != 0 and matriz[i - 1][j] != PAREDE and livre[i - 1][j]:
            processa_vizinho(i - 1, j)

        # Debugging portal
        if len(fila) == 0:
            return -1

def main():
    path = input("Arquivo:\n")
    with open(path, "r") as arq:
        matriz = []
        portais = []
        linha1 = str(arq.readline().strip()).split()
        n_linhas = int(linha1[0])
        n_colunas = int(linha1[1])

        # Adiciona valores linha por linha
        for i in range(n_linhas):
            linha = str(arq.readline().strip()).split()
            linha = [int(i) for i in linha]
            matriz.append(linha)
            # Checa se tem um portal na linha
            if len(portais) < 2:
                for j in range(n_colunas):
                    if linha[j] == PORTAL:
                        portais.append([i, j])
        print(busca_larg(matriz, 0, 0, n_linhas, n_colunas, portais))

if __name__ == '__main__':
    main()
