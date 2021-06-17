# По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
# постройте оптимальный беспрефиксный код.
# В первой строке выведите количество различных букв k, встречающихся в строке,
# и размер получившейся закодированной строки.
# В следующих k строках запишите коды букв в формате "char: code".
# В последней строке выведите закодированную строку.

class Node:
    def __init__(self, _weight, _left, _right):
        self.weight = _weight
        self.left = _left
        self.right = _right

    def __str__(self):
        return 'Node {weight: ' + str(self.weight) + ', left: ' + str(self.left) + ', right: ' + str(self.right) + '}'


class Leaf:
    def __init__(self, _name, _weight):
        self.name = _name
        self.weight = _weight

    def __str__(self):
        return 'Leaf {name: ' + str(self.name) + ', weight: ' + str(self.weight) + '}'


class Forrest:
    def __init__(self):
        self.content = []

    def insert(self, _unit):
        self.content.append(_unit)

    def extract_minimum(self):
        minimum = self.content[0]
        for unit in self.content:
            if unit.weight < minimum.weight:
                minimum = unit
        self.content.remove(minimum)
        return minimum

    def __str__(self):
        if len(self.content) == 0:
            return 'Forrest []'
        result = 'Forrest ['
        for unit in self.content:
            result += str(unit) + ' ,'
        result = result[:-2] + ']'
        return result


string = input()
dictionary = {}

for char in string:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

forrest = Forrest()

for letter, weight in dictionary.items():
    forrest.insert(Leaf(letter, weight))

while len(forrest.content) > 1:
    i = forrest.extract_minimum()
    j = forrest.extract_minimum()
    forrest.insert(Node(i.weight + j.weight, i, j))

print(forrest)
