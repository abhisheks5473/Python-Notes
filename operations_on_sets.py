nums = {1, 3, 2, 0, -1}

# Membership operator - in, not in
print(0 in nums)
print(10 in nums)
print()

# concatenation, repetition are not supported by sets


# conversion between lists, tuples and sets is allowed
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri") # tuple
weekdays = set(weekdays) # converted to set
print(weekdays) # this will not give an ordered pair sat the mentioned tuple or list because sets are non-sequential and will give different order of elements every time
print()


# Are sets mutable or immutable? they are mutable.
set1 = {2, 0, -1}
print(set1)

# add()
set1.add(5)
print(set1)

# remove()
set1.remove(0)
print(set1)
# this function will give an error if you do not have the specified element in the set

# discard()
set1.discard(0)
print(set1)
# this will remove the element specified if present otherwise it will not give an error








# some imp operations

student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths","CS"}
# common subjects of student1 and student2 - intersection
common_subjects = student1.intersection(student2, student3) # it can also be written as student1 & student2
print(common_subjects) # if the is no common subjects then the result will be 'set()'


#all subjects of student1 and student2
all_subjects = student1.union(student2, student3)  # instead of .union you can use '|' # use a ',' and rest of the other students if there are multiple students
print(all_subjects)
print(all_subjects)


#
days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}

# difference of sets
weekdays = days - weekends # or you can type days.difference(weekends) # elements of days which are NOT in weekends
print(weekdays)

# (days - weekends) is not equal to (weekends - days)
