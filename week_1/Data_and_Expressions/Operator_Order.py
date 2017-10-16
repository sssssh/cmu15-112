print("Precedence:")
print(2 + 3 * 4)
print(5 + 4 % 3)  # % has same precedence as *, /, and //
print(2 ** 3 * 4)  # ** has higher precedence than *, /, //, and %


print()


print("Associativity:")
print(5 - 4 - 3)  # - associates left-to-right
print(4 ** 3 ** 2)  # ** associates right-to-left
