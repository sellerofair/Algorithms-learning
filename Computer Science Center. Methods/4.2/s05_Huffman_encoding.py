# По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
# постройте оптимальный беспрефиксный код.
# В первой строке выведите количество различных букв k, встречающихся в строке,
# и размер получившейся закодированной строки.
# В следующих k строках запишите коды букв в формате "char: code".
# В последней строке выведите закодированную строку.

class Weighted:
    def __init__(self, _weight):
        self.weight = _weight


class Node(Weighted):
    def __init__(self, _weight, _left, _right):
        Weighted.__init__(self, _weight)
        self.left = _left
        self.right = _right

    def __str__(self):
        return 'Node {weight: ' + str(self.weight) + ', left: ' + str(self.left) + ', right: ' + str(self.right) + '}'


class Leaf(Weighted):
    def __init__(self, _name, _weight):
        self.name = _name
        Weighted.__init__(self, _weight)

    def __str__(self):
        return 'Leaf {name: ' + str(self.name) + ', weight: ' + str(self.weight) + '}'


class Forrest:
    content: list[Weighted]

    def __init__(self):
        self.content = []

    def insert(self, _unit):
        """ :param Weighted _unit: """
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


def code_former(_codes, _unit, _current_code):
    """
    :param dict _codes:
    :param Weighted _unit:
    :param str _current_code:
    """
    if isinstance(_unit, Leaf):
        _codes[_unit.name] = _current_code
    elif isinstance(_unit, Node):
        code_former(_codes, _unit.left, _current_code + '0')
        code_former(_codes, _unit.right, _current_code + '1')
    else:
        print('Unknown type of unit')


def tree_to_codes(_tree, _codes):
    """
    :param Weighted _tree:
    :param dict _codes:
    """
    if isinstance(_tree, Leaf):
        _codes[_tree.name] = '0'
    elif isinstance(_tree, Node):
        code_former(_codes, _tree, '')
    else:
        print('Unknown type of unit')


string = input()
dictionary = {}
forrest = Forrest()
codes = {}
encoded_string = ''

for char in string:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

for letter, weight in dictionary.items():
    forrest.insert(Leaf(letter, weight))

while len(forrest.content) > 1:
    i = forrest.extract_minimum()
    j = forrest.extract_minimum()
    forrest.insert(Node(i.weight + j.weight, i, j))

tree_to_codes(forrest.content[0], codes)

for char in string:
    encoded_string += codes[char]

print(len(codes), len(encoded_string))
for letter, code in codes.items():
    print(letter + ':', code)
print(encoded_string)
