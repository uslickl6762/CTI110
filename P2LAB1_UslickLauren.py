 # Lauren Uslick
 # 2/27/2024
 #P2LAB1 
 # Calculate the diameter, circumference, and area of a circle.
import math

pi= math.pi

rad = float(input('What is the radius of the circle? '))
print()
dia=rad*2
print(f"The diameter of the circle is {dia:.1f}")
print()
cir=2*math.pi*rad
print(f"The circumference of the circle is {cir:.2f}")
print()
area=pi*math.pow(rad,2)
print(f"The  area of the circle is {area:.3f}")



