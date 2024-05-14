# Lauren Uslick
# P3LAB
#  3/21/2024
#  9.18 LAB: Exact change

input_val = int(input("Enter a coin amont to convert to quarters, dimes, nickels, and pennies: "))
##input_val = int(input())

if (input_val <= 0):
    print("No change")
    
num_dollars = input_val // 100
input_val= input_val % 100

num_quarters = input_val // 25
input_val= input_val % 25

num_dimes = input_val // 10
input_val= input_val % 10

num_nickels = input_val // 5
input_val= input_val % 5

num_pennies = input_val

# print out the values for zybooks

if (num_dollars > 0):
    print(num_dollars, end='')
    if(num_dollars == 1):
       print(" Dollar")
    else:
        print(" Dollars")
if (num_quarters > 0):
    print(num_quarters, end='')
    if(num_quarters == 1):
       print(" Quarter")
    else:
        print(" Quarters")
if (num_dimes > 0):
    print(num_dimes, end='')
    if(num_dimes == 1):
       print(" Dime")
    else:
        print(" Dimes")
if (num_nickels> 0):
    print(num_nickels, end='')
    if(num_nickels == 1):
       print(" Nickel")
    else:
        print(" Nickels")        
if (num_pennies > 0):
    print(num_pennies, end='')
    if(num_pennies == 1):
       print(" Penny")
    else:
        print(" Pennies")




##print(num_dollars)
##print(num_quarters)
##print(num_dimes)
##print(num_nickels)
##print(num_pennies)

    
##input_val = input_val - num_dollars *100
