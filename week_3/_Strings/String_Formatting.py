# %s - string
breed = "beagle"
print("Dig you see a %s?" % breed)


# %d - integer
dogs = 42
print("There are %d dogs." % dogs)


# %f - float
grade = 87.385
print("Your current grade is %f!" % grade)


# %.[precision]f - float
print("Your current grade is %0.1f!" % grade)


# multiple values
cats = 18
exclamation = "Wow"
print("There are %d dogs and %d cats. %s!!!" % (dogs, cats, exclamation))


# %[minWidth] - right-aligned
print("%10s %10s" % ("dogs", "cats"))
print("%10d %10d" % (dogs, cats))


# %-[minWidth] - left-aligned
print("%-10s %-10s" % ("dogs", "cats"))
print("%-10d %-10d" % (dogs, cats))


# Basic File IO
# Note: As this requires read-write access to your hard drive,
#       this will not run in the browser in Brython.

def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)


contentsToWrite = "This is a test!\nIt is only a test!"
writeFile("foo.txt", contentsToWrite)

contentsRead = readFile("foo.txt")
assert(contentsRead == contentsToWrite)

print("Open the file foo.txt and verify its contents.")
