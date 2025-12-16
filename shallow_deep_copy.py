import copy

l1 = [1, 2.5, [10, 20, 30], 'Python']

'''
# shallow copy
l2 = copy.copy(l1)

# print(l2)
# print(id(l1))
# print(id(l2))

l1[0] = 5     # this will not change the value to 5
l1[2][0] = 50 # this will change the value to 50

print(f"l1 -> {l1}", id(l1))
print(f"l2 -> {l2}", id(l2))
'''

# deepcopy

l3 = copy.deepcopy(l1)

l1[0] = 5
l1[2][0] = 50

print(f"l1 -> {l1}", id(l1))
print(f"l3 -> {l3}", id(l3))


# so in case of shallow copy the id of l1 and l2 are different but the id of items in it are same
# and in case of deep copy the id of l1 ans l3 are different and the id of items in it are also different



import copy

d1 = {'id': 1111, 'name': 'John', 'marks': {'eng': 71.5, 'maths': 91.5, 'bio': 80.0}}
'''
# copy
d2 = copy.copy(d1)

d1['name'] = "Dan"
d1['marks']['eng'] = 75.5
# l1[2][0] = 50

print(f"d1 -> {d1}", id(d1))
print(f"d2 -> {d2}", id(d2)) # this will cause no change to name but will cause the change in eng marks as the copy is shallow
'''

# deepcopy
d2 = copy.deepcopy(d1)

d1['name'] = "Dan"
d1['marks']['eng'] = 75.5
# l1[2][0] = 50

print(f"d1 -> {d1}", id(d1))
print(f"d2 -> {d2}", id(d2)) # this will cause no change anywhere as the copy is deep

