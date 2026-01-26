"""
檔名：gpa_calculator.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
def gpa(score):
    if score >= 80:
        print('A')
    elif score>= 70:
        print('B')
    elif score>= 60:
        print('C')
    elif score>= 50:
        print('D')
    else:
        print('E')
    
def main():
    score = eval(input('輸入成績：'))

    while score >= 0:
        gpa(score)
        score = eval(input('輸入成績：'))
    
main()