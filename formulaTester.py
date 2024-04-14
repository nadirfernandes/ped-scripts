import math


print("2 - P(Nt < X)")
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





