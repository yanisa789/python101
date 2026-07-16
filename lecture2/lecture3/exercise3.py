hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hours pay rate: "))
if hours <= 40:
    gross_pay = hours * pay_rate
else:
    regular_pay = 40 * pay_rate
    overtime_pay = (hours - 40) * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
    print(f"Gross pay: ${gross_pay:.2f}")
    