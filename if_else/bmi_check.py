"""
檔名：bmi_check.py
功能：邏輯判斷練習
學習重點：條件分歧、布林邏輯運算
"""
weight = eval(input('Enter your weight: '))
height = eval(input('Enter your height: '))
heightMeter = height / 100
bmi = weight / (heightMeter * heightMeter)
print('Your BMI is %.2f'%(bmi))
if bmi < 18.5:
    print ('Underweight')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obese')
    