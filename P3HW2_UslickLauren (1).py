# Lauren Uslick
# P3HW2
# 3/28/2024
# Wage calculator

em = input("Enter employee's name: ")
hrs = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))
print('-'*37)

print("Employee name:  ", em)
print()
hw = "Hours Worked"
pr = 'Pay Rate'
ov = 'OverTime'
op = 'OverTime Pay'
rp = 'RegHour Pay'
gp = 'Gross Pay'

print(f'{hw:<15}{pr:<12}{ov:<12}{op:<20}{rp:<20}{gp:<20}')
##print(hw.ljust(15) + pr.ljust(12) + ov.ljust(12) + op.ljust(20) + rp.ljust(20) + gp)
##print("Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay")
print('-'*98)

ovt_hours = 0
ovt_pay = 0
if hrs > 40:
    reg_pay = rate * 40
    ovt_hours = hrs - 40
    ovt_rate = 1.5 * rate
    ovt_pay = ovt_hours * ovt_rate
    gross_pay = ovt_pay + reg_pay
else:
    reg_pay = rate * hrs
    gross_pay = ovt_pay + reg_pay

print(f'{hrs:<15.1f}{rate:<12.1f}{ovt_hours:<12.1f}{ovt_pay:<19.2f} ${reg_pay:<19.2f} ${gross_pay:<15.2f}')
