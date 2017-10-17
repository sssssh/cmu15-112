# Tuple syntax
t = (1, 2, 3)
print(type(t), len(t), t)


a = [1, 2, 3]
t = tuple(a)
print(type(t), len(t), t)


# Tuples are immutable
t = (1, 2, 3)
print(t[0])

t[0] = 42    # crash!
print(t[0])


# Parallel (tuple) assignment
(x, y) = (1, 2)
print(x)
print(y)

(x, y) = (y, x)
print(x)
print(y)


# Singleton tuple syntax
t = (42)
print(type(t), t*5)  # 10

t = (42,)
print(type(t), t*5)  # (42, 42, 42, 42, 42)
