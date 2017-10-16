# In general, you should avoid using global variables.
# You will even lose style points if you use them!
# Still, you need to understand how they work, since others will use them, and there may also be some very few occasions where you should use them, too!


g = 100


def f(x):
    return x + g


print(f(5))
print(f(6))
print(g)
