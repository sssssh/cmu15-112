for n in range(200):
    if (n % 3 == 0):
        continue  # skips rest of this pass (rarely a good idea to use "continue")
    elif (n == 8):
        break  # skips rest of entire loop
    print(n, end=" ")


print()
