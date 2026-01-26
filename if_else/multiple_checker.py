"""
檔名：multiple_checker.py
功能：邏輯判斷練習
學習重點：條件分歧、布林邏輯運算
"""
import random
num = random.randint(1, 1000)
if num % 3 == 0:
    print('%d is 3-multiple'%(num))
elif num % 4 == 0:
    print('%d is 4-multiple'%(num))
elif num % 7 == 0:
    print('%d is 7-multiple'%(num))
if (num %3 !=0 and  num %4 != 0 and num %7 != 0):
    print('%d is not 3 or 4 or 7 multiple'%(num))