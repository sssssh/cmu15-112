# 1 you cannot change strings! they are immutable
s = 'abcde'
s[2] = 'z'  # cannot assign into s[i]


# 2 instead, you must create a new string
s = s[:2] + "z" + s[3:]
print(s)
