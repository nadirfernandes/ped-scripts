import math
from math import sqrt, erf

while True:

    def tabela_normal_reduzida(z):
        return (1 + erf(z / sqrt(2))) / 2


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
    print("5 - Distribuição Uniforme")
    print("6 - Distribuição Exponencial")
    print("7 - Função de Distribuição do Modelo Normal Reduzido")
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
            print("4 - Intervalos de probabilidades")

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
                case 4:
                    print()
                    print("1 - P(X ≤ k)")
                    print()

                    choice2 = int(input("Escolha o tipo de probabilidade pretendida: "))
                    match choice2:
                        case 1:
                            print()
                            n = int(input("n: "))
                            p = float(input("p: "))
                            k = int(input("k: "))

                            result = 0

                            for k in range(0, k+1):
                                res = comb(n,k) * (p ** k) * ((1-p) ** (n-k))
                                result = result + res

                            print(f"Resultado: {result}")
        case 3:
            print()
            print("Distribuição Poisson de parâmetro λ [X~P(λ)]")
            print()
            print("1 - Função de probabilidade")
            print("2 - Valor médio")
            print("3 - Variância")
            print("4 - Lamda (λ)")
            print("5 - Processo de Poisson")
            print()

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
                case 5:
                    print()
                    print("1 - P(X ≤ Nt ≤ Y)")
                    print("2 - P(X < Nt ≤ Y)")
                    print("3 - P(X ≤ Nt < Y)")
                    print("4 - P(X < Nt < Y)")
                    print("5 - P(Nt ≤ X)")
                    print("6 - P(Nt < X)")
                    print()


                    choice2 = int(input("Escolha o tipo de probabilidade pretendida: "))
                    match choice2:
                        case 1:
                            print()
                            beta = float(input("β: "))
                            t = float(input("t: "))
                            w = int(input("X: "))
                            y = int(input("Y: "))

                            lamb = beta*t

                            result = 0

                            for x in range(w, y+1):
                                res = (math.e ** -lamb) * ((lamb ** x) / math.factorial(x))
                                result = result + res

                            print(f"Resultado: {result}")

                        case 2:
                            print()
                            beta = float(input("β: "))
                            t = float(input("t: "))
                            w = int(input("X: "))
                            y = int(input("Y: "))

                            lamb = beta*t

                            result = 0

                            for x in range(w+1, y+1):
                                res = (math.e ** -lamb) * ((lamb ** x) / math.factorial(x))
                                result = result + res

                            print(f"Resultado: {result}")

                        case 3:
                            print()
                            beta = float(input("β: "))
                            t = float(input("t: "))
                            w = int(input("X: "))
                            y = int(input("Y: "))

                            lamb = beta*t

                            result = 0

                            for x in range(w, y):
                                res = (math.e ** -lamb) * ((lamb ** x) / math.factorial(x))
                                result = result + res

                            print(f"Resultado: {result}")

                        case 4:
                            print()
                            beta = float(input("β: "))
                            t = float(input("t: "))
                            w = int(input("X: "))
                            y = int(input("Y: "))

                            lamb = beta*t

                            result = 0

                            for x in range(w+1, y):
                                res = (math.e ** -lamb) * ((lamb ** x) / math.factorial(x))
                                result = result + res

                            print(f"Resultado: {result}")

                        case 5:
                            print()
                            beta = float(input("β: "))
                            t = float(input("t: "))
                            w = int(input("X: "))

                            lamb = beta*t

                            result = 0

                            for x in range(0, w+1):
                                res = (math.e ** -lamb) * ((lamb ** x) / math.factorial(x))
                                result = result + res

                            print(f"Resultado: {result}")

                        case 6:
                            print()
                            beta = float(input("β: "))
                            t = float(input("t: "))
                            w = int(input("X: "))

                            lamb = beta*t

                            result = 0

                            for x in range(0, w):
                                res = (math.e ** -lamb) * ((lamb ** x) / math.factorial(x))
                                result = result + res

                            print(f"Resultado: {result}")


        case 4:
            print()
            print("Distribuição Geométrica de parâmetro p [X~G(p)]")
            print()
            print("1 - Função de probabilidade")
            print("2 - Valor médio")
            print("3 - Variância")
            print()
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
        case 5:
            print()
            print("Distribuição Uniforme de parâmetros (a,b) [X~U(a,b)]")
            print()
            print(" Função densidade de probabilidade:")
            print("f(x) = { 1/(b-a), x ∈ [a,b] ; 0, x ∉ [a,b]" )
            print()
            print("Função distribuição:")
            print("Fx(x) = P(X ≤ x) = { 0, x < a ; (x-a)/(b-a), a ≤ x < b ; 1, x ≥ b")
            print()
            print("1 - Valor médio")
            print("2 - Valor médio ^2")
            print("3 - Variância")
            print()
            choice = int(input("Escolha a área pretendida: "))
            match choice:
                case 1:
                    print()
                    a = int(input("a: "))
                    b = int(input("b: "))
                    res = (a+b)/2
                    print(f"Resultado: {res}")
                case 2:
                    print()
                    a = int(input("a: "))
                    b = int(input("b: "))
                    res = ( (b**2) + a*b + (a**2) )/3
                    print(f"Resultado: {res}")
                case 3:
                    print()
                    a = int(input("a: "))
                    b = int(input("b: "))
                    res = ((b-a) ** 2)/12
                    print(f"Resultado: {res}")
        case 6:
            print()
            print("Distribuição Exponencial de parâmetros (λ,δ) [X~E(λ,δ)]")
            print()
            print("1 - Valor médio")
            print("2 - Variância")
            print()
            choice = int(input("Escolha a área pretendida: "))
            match choice:
                case 1:
                    print()
                    lamda = int(input("λ: "))
                    delta = int(input("δ: "))
                    res = lamda+delta
                    print(f"Resultado: {res}")
                case 2:
                    print()
                    delta = int(input("δ: "))
                    res = delta ** 2
                    print(f"Resultado: {res}")
        case 7:
            print()
            print("Φ(z) = P (Z ≤ z)")
            print()
            z = float(input("z: "))
            probabilidade = round(tabela_normal_reduzida(z),4)
            print("Probabilidade: ", probabilidade)




    print()
    user_input = input("Quer terminar o programa (Escreva s ou n)? ").lower()
    if user_input == "s":
        break


