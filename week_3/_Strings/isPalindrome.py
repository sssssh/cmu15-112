# There are many ways to write isPalindrome(s)
# here are several. which way is best?


def reverseString(s):
    return s[::-1]


def isPalindrome1(s):
    return s == reverseString(s)


def isPalindrome2(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True


def isPalindrome3(s):
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            return False
    return True


def isPalindrome4(s):
    while len(s) > 1:
        if s[0] != s[-1]:
            return False
        s = s[1:-1]
    return True


print(isPalindrome1("abcba"), isPalindrome1("abca"))
print(isPalindrome2("abcba"), isPalindrome2("abca"))
print(isPalindrome3("abcba"), isPalindrome3("abca"))
print(isPalindrome4("abcba"), isPalindrome4("abca"))
