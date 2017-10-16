def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    elif (x == 1):
        print("D", end="")
    else:
        print("E", end="")
        if (x == 2):
            print("F", end="")
        else:
            print("G", end="")
    print("H")


f(0)
f(1)
f(2)
f(3)


def numberOfRoots(a, b, c):
    # Returns number of roots (zeros) of y = a*x**2 + b*x + c
    d = b**2 - 4*a*c
    if (d > 0):
        return 2
    elif (d == 0):
        return 1
    else:
        return 0


print("y = 4*x**2 + 5*x + 1 has", numberOfRoots(4,5,1), "root(s).")
print("y = 4*x**2 + 4*x + 1 has", numberOfRoots(4,4,1), "root(s).")
print("y = 4*x**2 + 3*x + 1 has", numberOfRoots(4,3,1), "root(s).")


def getGrade(score):
    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    else:
        grade = "F"
    return grade


print("103 -->", getGrade(103))
print(" 88 -->", getGrade(88))
print(" 70 -->", getGrade(70))
print(" 61 -->", getGrade(61))
print(" 22 -->", getGrade(22))
