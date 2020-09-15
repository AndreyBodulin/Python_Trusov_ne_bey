import math as m


# Декоратор с аргументами оборачиваемой функции
def square(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res ** 2

    return wrapper


# Декоратор, который сам может принимать аргументы


def pow(power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = 1
            for i in range(power):
                res *= func(*args, **kwargs)
            return res

        return wrapper

    return decorator


def lim(a):
    def decorator(func):
        def wrapper(*args, **kwargs):
            Del = 0.00000001
            y = func(a)
            y1 = func(a - Del)
            y2 = func(a + Del)
            Eps = m.fabs(y - y1)
            i = a - Del
            while i <= (a + Del):
                if (y1 <= func(i)) and (y2 >= func(i)):
                    True
                else:
                    break
                i += (Del / 2)
            print(y)
        return wrapper
    return decorator


@lim(a=1)
def f4(x):
    return (2 * x**2 - 3 * x - 5) / (x + 1)


f4()


@square
def f2(a, b, c):
    return a + b + c


@pow(power=3)
def f3(c, d):
    return c - d


'''Декоратор который считает предел функции в точке '''
