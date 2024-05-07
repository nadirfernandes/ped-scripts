from math import sqrt, erf

def tabela_normal_reduzida(z):
    return (1 + erf(z / sqrt(2))) / 2

# Exemplo de uso
z = 3.0 # O valor de z para o qual você deseja calcular a probabilidade
probabilidade = round(tabela_normal_reduzida(z),4)
print("Probabilidade para z =", z, ":", probabilidade)
