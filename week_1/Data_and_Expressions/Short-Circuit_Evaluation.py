def yes():
    return True


def no():
    return False


def crash():
    return 1/0  # crashes!


print(no() and crash())
print(crash() and no())
print(yes() and crash())


print(yes() or crash())
print(crash() or yes())
print(no() or crash())