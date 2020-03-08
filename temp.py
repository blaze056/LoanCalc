from calc import calc

loan_amount = 100000
rate = 5
loan_period = 36
table = calc(loan_amount,rate,loan_period)
#print(table)
for item in table:
    print(item)