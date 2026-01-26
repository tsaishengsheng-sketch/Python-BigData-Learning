"""
檔名：月支付額與總支付額.py
功能：基礎語法練習
學習重點：變數賦值、基本數學運算
"""
rate = eval(input('Annual rate: '))
amount = eval(input('Enter Loan amount: '))
year = eval(input('Enter number of years: '))

monthlyInterestRate = rate / 1200
monthlyPay = amount * monthlyInterestRate / (1 - (1 / pow(1 + monthlyInterestRate, year * 12)))

totalPay = monthlyPay * year * 12
print('Monthly payment: %.2f'%(monthlyPay))
print('Total payment: %.2f'%(totalPay)) 