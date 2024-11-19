# set {}- a type of collection which is immutable and unordered, but Add/Remove OK. No duplicates
# in chatGPT terms- A set in Python is an unordered collection of unique and immutable elements. Sets are useful for mathematical operations like union, intersection, difference, and for efficiently checking membership.

set1= {1, 2, 3, 4, 5} # here we have {} square brackets, but we can also use set() function to create a set

print(set1)

set2 =set([5, 8, 4, 3, 1, 6, 1]) # by using set as a method

print(set2)

# print(dir(set1)) # this will print the methods available with the set

set1.add(6) # to add an item in the set
print(set1)

set2.remove(1)
print(set2)

# we have pop(), and clear() method with it

# Remember: the sets are used mostly for mathematical operations, so it has methods or operations like union, intersection, etc.
