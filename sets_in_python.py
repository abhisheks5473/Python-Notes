# Sets are non-sequential collection of items
# comma separated elements enclosed within {}
# python sets are very similar to mathematics sets



set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

# You cannot do indexing in set, it will give an error
# You cannot do slicing in set, it wll give an error

# Length of the set
print(len(set1))

# sets do not allow duplicate elements

l1 = [10, 2.5, 10, 30, 10] # list
print(l1, type(l1))
s1 = {10, 2.5, 10, 30, 10}
print(s1, type(s1)) # this will print {10, 2.5, 30} so this means that it will remove all the duplicate elements
print(len(s1)) # this will give 3
