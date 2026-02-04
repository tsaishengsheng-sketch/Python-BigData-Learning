"""
檔名：division_check.py
功能：邏輯判斷練習
學習重點：條件分歧、布林邏輯運算
"""
# 相除不等於0
a = eval (input('Enter a number1: '))
b = eval (input('Enter a number2: '))
if b != 0:
        c = a / b
        print('%.2f /%.2f = %.2f'%(a, b, c))
else:
        print('Divisor con\'t be zero')        
print('Over')

