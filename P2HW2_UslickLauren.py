# Lauren Uslick
# 3/5/2024
# P2HW2
# Grade calculator




grade_list= []
grade = float(input('Enter grade for Module 1: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 2: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 3: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 4: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 5: '))
grade_list.append(grade)
grade = float(input('Enter grade for Module 6: '))
grade_list.append(grade)
print()

print('-'*12 + "Results" + 12*'-')
low = min(grade_list)
high = max(grade_list)
sum1 = sum(grade_list)
length = len(grade_list)
average = sum1/length
print('Lowest Grade:'.ljust(20) + f'{low:.2f}') 
print('Highest Grade:'.ljust(20) + f'{high:.2f}') 
print('Sum of Grades:'.ljust(20) + f'{sum1:.2f}') 
print('Average:'.ljust(20) + f'{average:.2f}')
print('-'*40)



