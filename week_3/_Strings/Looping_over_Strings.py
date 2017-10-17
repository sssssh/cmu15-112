# 1 'for' loop with indexes
s = "abcd"
for i in range(len(s)):
    print(i, s[i])


# 2 'for' loop without indexes
s2 = "abcd"
for c in s2:
    print(c)


# 3 'for' loop with split
names = "fred,wilma,betty,barney"
for name in names.split(","):
    print(name)


# 4 'for' loop with splitlines
quotes = """\
Dijkstra: Simplicity is prerequisite for reliability.
Knuth: If you optimize everything, you will always be unhappy.
Dijkstra: Perfecting oneself is as much unlearning as it is learning.
Knuth: Beware of bugs in the above code; I have only proved it correct, not tried it.
Dijkstra: Computer science is no more about computers than astronomy is about telescopes.
"""
for line in quotes.splitlines():
    if (line.startswith("Knuth")):
        print(line)
