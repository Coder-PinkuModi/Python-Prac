# compound interest calculator

# formula A= P(1 + r/n)^(t)

# A= final amount
# P= principal amount
# r= rate of interest
# n= number of times interest applied per time period
# t= number of time periods elapsed

principle= 0
rate= 0
numberofTimes= -1
time= -1

principle = float(input("Enter the principal amount: "))
while principle <= 0:
    print("Please enter a positive number greater than zero")
    principle = float(input("Enter the principal amount: "))
    
rate = float(input("Enter the rate of interest: "))
while rate <= 0:
    print("Please enter a positive number greater than zero")
    rate = float(input("Enter the rate of interest: "))
    
numberOfTimes = int(input("Enter the number of times interest applied per time period: "))
while not numberofTimes < 0:
    print("Please enter a positive number greater than zero")
    numberofTimes = int(input("Enter the number of times interest applied per time period: "))
    
time = int(input("Enter the number of time periods elapsed: "))
while not time < 0:
    print("Please enter a positive number greater than zero")
    time= int(input("Enter a period of time in years"))

amount = principle * (1 + (rate / numberofTimes )) ** (time)

print(f"The compound interest is {amount}")