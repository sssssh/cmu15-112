def letterCounts(s):
    counts = [0] * 26
    for ch in s.upper():
        if ((ch >= "A") and (ch <= "Z")):
            counts[ord(ch) - ord("A")] += 1
    return counts


def isAnagram(s1, s2):
    # First approach: same #'s of each letter
    return (letterCounts(s1) == letterCounts(s2))


def isAnagram(s1, s2):
    # Second approach: sorted strings must match!
    return sorted(list(s1.upper())) == sorted(list(s2.upper()))


def testIsAnagram():
    print("Testing isAnagram()...", end="")
    assert(isAnagram("", "") == True)
    assert(isAnagram("abCdabCd", "abcdabcd") == True)
    assert(isAnagram("abcdaBcD", "AAbbcddc") == True)
    assert(isAnagram("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")


testIsAnagram()
