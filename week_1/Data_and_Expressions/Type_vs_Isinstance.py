# In general, you should use isinstance(x, T) instead of type(x) == T
# In fact, we will disallow type(x) in labs and hw's


print(type("abc") == str)
print(isinstance("abc", str))


# We'll see better reasons for this when we cover OOP + inheritance later in the course.
# For now, here is one reason: say you wanted to check if a value is any kind of numeber
def isNumber(x):
    return ((type(x) == int) or
            (type(x) == float))


print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))


# But this is cleaner, and works for all kinds of numbers, including complex numbers for example:
import numbers
def isNumber(x):
    return isinstance(x, numbers.Number)  # works for any kind of number


print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))
