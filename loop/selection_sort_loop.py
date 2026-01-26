"""
檔名：selection_sort_loop.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
import random
lst = []
for i in range(1,11):
    num = random.randint(1,100)
    lst.append(num)

print('Original data:')
for x in lst:
    print(f"{x:3d}", end = '' )
print('\n')

# selection sort 
for i in range(len(lst) -1 ):
    min = lst[i]
    minIndex = i
    for j in range(i+1, len(lst)):
        if lst[j] < min:
            min = lst[j]
            minIndex = j
    if minIndex != i:
        lst[minIndex] = lst[i]
        lst[i] = min

# ===================

print('Sorted data:' )
for x in lst:
    print(f"{x:3d}",end = '')

print()
