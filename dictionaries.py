# comma separated key-value pairs enclosed within {}
# {key1:value1, key2:value2, ......}

groceries = {'milk': 60, 'biscuits': 20, 'rice': 90, 'bread': 30}
print(groceries)
print(type(groceries))

# dictionaries are mutable

groceries['milk'] = 70 # you can update the value of 'key' not the key

print(groceries)
print(type(groceries))

# you can fetch the value of a key which is already present in the dictionary
print(groceries['milk'])

# addition of a key in dictionary
groceries['eggs'] = 10 # add new key - value pair ('eggs': 10) to the dictionary (groceries)
print(groceries)

