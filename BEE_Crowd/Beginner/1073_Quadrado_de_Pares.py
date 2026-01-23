# Problema: 1073 - Quadrado de Pares
# Link: https://judge.beecrowd.com/pt/problems/view/1073
# Categoria: Beginner

n = 2 + int(input())
r1 = 2
r2 = 2

for i in range(2, n, 2):
    r1 = i**2
    print(f"{i}^2 = {r1}")
