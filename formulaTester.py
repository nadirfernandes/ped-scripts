import math










print("5 - P(X ≤ k)")

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

n = int(input("n: "))
p = float(input("p: "))
k = int(input("k: "))

result = 0

for k in range(0, k+1):
    res = comb(n,k) * (p ** k) * ((1-p) ** (n-k))
    result = result + res

print(f"Resultado: {result}")




