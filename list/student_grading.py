"""
檔名：student_grading.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
def best(lst2):
    max = lst2[0]
    for i in range(len(lst2)):
        if lst2[i] > max:
            max = lst2[i]
    return max

def grade(g, lst2):
    for i in range(len(lst2)):
        if lst2[i] >= g-5:
            #print('score:%2d is grade A'%(lst2[i]))
            print(f"score:{lst2[i]:2d} is grade A")
        elif lst2[i] >= g-15:
            print(f"score:{lst2[i]:2d} is grade B")
        elif lst2[i] >= g-25:
            print(f"score:{lst2[i]:2d} is grade C")
        elif lst2[i] >= g-35:
            print(f"score:{lst2[i]:2d} is grade D")
        else:
            print(f"score:{lst2[i]:2d} is grade F")

def main():
    scoreslst = []
    score = eval(input('Enter score: '))
    while score >= 0 :
        scoreslst.append(score)
        score = eval(input('Enter score: '))
    greatest = best(scoreslst)
    grade(greatest, scoreslst)

main()