# Очередь с приоритетами
#
# Первая строка входа содержит число операций 1 ≤ n ≤ 10^5.
# Каждая из последующих n строк задают операцию одного из следующих двух типов:
#  - Insert x, где 0 ≤ x ≤ 10^9 — целое число;
#  - ExtractMax.
# Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.


def insert(ls, x):
    ls.append(x)
    i = len(ls) - 1
    while i > 0:
        j = (i - 1) // 2
        parent = ls[j]
        if parent < x:
            ls[i], ls[j] = parent, x
            i = j
        else:
            break


def extract_max(ls):
    if len(ls) <= 0:
        return
    if len(ls) == 1:
        maximum = ls.pop()
    elif len(ls) == 2:
        maximum = ls.pop(0)
    else:
        maximum = ls[0]
        sifted = ls[-1]
        ls[0], ls[-1] = sifted, maximum
        ls.pop()

        i = 0
        while True:
            j = i * 2 + 1
            if j > len(ls) - 1:
                break
            if j <= len(ls) - 2 and ls[j] < ls[j + 1]:
                j += 1
            child = ls[j]
            if sifted < child:
                ls[i], ls[j] = child, sifted
                i = j
            else:
                break

    print(maximum)
    return maximum


operation_dict = {
    'Insert': insert,
    'ExtractMax': extract_max
}

priority_queue = []

n = int(input())

for _ in range(n):
    operation = input().split()
    operation_dict[operation[0]](priority_queue, *[int(x) for x in operation[1:]])
