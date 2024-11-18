# just use-> print(help(str)) to know some of the methods of string.

# haha! i was joking, why to practice much when you already know strings thing + vscode already shows you mych of the methods justgive it a string and then use dot immediate after that

# let's do rather an excercise , that is validate a user innput username
# which have some rules:-
# 1. user name should not contain more than 12 characters
# 2. user name should not contain any spaces
# 3. user name should not contain any number
# 4. user name should not have any upper-case letter

user_name = input("Enter a user name: ")

if not user_name.find(" ") == -1:
    print("User name should not contain spaces")
elif len(user_name) > 12:
    print("User name should not contain more than 12 characters")
elif user_name.isalpha() == False:
    print("User name should not contain numbers or special characters")
elif not user_name.islower() == -1:
    print("User name should not contain upper-case letters")
else:
    print("User name is valid") 