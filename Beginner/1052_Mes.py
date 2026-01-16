# Problema: 1052 - Mês
# Link: https://judge.beecrowd.com/pt/problems/view/1052
# Categoria: Beginner

mes = str(input())

meses = [
    {"num": "1", "nome": "January"},
    {"num": "2", "nome": "February"},
    {"num": "3", "nome": "March"},
    {"num": "4", "nome": "April"},
    {"num": "5", "nome": "May"},
    {"num": "6", "nome": "June"},
    {"num": "7", "nome": "July"},
    {"num": "8", "nome": "August"},
    {"num": "9", "nome": "September"},
    {"num": "10", "nome": "October"},
    {"num": "11", "nome": "November"},
    {"num": "12", "nome": "December"},
]


def calendario(mes):
    for i in meses:
        num, nome = i.values()
        if num == mes:
            return print(nome)


calendario(mes)
