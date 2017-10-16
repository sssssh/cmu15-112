def f(w):
    return 10 * w


def g(x, y):
    return f(3 * x) + y


def h(z):
    return f(g(z, f(z + 1)))


print(h(1))  # how it do?
