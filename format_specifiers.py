# format specifiers = { value:flags } format a value based on what flags are inserted

# in simpler word a Format specifiers in Python are placeholders used in strings to format values dynamically. They define how a value (like a number, string, or object) should appear when inserted into a string.

# syntax: as per modern pyton we can use it with f-strings

name = "Pinku Modi"
age = 20
rank= 1220.561485
ph_number= 2045698758524

print(f"Hello, {name}! You are {age:^} years old.") # here ^ is for centering the text, there are more like left, right same as center andf their symbol is <, > respectively


print(f"My phone number is {ph_number:+} and my rank is {rank:.3f}") # here the + is for adding + to the ph_number and the .3f is for rounding off the rank to 3 decimal places

# there are more of it, even the ways we can like using .format but with time we will get use to them