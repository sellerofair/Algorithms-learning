import time


def fib1(n):
    """ Наивный алгоритм """
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


def fib2(n, _cache):
    """ Алгоритм с использованием глобальной переменной, в которую сохраняются вычисленные значения """
    assert n >= 0
    if n not in _cache:
        _cache[n] = n if n <= 1 else fib2(n - 1, _cache) + fib2(n - 2, _cache)
    return _cache[n]


def memo(f):
    """
    Декоратор, внутри которого создается локальная переменная cache
    Аналог lru_cache из стандартной библиотеки functools
    """
    local_cache = {}

    def inner(n):
        if n not in local_cache:
            local_cache[n] = f(n)
        return local_cache[n]

    return inner


def fib3(n):
    """ Алгоритм с итерациями вместо рекурсий """
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def timed(f, *args, n_iter=100):
    """ Вычисляет время работы функции """
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


print(fib1(10))
print(timed(fib1, 10))

cache = {}
print(fib2(100, cache))
cache.clear()
print(timed(fib2, 100, cache))

fib1 = memo(fib1)
print(fib1(100))
print(timed(fib1, 100))

print(fib3(10000))
print(timed(fib3, 100000))
