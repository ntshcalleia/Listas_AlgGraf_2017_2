
def egipcio(n, d):
    if n == 1:
        return "1/{}".format(d)

    fracao = ""
    soma = 0
    i = 2
    e = 1e-6 # Margem de erro p/ lidar com floating point precision

    if (n/d <= e):
        return "Valor muito pequeno ({})! Tente outro valor ou aumente a precisão".format(n/d)

    while (n/d - soma > e):
        if (soma + 1/i <= n/d): # Critério guloso: pegar maior fração possível
            fracao = fracao + "1/{} + ".format(i)
            soma = soma + 1/i
        else:
            i = i + 1

    return fracao[:-2]

def main():
    n = int(input("Numerador: "))
    d = int(input("Denominador: "))

    print("{}/{} = ".format(n, d) + egipcio(n, d))


if __name__ == '__main__':
    main()