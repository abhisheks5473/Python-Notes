'''
student1 = {'math': 80.5, 'eng': 76, 'phy': 89.0}

# fetch marks of phy
# method-1
print(student1['phy'])
# method-2
print(student1.get('phy'))
print(student1.get('chem')) # if a key is not present then it will show None
'''

"""
emp1 = {'id': 1001, 'name': 'John', 'salary': 10000}

# how to set a default value for a key which is not present in the dict
print(emp1.get('id', 9876543210))

# membership operator => in, not in
print(1001 in emp1) # will give False
print('name' in emp1)# will give True
# membership operator works only on keys not values
"""
"""
sem1_marks = {'maths': 78.5, 'eng': 71.0, 'phy': 86.5}
sem2_marks = {'chem': 81.5, 'bio': 90.5, 'phy': 95}

# updating
sem1_marks.update(sem2_marks) # updates marks of sem1 and add the missing subjects and marks that are mot in sem1 but are in sem2
print(sem1_marks)

# pop() - remove the key and the value associated with the mentioned key
sem1_marks.pop('phy') # this step is necessary you cannot do print(sem1_marks.pop('phy'))
print(sem1_marks)
"""
"""
# keys cannot be duplicated in dict
groceries = {'milk': 60, 'biscuits': 20, 'rice': 90, 'milk': 30}
print(groceries) # this will not give an error, but it will not print milk = 60 instead it will print milk = 30 because python reads the dict from left to right and takes the most recent value which in this case is 30
"""



d1 = {"Sunny": 6}
print(d1)

# things allowed as keys
# not allowed - list, set, dict => mutable datatypes
# allowed keys - str, int, float, bool, tuple => immutable datatypes

# keys can only be immutable data types
# values can be any datatype


student1 = {'id': 1001, 'name': 'John', 'marks': [89.5, 71.5, 81.0]}
print(student1['marks'][1]) # this fetches the element in index 1 of the value of 'marks'

student2 = {'id': 1001, 'name': 'John', 'marks': {'eng': 89.5,'math': 71.5,'phy': 81.0}}
print(student2['marks']['eng'])

# fetch all the keys?
# .keys()
print(student2.keys()), print(type(student2.keys()))

# fetch all values?
# .value()
print(student2.values()), print(type(student2.values()))

# fetch all pairs of (key: value)
print(student2.items()), print(type(student2.items()))
