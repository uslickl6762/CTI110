# Lauren Uslick
# P5Lab
# 4/30/2024
# Simulate a customer using a self-checkout machine

# get random library
import random

# change calculator
def disperse_change(change):
        if change == 0:
                print("No Change Due")

            #Calculate the amount of each coin needed
            #integer division - //

        num_dollars = change // 100
        change = change - (num_dollars * 100)

        num_quarters = change // 25
        change = change - (num_quarters * 25)

        num_dimes = change // 10
        change = change - (num_dimes * 10)

        num_nickles = change // 5
        change = change - (num_nickles *5)

        num_pennies = change // 1

        #Display coins owed

        if num_dollars > 0:
            print(num_dollars,  end=" ")
            if num_dollars == 1:
                print("Dollar")
            else:
                print("Dollars")
                        
        if num_quarters > 0:
            print(num_quarters,  end=" ")
            if num_quarters == 1:
                print("Quarter")
            else:
                print("Quarters")

        if num_dimes > 0:
            print(num_dimes,  end=" ")
            if num_dimes == 1:
                print("Dime")
            else:
                print("Dimes")

        if num_nickles > 0:
            print(num_nickles,  end=" ")
            if num_nickles == 1:
                print("Nickle")
            else:
                print("Nickles")

        if num_pennies > 0:
            print(num_pennies,  end=" ")
            if num_pennies == 1:
                print("Penny")
            else:
                print("Pennies")
  
def main():
        print("Checkout Calculator")
        print()
        # generate a random float w/ 2 decimal places as the amount the customer owes
        amount_owed = round(random.uniform(0.01, 100.00), 2)
        # Display the amount owed
        print(f"You owe ${amount_owed:.2f}")
        print()
        # prompt user to enter a float as the cash they will put in the checkout machine
        amount_paid = float(input("How much cash will you put in the self-checkout? "))
        print()
        # calculate change owed
        change_owed = amount_paid - amount_owed
        # Display the chnage owed
        print(f"Change is: ${change_owed:.2f}")
        print()
        # Convert the float change to integer
        change_owed = round(change_owed*100)
        print()
        # Call the disperse_change function and pass change_owed as the parameter
        disperse_change(change_owed)
        
        
        
main()



    
