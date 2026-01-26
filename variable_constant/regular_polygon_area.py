"""
檔名：計算正n邊形面積.py
功能：基礎語法練習
學習重點：變數賦值、基本數學運算
"""
import math
num = eval(input('How many sides: '))
side = eval(input('Enter Length of a side: '))
area = (num * side ** 2) / (4 * math.tan(math.pi/num))
print('Area of n-side is %.2f'%(area))
