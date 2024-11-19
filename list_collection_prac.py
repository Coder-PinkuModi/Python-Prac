# here there are sort of practice or experiment upon the array or which can be also called list in python.

# list- the array type collections of same items of same data types, which mutable in nature. It is enclosed within [] square brackets

clothes = ["Jeans", "T-shirt", "Shirt", "Trousers", "Joggers"]

# print(clothes) # to print the whole list

# to know the methods available with the list, we can take help of the command "print(help(collections))"
# print(help(clothes))
# one more is there just print-> print(dir(list_variable)), here list_variable is the variable name of the list, i.e. clothes

# print(len(clothes)) # to know the length of the list
# print("Jeans" in clothes) # to check whether the item is present in the list or not 
# print("Pyjama" in clothes) 

# practicing some of the methods available in list

# clothes.append("Pyjama") # to add an item at the end of the list
# clothes.sort() # to sort the list

# if you want to sort it in reverse way then , first sort and then use reverse method to reverse the list
# clothes.sort(reverse=True)

# to remove an item from the list
# clothes.remove("T-shirt")

# clothes.insert(3, "Pants") # to insert an item in the list in the given postition we need insert method

# clothes[1] = "Shirt" # one can also overwrite the item of the list with it's index

# clothes.pop() # to remove the last item of the list
# clothes.pop(3) # to remove the item at the given index

# print(clothes.index("T-shirt")) # we can also get the index of the particular item in the list 

print(clothes)