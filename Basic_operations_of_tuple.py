"""
concatenation, repetition, membership
count, index
min, max, sum
"""
student_detail1 = (1001, 'Jhon')
student_detail2 = (78.5, 91.0, 83.5, 79.5)

# concatenation (+)
student_details = student_detail1 + student_detail2
print(student_details)
print()

# repetition (*)
t1 = ("Class 5", 5000)
print(t1 * 3)
print()

# membership operation (in, not in) checks weather the item is present or not in the string, list, or tuple
student_detail2 = (78.5, 91.0, 83.5, 79.5)
print(91 in student_detail2) # if a float has .0 ending and the part that you asked is the part before the  decimal the answer will be true
print(99 not in student_detail2)
print()

# count
x= (10, 4, 1, 9, 0, 3, 1)
#tuple.count(element)
print(x.count(1))
print()

# index
x= (10, 4, 1, 9, 0, 3, 1)
#tuple.index(element)
print(x.index(4)) # wht is index of 4 in tuple x
print()

# min, max, sum
numbers = (10, 4, -1, 20, 5.5, 7, 1)

# Smallest number in the list
# min()
print(f"Smallest number: {min(numbers)}")

# Biggest number in the list
# max()
print(f"Biggest number: {max(numbers)}")

# Total of the numbers in the list
# sum()
print(f"Total: {sum(numbers)}")



