"""
檔名：leap_year_check.py
功能：邏輯判斷練習
學習重點：條件分歧、布林邏輯運算
"""
year = eval(input('Enter a year '))
con1 = year % 400 == 0
con2 = year % 4 == 0 
con3 = year % 100 != 0
if con1 or (con2 and con3):
    print('%d is a leap year.'%(year))
else:
    print('%d is a common year.'%(year))