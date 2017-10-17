# Ragged
# 2d lists do not have to be rectangular
a = [[1, 2, 3],
     [4, 5],
     [6],
     [7, 8, 9, 10]]


rows = len(a)
for row in range(rows):
    cols = len(a[row]) # now cols depends on each row
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(a[row][col], " ", end="")
    print()
