def mod(a, b):
    return a - (a // b) * b


print(41 % 14, mod(41, 14))
print(14 % 41, mod(14, 41))
print(-32 % 9, mod(-32, 9))
print(32 % -9, mod(32, -9))
