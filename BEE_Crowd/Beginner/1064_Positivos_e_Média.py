#  Problema: 1064 - Positivos e Média
#  Link: https://judge.beecrowd.com/pt/problems/view/1064
#  Categoria: Beginner

entradas = []
valores = 0
positivo = 0

while True:
    if len(entradas) < 6:
        entrada = float(input())
        entradas.append(entrada)
        continue
    break

for i in entradas:
    if i > 0:
        valores = valores + i
        positivo = positivo + 1

media = valores / positivo

print(f"{positivo} valores positivos")
print(f"{media:.1f}")
