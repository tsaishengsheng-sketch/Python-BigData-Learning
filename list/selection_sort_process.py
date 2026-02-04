"""
檔名：selection_sort_process.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random
lst = []
for i in range(1, 11):
    num = random.randint(1, 100)
    lst.append(num)

print('Original data:')
for x in lst:
    print(f"{x:3d}", end= '')
print('\n')

#selection sort 
print('sorting')
for i in range(len(lst)-1):
    print(f"step= {(i+1)}")
    min = lst[i]
    minIndex = i
    for j in range(i+1, len(lst)):
        if lst[j] < min:
            min = lst[j]
            minIndex = j
        if minIndex != i:
            lst[minIndex] = lst[i]
            lst[i] = min
        #print data
        for x in lst:
            print(f"{x:3d}", end='')
        print('\n')

#-----------------

print('Sorted data:') 
for x in lst:
    print(f"{x:3d}", end='')
print()