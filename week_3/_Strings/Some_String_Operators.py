# 1 String + and *
print("abc" + "def")
print("abc" * 3)
print("abc" + 3)  # error


# 2 the in operator
print("ring" in "strings")
print("wow" in "amazing!")
print("Yes" in "yes!")
print("" in "No way!")


# 3 string indexing and slicing
# 3.1 indexing a single character
s1 = "abcdefgh"
print(s1)
print(s1[0])
print(s1[1])
print(s1[2])

print("-----------")
print(s1[len(s1)-1])
print(s1[len(s1)])  # crashes (string index out of range)


# 3.2 negative indexes
s2 = "abcdefgh"
print(s2)
print(s2[-1])
print(s2[-2])


# 3.3 slicing a range of characters
s3 = "abcdefgh"
print(s3)
print(s3[0:3])
print(s3[1:3])
print("-----------")
print(s3[2:3])
print(s3[3:3])


# 3.4 slicing with default parameters
s4 = "abcdefgh"
print(s4)
print(s4[3:])
print(s4[:3])
print(s4[:])


# 3.4 slicing with a step parameter
print("This is not as common, but perfectly ok.")
s5 = "abcdefgh"
print(s5)
print(s5[1:7:2])
print(s5[1:7:3])


# 3.6 reversing a string
s6 = "abcdefgh"

print("This works, but is confusing:")
print(s6[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s6)))

print("Best way: write your own reverseString() function:")


def reverseString(s):
    return s[::-1]


print(reverseString(s6))  # crystal clear!
