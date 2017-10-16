import math


def f():
    print("This is a user-defined function")
    return 42


print("Some basic types in Python:")
print(type(2))
print(type(2.2))
print(type("2.2"))
print(type(2 < 2.2))
print(type(math))
print(type(math.tan))
print(type(f))
print(type(type(42)))


print("########################################################")


print("And some other types we will see later in the course...")
print(type(Exception()))
print(type(range(5)))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2}))
print(type({1: 42}))
print(type(2+3j))
