# Lauren Uslick
# 3/5/2024
#P2HW1
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")
print()
budget = float(input('Enter Budget: '))
print()
lname = input("Enter your travel destination: ")
print()
gas = float(input('How much do you think you will spend on gas?: '))
print()
hotel = float(input('Approximately, how much will you need for accomodation/hotel?: '))
print()
food = float(input('Last, how much will you need for food?: '))
print()
print('-'*12 + 'Travel Expenses' + 12*'-')
print('Location:'.ljust(20) + lname)
print('Initial Budget:'.ljust(20) + '$' + f'{budget:.2f}')
print('Fuel:'.ljust(20) + '$' + f'{gas:.2f}')
print('Accomodation:'.ljust(20) + '$' + f'{hotel:.2f}')
print('Food:'.ljust(20) + '$' + f'{food:.2f}')
print('-'*39)


print()
balance=budget-gas-hotel-food
print("Remaining Balance:".ljust(20) + '$' + f'{balance:.2f}')
