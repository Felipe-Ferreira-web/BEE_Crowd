# Problema: 1071 - Soma de Impares Consecutivos I
# Link: https://judge.beecrowd.com/pt/problems/view/1071
# Categoria: Beginner


def soma_impares(n1, n2):
    valores = []
    soma = 0

    if n1 == n2:
        return print("0")

    if n1 > n2:
        n1 = n1 - 1
        for i in range(n1, n2, -1):
            valores.append(i)
    else:
        n1 = n1 + 1
        for i in range(n1, n2, 1):
            valores.append(i)

    for i in valores:
        if i % 2 != 0:
            soma = soma + (i)

    return print(soma)


n1 = int(input())
n2 = int(input())

soma_impares(n1, n2)
