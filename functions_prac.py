# Here we can see a function and there aspects, with argument, default argument, keyword and aribitrary

# remember a function can be defined, Syntax: def function_name(parameters):

# well we know that there are ways to take parameters in python like: positional argument, default argument, keyword argument and arbitrary argument

# now let's call a function with positional argument

def add(a, b):
    return a+b

# now the positional parameters means we will call the function ana the order of the parameters will matter and have to be the same as of the parameters in the function

print(add(2, 3)) # here we don't have to provide any name of the argument like a=2, b=3 as keyword arguments


# now let's see what is Keyword arguments mean,

def intro(title, first_name, last_name, age):
    print(f"{title} {first_name} {last_name} is {age} years old")
    
# intro("Mr.", "Pinku", "Modi", 20) # this is the way of passing argument as a positional argument 

intro(title="Mr.", first_name ="Pinku", last_name="Modi", age= 20) # keyword argument means, we will assign the argument inside the keyword matches the parameters in the function

# NOTE:- in positional argument order matters but in keyword argument order does't matter, and we can also pass it as intro(first_name ="Pinku", age= 20, last_name="Modi", title="Mr.")


# Default argument= sometimes there is possiblity that we don't provide any value for some argument or any user forgets that there can be a default argument that means the argument itself will contain the default value
# this can be acieved by, at the time of function making we can pass a value to the parameter like,
# def name(name="Guest"):
    # return name
# now calling - name() # here user either forget to put any name while calling the function or he/she didn't provided their name so it will take the default value


# about arbitrary argument:- this are ways of taking multiple arguments in a function without asking for all that arguments at the time of function definition. Well, in this we can give multiple arguments, tuples ,list, dictionaries but that can be done by SYNTAX:- *args and **kwargs repectively

