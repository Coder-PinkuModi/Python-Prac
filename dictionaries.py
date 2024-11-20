# dictionary = it is a collection of {key:value} pairs, just like objects in js

# syntax: dictionary_name = {key1:value1, key2:value2, key3:value3}

# we can also use dict() function to create a dictionary

my_dict = {
    "name": "Pinku Modi",
    "age": 20,
    "height": 5.7,
    "is_adult": True
}

# now there are some methods avaialable with the dictionary

# print(dir(my_dict)) # this will print the methods available with the dictionary

print(my_dict["name"]) # to print the value of the key

my_dict.update({"rank": 1220.561485}) # this can be used for both overriding a key and adding new key

print(my_dict)

my_dict.popitem() # this will remove the last key

my_dict.pop("is_adult")  # this will remove the key

# my_dict.clear() # this will remove all the keys

my_dict.get("name") # this will return the value of the key

my_dict.keys() # this will return the keys of the dictionary

my_dict.values() # this will return the values of the dictionary

my_dict.items() # this will return the items of the dictionary

print(my_dict)