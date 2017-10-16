'''
Python Language Reference, Ch 7.0 (Compound statements introduction)
- https://docs.python.org/3/reference/compound_stmts.html
Be sure to understand the modified BNF and the syntax it describes!

Python Language Reference, Ch 7.1 (The if statement)
Ditto!
- https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
'''


# if
if (1 < 2):
    print("yes!")
if (5 < 4):
    print("really?")
print("you bet!")


# if-else
if (5 < 4):
    print("really?")
else:
    print("not really!")
print("fascinating!")


# if-elif-...-else
if (5 < 4):
    print "really?"
elif (4 < 3):
    print "curious!"
elif (3 > 2):
    print "perhaps..."
else:
    print "why not?"
print "yippee!"


# A Better Example:
n = int(raw_input("Enter an integer: "))
if (n > 0):
    print n,"is positive"
elif (n == 0):
    print n,"is zero"
else:
    print n,"is negative"


# Aside:  Same example with a nasty bug:
n = raw_input("Enter an integer: ")
if (n > 0):
    print n,"is positive"
elif (n == 0):
    print n,"is zero"
else:
    print n,"is negative"


# Nested "if" statements
if (2 < 1):
    if (3 == 3):
        print "a"
    else:
        print "b"
else:
    if (4 == 4):
        print "c"
    else:
        print "d"


# The "dangling-else" problem
print "first:"
if (2 < 1):
    if (3 == 3):
        print "a"
    else:
        print "b"
        
print "second:"
if (2 < 1):
    if (3 == 3):
        print "c"
else:
        print "d"


# Complex Conditionals and Boolean Logic
age = 42
if ((age >= 6) and (age <= 21)):
    print "student"
elif (not ((age < 6) or (age > 75))):
    print "professional"


# Same logic, after applying DeMorgan's Law:
age = 42
if ((age >= 6) and (age <= 21)):
    print "student"
elif ((age >= 6) and (age <= 75)):
    print "professional"


# Same logic again, sharing a common condition:
age = 42
if (age >= 6):
    if (age <= 21):
        print "student"
    elif (age <= 75):
        print "professional"


# And why we parenthesize...:
print not True and False
print not (True and False)


# Conditional Expressions 
x = 3 if (1 < 2) else 4
print x
x = 5 if (1 > 2) else 6
print x


# A Somewhat Better Example:
p = 5
print "I saw",p,"people" if (p>1) else "person"
p = 1
print "I saw",p,"people" if (p>1) else "person"



