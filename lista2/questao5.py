import math

def troco(T):
    moedas = {
        1: 0,
        5: 0,
        10: 0,
        25: 0,
        50: 0,
        100: 0
    }

    while(T > 0): # Criterio guloso: escolher maior moeda possivel. Colocar quantas der dela
        if T >= 100:
            moedas[100] = int(math.floor(T/100))
            T = T % 100
        elif T >= 50:
            moedas[50] = int(math.floor(T/50))
            T = T % 50
        elif T >= 25:
            moedas[25] = int(math.floor(T/25))
            T = T % 25
        elif T >= 10:
            moedas[10] = int(math.floor(T/10))
            T = T % 10
        elif T >= 5:
            moedas[5] = int(math.floor(T/5))
            T = T % 5
        elif T >= 1: 
            moedas[1] = T
            T = 0
    return moedas

def main():
    T = int(input("T = "))
    moedas = troco(T)

    print("{} pode ser representado por:".format(T))
    if moedas[1] != 0:
        if moedas[1] == 1:
            print("1 moeda de 1")
        else:
            print("{} moedas de 1".format(moedas[1]))

    if moedas[5] != 0:
        if moedas[5] == 1:
            print("1 moeda de 5")
        else:
            print("{} moedas de 5".format(moedas[5]))

    if moedas[10] != 0:
        if moedas[10] == 1:
            print("1 moeda de 10")
        else:
            print("{} moedas de 10".format(moedas[10]))

    if moedas[25] != 0:
        if moedas[25] == 1:
            print("1 moeda de 25")
        else:
            print("{} moedas de 25".format(moedas[25]))

    if moedas[50] != 0:
        if moedas[50] == 1:
            print("1 moeda de 50")
        else:
            print("{} moedas de 50".format(moedas[50]))

    if moedas[100] != 0:
        if moedas[100] == 1:
            print("1 moeda de 100")
        else:
            print("{} moedas de 100".format(moedas[100]))

if __name__ == '__main__':
    main()