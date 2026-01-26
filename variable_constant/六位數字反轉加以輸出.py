"""
檔名：六位數字反轉加以輸出.py
功能：基礎語法練習
學習重點：變數賦值、基本數學運算
"""
n = eval(input('Enter a 6-digit: '))
print(n % 10, end = '')
n1 = n // 10
print(n1 % 10, end = '')
n2 = n1 // 10
print(n2 % 10, end = '')
n3 = n2 // 10
print(n3 % 10, end = '')
n4 = n3 // 10
print(n4 % 10, end = '')
n5 = n4 // 10
print(n5)
