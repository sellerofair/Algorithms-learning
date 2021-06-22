# Расстановка скобок в коде
# Проверяет правильность расстановки скобок в строке.

# Формат входа.
# Строка s[1 ... n], состоящая из заглавных и прописных букв латинского алфавита, цифр,
# знаков препинания и скобок из множества []{}().

# Формат выхода.
# Если скобки в s расставлены правильно, выведите строку “Success".
# В противном случае выведите индекс (используя индексацию с единицы) первой закрывающей скобки, для
# которой нет соответствующей открывающей. Если такой нет, выведите индекс первой открывающей скобки,
# для которой нет соответствующей закрывающей.


opening_brackets = ['(', '[', '{']
closing_brackets = [')', ']', '}']
brackets_parity = {
    ')': '(',
    ']': '[',
    '}': '{'
}


def check_brackets(string):
    brackets_stack = []
    indices_stack = []

    for i in range(len(string)):
        c = string[i]
        if c in opening_brackets:
            brackets_stack.append(c)
            indices_stack.append(i)
        elif c in closing_brackets:
            if len(brackets_stack) == 0 or brackets_parity[c] != brackets_stack.pop():
                print(i + 1)
                break
            indices_stack.pop()

    else:
        if len(brackets_stack) == 0:
            print('Success')
        else:
            print(indices_stack.pop() + 1)


check_brackets(input())
