# Problema: 1051 - Imposto de Renda
# Link: https://judge.beecrowd.com/pt/problems/view/1051
# Categoria: Beginner

salario = float(input())

if salario <= 2000:
    print("Isento")

elif salario > 2000 and salario <= 3000:
    valor = salario - 2000
    imposto = valor * 0.08
    print(f"R$ {imposto:.2f}")  # Mostra o resultado sempre com duas casas decimais

elif salario > 3000 and salario <= 4500:
    salario = salario - 2000  # parcela de isenção
    valor_08 = 1000 * 0.08  # parcelo de 8%
    imposto = ((salario - 1000) * 0.18) + valor_08
    print(f"R$ {imposto:.2f}")

elif salario > 4500:
    salario = salario - 2000  # parcela de isenção
    valor_08 = 1000 * 0.08  # parcela de 8%
    valor_18 = 1500 * 0.18  # parcela 18%
    imposto = (
        ((salario - 2500) * 0.28) + valor_08 + valor_18
    )  # Subtrai as parcelas já calculadas e soma o valor total
    print(f"R$ {imposto:.2f}")
