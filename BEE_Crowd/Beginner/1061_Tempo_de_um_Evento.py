# Problema: 1061 - Tempo de um Evento
# Link: https://judge.beecrowd.com/pt/problems/view/1061
# Categoria: Beginner

di = input()  # dia inicial
hi = input()  # hora inicial
df = input()  # dia final
hf = input()  # hora final

di = di[4:]
hri, mni, sgi = hi[0:2], hi[5:7], hi[10:13]
di, hri, mni, sgi = map(int, [di, hri, mni, sgi])

df = df[4:]
hrf, mnf, sgf = hf[0:2], hf[5:7], hf[10:13]
df, hrf, mnf, sgf = map(int, [df, hrf, mnf, sgf])

min_segs = 60
hora_segs = 3600
dia_segs = 3600 * 24

inicio = sgi + mni * min_segs + hri * hora_segs + di * dia_segs
fim = sgf + mnf * min_segs + hrf * hora_segs + df * dia_segs

if inicio < fim:
    t = fim - inicio
    dia = int(t / dia_segs)
    t = t % dia_segs
    hora = int(t / hora_segs)
    t = t % hora_segs
    minu = int(t / min_segs)
    t = t % min_segs
    segs = int(t)

print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minu} minuto(s)")
print(f"{segs} segundo(s)")
