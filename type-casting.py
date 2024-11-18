# we are going to check the methods or functions by which we can do type- casting possible

# first the list of functions available for type casting is -> int(), str(), float(), bool()

# a record of an employee and have to do some operations

emp_name= input("Enter your name: ")
emp_age= int(input("Enter your age: ")) # type-casting of the string to integer
emp_height= float(input("Enter your height: ")) # type-casting of the string to float
emp_married= int(input("Are you married: (type 1 for true and 0 for false) ")) # type-casting of the string to integer, so that we can later on perform for boolean after checking the inserted valur is either 1 or 0

if (emp_married == 1 or emp_married == 0): 
    emp_married = bool(emp_married)
else:
    print("Invalid input for marital status. Exiting program.")
    exit()


#print employee details

print(f"Name of the employee: {emp_name}")
print(f"Age of the employee: {emp_age}")
print(f"Height of the employee: {emp_height}")

if emp_married:
    print(f"{emp_name} is married, so eligible for family benefits")
else:
    print(f"{emp_name} is not married, so not eligible for family benefits")