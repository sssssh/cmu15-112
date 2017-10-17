# 1 input, str, len
name = input("Enter your name: ")
print("Hi, " + name + ". Your name has " + str(len(name)) + " letters!")


# 2 chr, ord
print(ord("A"))  # 65
print(chr(65))   # "A"
print(chr(ord("A") + 1))  # ?


# 3 eval
# eval() works but you should not use it!
s = "(3**2 + 4**2)**0.5"
print(eval(s))

# why not? Well...
s = "reformatMyHardDrive()"
print(eval(s))  # no such function!  But what if there was?
