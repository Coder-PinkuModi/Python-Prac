# here we are going to make a stopwatch, where user will be prompted to input the hours, minutes and seconds
# THen the timer will be updated and each time gets printed as we have no other way to do it right now bcoz we haven't done the GUI part yet with python 

import time

print("Hey User, Welcome to the mini software of stopwatch")
choice = input("Type \"start\" to start the timer: ")

if choice.lower() == "start":
    # The program is made in such a way that ones a user start the program he/she will have to be give right input or else either the program quits with error or the loop keeps running forever for each input
    hours = int(input("Enter the hours: "))
    while not 0 <= hours <= 23:
        print("Please enter a valid time in 24-hour format.")
        hours = int(input("Enter the hours: "))
    
    minutes = int(input("Enter the minutes: "))
    while not 0 <= minutes <= 59:
        print("Please enter a valid minute between 0 and 59.")
        minutes = int(input("Enter the minutes: "))
        
    seconds = int(input("Enter the seconds: "))
    while not 0 <= seconds <= 59:
        print("Please enter a valid second between 0 and 59")
        seconds = int(input("Enter the seconds: "))
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        # hours = total_seconds / 3600
        # remainder = total_seconds % 3600 
        # 2-steps written above this line is the line equal to the one line written in below
        hours,remainder = divmod(total_seconds, 3600)
        minutes,remainder = divmod(remainder, 60)
        seconds = remainder
        
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
        total_seconds -= 1
        time.sleep(1)

    print("Time's up🕛")
    
else : 
    print("You typed other than \"start\" and this means to quit the program")
    quit()