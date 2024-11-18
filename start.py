#This is my first program, and by giging '#' we can comment our code

print("I am Pinku Modi, will be the best coder in the world and surpass all the coder")
print("I am learning Python")

# variable-> string,intger, float, boolean we are going to know todar

# string
name = "Pinku Modi"
print(name)
print(type(name)) # this "type" keyword will return the type of the variable

# now as we know the string literal used in js-> bu using backticks `` , here in python it is same with name f-string, here wb giving f"{variable_name}"
#like in the below line
print(f"My name is {name}")

#integer
age = 20
print(age)
print(type(age))

#float
height = 5.7
print(height)
print(type(height))

#boolean
is_adult = True
print(is_adult)
print(type(is_adult))

# -> let's use the if- statement for boolean value
if is_adult:
    print("You are an adult")
else:
    print("You are not an adult")
    
# let's make a whole operation with the variables and if - statement

# a record of a student without objects, using simple variables

print("Below this a record of a student, and checked if he or she is allowed in halloween party")

st_name = "Raghuvir"
st_age = 20
st_class = "10th"

if st_age >= 18:
    print(f"{st_name} is allowed in halloween party")
else:
    print(f"{st_name} not allowed")