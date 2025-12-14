# mutability & immutability
# lists are mutable
# tuples and strings are not mutable

s1 = "Python is Fun"
s2 = s1.replace("Python", "JavaScript")
print(s1) # as you can see the first string (s1) did not change hence this proves that strings are immutable
print(s2)
print()

l1 = ["Mango", "orange", "apple"]
# print(id(l1))
# l1.append("Pineapple") # adds banana in the list
# print(l1) # hence mutable
# print(id(l1)) # as you can see that th id of l1 remains same this proves that l1 is not changed even afet adding a new item in it

l1[-1] = "Pineapple" # this way we can replace the value of the specified index with new value that you want
print(l1)
# you cannot do this all if l1 was a tuple or a string, it will give an error

print()

