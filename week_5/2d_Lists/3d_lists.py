# 2d lists do not really exist in Python.
# They are just lists that happen to contain other lists as elements.
# And so this can be done for "3d lists", or even "4d" or higher-dimensional lists.
# And these can also be non-rectangular, of course!

a = [[[1, 2],
      [3, 4]],
     [[5, 6, 7],
      [8, 9]],
     [[10]]]

for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print("a[%d][%d][%d] = %d" % (i, j, k, a[i][j][k]))
