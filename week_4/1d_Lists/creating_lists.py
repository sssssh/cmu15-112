# empty list
print("Two standard ways to create an empty list:")
a = []
b = list()


print(type(a), len(a), a, id(a))
print(type(b), len(b), b, id(b))
print(a == b)


# list with one element (singleton)
a = ["hello"]
b = [42]


print(type(a), len(a), a)
print(type(b), len(b), b)
print(a == b)


# list with multiple elements
a = [2, 3, 5, 7]
b = list(range(5))
c = ["mixed types", True, 42]

print(type(a), len(a), a)
print(type(b), len(b), b)
print(type(c), len(c), c)


# variable-length list
n = 10
a = [0] * n
b = list(range(n))

print(type(a), len(a), a)
print(type(b), len(b), b)
