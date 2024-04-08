import math

def comb(n, k):
    """
    Calcula combinações de n elementos tomados k a k.
    
    Argumentos:
    n -- número total de elementos
    k -- número de elementos a serem escolhidos
    
    Retorna:
    O número de combinações possíveis
    """
    if k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))







print("1 - Distribuição Hipergeométrica")
print("2 - Distribuição Binomial")
print("3 - Distribuição de Poisson")
print("4 - Distribuição Geométrica")
print()

term = int(input("Escolha o tipo de distribuição pretendida: "))

match term:
    case 1:
        print()
        print("Distribuição Hipergeométrica de parâmetros (N,M,n) [X~H(N,M,n)]")
        print()
        print("1 - Função de probabilidade")
        print("2 - Valor médio")
        print("3 - Variância")
        print("4 - Desvio padrão")

        choice = int(input("Escolha a área pretendida: "))
        match choice:
            case 1:
                print()
                nGrande = int(input("N: "))
                m = int(input("M: "))
                n = int(input("n: "))
                k = int(input("k: "))
                res = (comb(m,k)*comb(nGrande-m,n-k))/comb(nGrande,n)
                print(f"Resultado: {res}")
            case 2:
                print()
                nGrande = int(input("N: "))
                m = int(input("M: "))
                n = int(input("n: "))
                res = n*(m/nGrande)
                print(f"Resultado: {res}")
            case 3:
                print()
                nGrande = int(input("N: "))
                m = int(input("M: "))
                n = int(input("n: "))
                res = (n*(m/nGrande)) * (1-(m/nGrande)) * ((nGrande-n)/(nGrande-1))
                print(f"Resultado: {res}")
            case 4:
                print()
                v = int(input("V: "))
                res = math.sqrt(v)
                print(f"Resultado: {res}")
    case 2:
        print()
        print("Distribuição Binomial de parâmetros (n,p) [X~B(n,p)]")
        print()
        print("1 - Função de probabilidade")
        print("2 - Valor médio")
        print("3 - Variância")

        choice = int(input("Escolha a área pretendida: "))
        match choice:
            case 1:
                print()
                n = int(input("n: "))
                p = float(input("p: "))
                k = int(input("k: "))
                res = comb(n,k) * (p ** k) * ((1-p) ** (n-k))
                print(f"Resultado: {res}")
            case 2:
                print()
                n = int(input("n: "))
                p = float(input("p: "))
                res = n*p
                print(f"Resultado: {res}")
            case 3:
                print()
                n = int(input("n: "))
                p = float(input("p: "))
                res = n*p*(1-p)
                print(f"Resultado: {res}")
    case 3:
        print()
        print("Distribuição Poisson de parâmetro λ [X~P(λ)]")
        print()
        print("1 - Função de probabilidade")
        print("2 - Valor médio")
        print("3 - Variância")
        print("4 - Lamda (λ)")

        choice = int(input("Escolha a área pretendida: "))
        match choice:
            case 1:
                print()
                λ = int(input("λ: "))
                k = int(input("k: "))
                res = (math.e ** -λ) * ((λ ** k) / math.factorial(k))
                print(f"Resultado: {res}")
            case 2:
                print()
                λ = int(input("λ: "))
                res = λ
                print(f"Resultado: {res}")
            case 3:
                print()
                λ = int(input("λ: "))
                res = λ
                print(f"Resultado: {res}")
            case 4:
                print()
                n = int(input("n: "))
                p = float(input("p: "))
                res = n*p
                print(f"Resultado: {res}")

    case 4:
        print()
        print("Distribuição Geométrica de parâmetro p [X~G(p)]")
        print()
        print("1 - Função de probabilidade")
        print("2 - Valor médio")
        print("3 - Variância")

        choice = int(input("Escolha a área pretendida: "))
        match choice:
            case 1:
                print()
                p = float(input("p: "))
                k = int(input("k: "))
                res = p * ((1-p) ** (k-1))
                print(f"Resultado: {res}")
            case 2:
                print()
                p = float(input("p: "))
                res = 1/p
                print(f"Resultado: {res}")
            case 3:
                print()
                p = float(input("p: "))
                res = (1-p) / (p ** 2)
                print(f"Resultado: {res}")