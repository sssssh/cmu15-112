def f(x):
    print("A", end="")
    if x == 0:
        print("B", end="")
        print("C", end="")
    else:
        print("D", end="")
        if x == 1:
            print("E", end="")
        else:
            print("F", end="")
    print("G")


f(0)
f(1)
f(2)
