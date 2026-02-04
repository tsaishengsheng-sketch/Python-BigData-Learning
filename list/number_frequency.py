"""
檔名：number_frequency.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random

def display(lst2):
    for n in range(len(lst2)):
        print(f"{lst2[n]:3d}", end = '')
        if (n+1) % 10 == 0:
            print()

def sortedDisplay(lst2):
    print('\nAfter sorted:')
    lst2.sort()
    for n in range(len(lst2)):
        print(f"{lst2[n]:3d}", end='')
        if (n+1) % 10 ==0 :
            print()

def calculateNum(lst2):
    lst = 50 * [0]
    for j in range(len(lst2)):
        lst[lst2[j]] += 1
    print('\n')
    for k in range(1, len(lst)):
        #print ('%2d: %d '%(k, lst[k]), end='')
        print(f"{k:2d}: {lst[k]} ", end='')
        if k & 10 ==0 :
            print()

def main():
    lottoNum = []
    for i in range(100):
        num = random.randint(1, 49)
        lottoNum.append(num)
    display(lottoNum)
    sortedDisplay(lottoNum)
    calculateNum(lottoNum)

main()