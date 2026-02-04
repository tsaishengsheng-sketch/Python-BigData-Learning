"""
檔名：binary_search.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random

def randNum():
    randLst = []
    count = 1
    while count <= 6:
        num = random.randint(1, 49)
        if num not in randLst:
            randLst.append(num)
            count += 1
    randLst.sort()  # 二分搜尋前必須先排序
    return randLst

def binSearch(key, Lst2):
    Low = 0
    high = len(Lst2) - 1
    count = 1
    while high >= Low:
        mid = (Low + high) // 2
        if key < Lst2[mid]:
            high = mid - 1
        elif key == Lst2[mid]:
            return mid, count
        else:
            Low = mid + 1
        count += 1
    return -999, count # 回傳 count 可以觀察即便沒找到也找了幾次

def main():
    lst = randNum()
    print("Sorted Numbers: ", end='')
    for x in lst:
        print(f"{x:3d}", end='')
    print('\n')

    try:
        key = int(input('What number do you want to search? '))
        n, c = binSearch(key, lst)
        
        if n == -999:
            print(f"Target {key} is NOT FOUND.")
            print(f"Total comparisons: {c - 1}")
        else:
            # 修正格式化，避免印出元組 (tuple)
            print(f"I found {key} at index {n}")
            print(f"Total comparisons: {c}")
    except ValueError:
        print("Please enter a valid integer.")

main()