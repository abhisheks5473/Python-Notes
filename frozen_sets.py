# frozen sets - immutable
fs1 = frozenset({10, "Python", 2.5})
print(fs1 , type(fs1)) # print(fs1) will give the output frozenset({10, 2.5, 'Python'}), as you can see there is a prefix "frozenset"

# you cannot perform any operation on the frozenset which does not change the original set, but if you try to perform such operations then it will give an error
# tou can perform intersection, union, difference of frozen set as they create a separate set and do not disturb the original set
