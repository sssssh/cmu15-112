print(0.1 + 0.1 == 0.2)  # True, but...
print(0.1 + 0.1 + 0.1 == 0.3)  # Flase!
print(0.1 + 0.1 + 0.1)  # prints 0.30000000000000004
print((0.1 + 0.1 + 0.1) - 0.3)  # prints 5.55111512313e-17 tiny, but non-zero!
