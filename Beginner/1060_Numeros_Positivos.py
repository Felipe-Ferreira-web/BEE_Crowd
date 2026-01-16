# Problema: 1060 - Números Positivos
# Link: https://judge.beecrowd.com/pt/problems/view/1060
# Categoria: Beginner

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())

x = 0

if num1 > 0:
    x = x + 1
if num2 > 0:
    x = x + 1
if num3 > 0:
    x = x + 1
if num4 > 0:
    x = x + 1
if num5 > 0:
    x = x + 1
if num6 > 0:
    x = x + 1

print(f"{x} valores positivos")
