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