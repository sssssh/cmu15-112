def f(x):
    print("In f, x =", x)
    x += 5
    return x


def g(x):
    return f(x * 2) + f(x * 3)


print(g(2))
