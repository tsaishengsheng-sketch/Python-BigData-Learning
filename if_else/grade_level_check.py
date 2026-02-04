"""
檔名：grade_level_check.py
功能：邏輯判斷練習
學習重點：條件分歧、布林邏輯運算
"""
score = eval(input('Enter your scare: '))
if score >= 80:
    print('Your GPA is A.')
elif score >= 70:
    print('Your GPA is B.')
elif score >= 60:
    print('Your GPA is C.')
elif score >= 50:
    print('Your GPA is D.')
else:
    print('Your GPA is F.')