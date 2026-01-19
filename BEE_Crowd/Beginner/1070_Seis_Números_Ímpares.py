# Problema: 1070 - Seis Números Ímpares
# Link: https://judge.beecrowd.com/pt/problems/view/1070
# Categoria: Beginner

valor = int(input())

final = valor + 12

if valor % 2 == 0:
    valor = valor + 1
    for i in range(valor, final, 2):
        print(i)
else:
    for i in range(valor, final, 2):
        print(i)
