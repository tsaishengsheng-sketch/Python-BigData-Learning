"""
檔名：selection_sort_function.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random

# Selection sort
def selectionSort(Lst2):
    for i in range(len(Lst2) - 1):
        min_val = Lst2[i]
        minIndex = i 
        # 內層迴圈：找出剩餘資料中的最小值
        for j in range(i + 1, len(Lst2)):
            if Lst2[j] < min_val:
                min_val = Lst2[j]
                minIndex = j

        # 修正：將交換邏輯移出內層迴圈，且不要加上中括號
        if minIndex != i:
            Lst2[minIndex] = Lst2[i]
            Lst2[i] = min_val

# -----------------------------------
def main():
    Lst = []
    for i in range(1, 11):
        num = random.randint(1, 100)
        Lst.append(num)

    print('Original data:')
    for x in Lst:
        print(f"{x:3d}", end='')
    print('\n')

    selectionSort(Lst)

    print('Sorted data:')
    for x in Lst:
        print(f"{x:3d}", end='')
    print() # 避免出現 % 符號

main()