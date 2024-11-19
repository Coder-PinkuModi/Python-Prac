# tuple () - A tuple is an ordered, immutable collection of elements in Python. They are similar to lists but have some key differences, such as immutability, which makes them useful for fixed data that shouldn't change.

# Key Features of Tuples
# Ordered: Tuples maintain the order of elements.
# Immutable: Once created, the elements of a tuple cannot be changed, added, or removed.
# Allow Duplicates: Tuples can contain duplicate elements.
# Heterogeneous: Tuples can store elements of different data types.
# just a tuple making and printing is enough right now, and with practice we will get to know more about them and their methods

# Remember: Tuple are faster than list

tuple1 = ("Pinku", "Modi", "Star")
print(tuple1)
print(type(tuple1))

empty_tuple = ()
print(empty_tuple)

# using tuple constructor 
tuple2= tuple(["Hey User", "Welcome to python world"])
print(tuple2)

# it's particular element can be accessed by indexing
print(tuple1[0])

print(tuple1[1:])

print(tuple1[::-1]) #reverse printing

print(tuple1.count("Pinku"))