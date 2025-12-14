# Slicing of lists
L1 = [3, 8, 1, 0, 4, 9, 7, 3, 6]
print(L1[1:6:1])
print(L1[2:7:2])

# concatenation of lists
L1 = [1, 7, 2]
L2 = [0, 5]
print(L1 + L2)
print(L2 + L1)

# Repetition of lists
L1 = [1, 7, 2]
L2 = [0, 5]
# *
print(L2 * 3)

# append()
# adds an item to the end of the list [only one item]

fruits = ["Mango", "Apple", "Orange"]
print(fruits)

# Syntax: list.append(item)
fruits.append("Banana")
print(fruits)

# print(fruits.append('banana')) # this will not work as append operation add the banana to the list but does not give it back to print function in the same line code and hence you have to use two lines of code as shown above

# insert
# adds an element before the specified index
# syntax: list.insert(index, item)
fruits.insert(2, "kiwi")
print(fruits)


# extend
# extends the list by appending elements from the iterable (like another list) to the end.
fruits = ["Apple", "Mango", "Orange"]
print(fruits)
fruits.extend(["Banana", "Grapes"])
print(fruits)


# remove()
# Removes the first occurrence of the specified value.

fruits = ["Apple", "Mango", "Orange"]
print(fruits)

fruits.remove("Mango")
print(fruits)
# Initial Output: ['Apple', 'Mango', 'Orange']
# Final Output:


# pop()
# pop function removes the item at the specified index and negative index can also be used
fruits = ["Apple", "Mango", "Orange", "Mango"]
print(fruits)
fruits.pop(2) #is () is left empty then it will delete the last item on the list
print(fruits)


###################
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days_of_week)

# reverse()
days_of_week.reverse()

print(days_of_week)

###########
nums = [4, 9, 0, 1, 2, 8]
print(nums)

# sort() # sorts the integer in ascending order
nums.sort() # or you can type nums.sort(reverse=False)
print("Sorted list:", nums)

nums.sort(reverse=True) # do this is you want to do a descending list
print("Sorted list:", nums)


#############
# count() # counts how many times is the specified item occurring
numbers = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(numbers.count(0))



#eg
# count()
numbers = [0, 1, 3, 4, 1, 0, 5, 0, 0, 3, 0]
print(f"The list is: {numbers}")
item_to_count = int(input("Enter the number to be counted from the above list: "))
c = numbers.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c}")
# if the number that the user has input is not there in the list then the resultant count will be 0


##########
# in
language = ["Python", "Java", "C++", "Python"]
print("Python" in language) # gives True or False as result # 'not in' is the reverse of 'in'





