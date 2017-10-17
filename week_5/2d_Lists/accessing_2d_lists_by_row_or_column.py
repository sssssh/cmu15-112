# 1 accessing a whole row
# alias (not a copy!); cheap (no new list created)
a = [[1, 2, 3], [4, 5, 6]]
row = 1
rowList = a[row]
print(rowList)


# 2 accessing a whole column
# copy (not an alias!); expensive (new list created)
a = [[1, 2, 3], [4, 5, 6]]
col = 1
colList = []
for i in range(len(a)):
    colList += [a[i][col]]
print(colList)


# accessing a whole column with a list comprehension
# still a copy, still expensive, but cheaper and cleaner with a list comprehension!
a = [[1, 2, 3], [4, 5, 6]]
col = 1
colList = [a[i][col] for i in range(len(a))]
print(colList)
