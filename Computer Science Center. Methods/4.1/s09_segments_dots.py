# По данным n отрезкам необходимо найти множество точек минимального размера,
# для которого каждый из отрезков содержит хотя бы одну из точек.
#
# В первой строке дано число 1 ≤ n ≤ 100 отрезков.
# Каждая из последующих n строк содержит по два числа 0 ≤ l ≤ r ≤ 10^9, задающих начало и конец отрезка.
# Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них

n = int(input())
segments = []

for _ in range(n):
    segments.append([int(c) for c in input().split()])

segments.sort(key=lambda pair: pair[1])

res = []
m = segments[0][1]
res.append(m)

for seg in segments:
    if seg[0] > m:
        m = seg[1]
        res.append(m)

print(len(res))
print(*res)
