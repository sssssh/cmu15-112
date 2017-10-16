# A broken test function
def onesDigit(n):
    return n % 10


def testOnesDigit():
    print("Testing oneDigit()...", end="")
    assert(onesDigit(5) == 5)
    assert(onesDigit(123) == 3)
    assert(onesDigit(100) == 0)
    assert(onesDigit(999) == 9)
    print("Passed!")


testOnesDigit()


def testOnesDigit():
    print("Testing oneDigit()...", end="")
    assert(onesDigit(5) == 5)
    assert(onesDigit(123) == 3)
    assert(onesDigit(100) == 0)
    assert(onesDigit(999) == 9)
    assert(onesDigit(-123) == 3)  # Added this test
    print("Passed!")


testOnesDigit()
