#List inside a list
L1 = [5, 1.5, "Python", True, None, [1, 2, 3], 10]
print(len(L1))
print(L1[-2])
print(L1[-2][0]) # this is to fetch the item inside the list which is already inside a list


L2 = [[1, 2], [3, 4], [5, 6, [0, 1]]] # you can create any number of nested list
print(L2[-1][2][0]) # this is to fetch the item inside the list which is already inside a list which is already inside a list
