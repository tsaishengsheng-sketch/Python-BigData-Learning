"""
檔名：zero_checker.py
功能：邏輯判斷練習
學習重點：條件分歧、布林邏輯運算
"""
a = eval(input('Enter a number ; '))
if a > 0:
    print('%d is greater than 0. '%(a))
elif a < 0:
    print('%d is less than 0. '%(a))
else:
    print('%d is equal to 0. '%(a))
print('Over')