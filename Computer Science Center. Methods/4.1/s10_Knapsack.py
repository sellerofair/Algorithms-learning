# Первая строка содержит количество предметов 1 ≤ n ≤ 10^3 и вместимость рюкзака 0 ≤ W ≤ 2⋅10^6.
# Каждая из следующих n строк задаёт стоимость 0 ≤ c_i ≤ 2⋅10^6 и объём 0 < w_i ≤ 2⋅10^6 предмета
# (n, W, c_i, w_i — целые числа).
#
# Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
# стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
# с точностью не менее трёх знаков после запятой.

n, W = [int(c) for c in input().split()]
things = []

for _ in range(n):
    c, w = [int(x) for x in input().split()]
    things.append([c, w, c / w])

things.sort(key=lambda x: -x[2])

value = 0

for thing in things:
    if W <= 0:
        break
    elif thing[1] <= W:
        value += thing[0]
        W -= thing[1]
    else:
        value += thing[2] * W
        break

print(format(value, '.3f'))