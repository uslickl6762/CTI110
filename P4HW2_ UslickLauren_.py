# Lauren Uslick
# 4/18/2024
# P4HW2
# Wage calculator looped


totOvertime = 0
totRegPay = 0
totGrossPay = 0
count = 0 

em = input("Enter employee's name or" + ' "Done" ' + "to terminate: ")
while em != "Done":
    
    hrs = float(input("How many hours did " + em + " work?: "))
    rate = float(input("What is " + em + "'s pay rate?: "))
    print()
    print("Employee name:  ", em)
    print()
    hw = "Hours Worked"
    pr = 'Pay Rate'
    ov = 'OverTime'
    op = 'OverTime Pay'
    rp = 'RegHour Pay'
    gp = 'Gross Pay'
    print(f'{hw:<15}{pr:<12}{ov:<12}{op:<20}{rp:<20}{gp:<20}')
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

    totOvertime = totOvertime + ovt_pay 
    totRegPay = totRegPay + reg_pay 
    totGrossPay = totGrossPay + gross_pay
    count = count + 1
    print(f'{hrs:<15.1f}{rate:<12.1f}{ovt_hours:<12.1f}{ovt_pay:<19.2f} ${reg_pay:<19.2f} ${gross_pay:<15.2f}')
    print()
    print()  
    em = input("Enter employee's name or" + ' "Done" ' + "to terminate: ")
    
print()
print("Total amount of employees entered:", count)
print(f'Total amount paid for overtime: ${totOvertime:.2f}')
print(f'Total amount paid for regular hours: ${totRegPay:.2f}')
print(f'Total amount paid in gross: ${totGrossPay:.2f}')
