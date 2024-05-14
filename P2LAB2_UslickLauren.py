# Lauren Uslick
# 2/29/2024
# P2LAB2
#  Write code that uses a dictionary to store user input and displays output to the user

car_dict = {
  "Camaro": 18.21,
  "Prius": 52.36,
  "Model S": 110,
  "Silverado": 26
}
carlist = car_dict
print("The keys in this dictionary are:")
print(*carlist, sep = ", ")
print()
vehicle = input("Enter a vehicle to see it's mpg: ")
print()
mpg = car_dict[vehicle]
print("The",vehicle,"gets",mpg,"mpg.")
print()
miles = float(input("How many miles will you drive the " + vehicle + "? "))
print()
gallons=miles/mpg
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")


 
