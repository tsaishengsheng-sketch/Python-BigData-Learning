"""
檔名：status_calculator.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random
import math

def creatNum():
    numLst = []
    for i in range(1, 101):
        num = random.randint(1, 50)
        numLst.append(num)
    return numLst

def display(lst2):
    for i in range(len(lst2)):
        if (i+1) % 10 == 0:
            print(f"{lst2[i]:3d}")
        else:
            print(f"{lst2[i]:3d}", end= '')

def mean(lst2):
    total = 0
    for i in range(len(lst2)):
        total += lst2[i]
    average = total / len(lst2)
    return average

def variance(lst2, aver):
    sum = 0
    for i in range(len(lst2)):
        sum += pow((lst2[i] - aver), 2)
    var = math.sqrt(sum)
    return var

def main():
    lst = creatNum()
    display(lst)
    aver = mean(lst)
    #print('\nMean is % .2f'%(aver))    
    print(f"\nMean is {aver:.2f}")
    var = variance(lst, aver)
    print(f"Variance is {var:.2f}")

main()
