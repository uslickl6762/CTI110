# Lauren Uslick
# P4Lab2
# 4/11/2024
# LAB: Output Range with increment of 5

num1 = int(input())
num2 = int(input())

if num2 < num1:
    print("Second integer can't be less than the first.")
else:
    for i in range(num1, num2 + 1, 5):
        print(f'{str(i)}', end=' ')
    print()
