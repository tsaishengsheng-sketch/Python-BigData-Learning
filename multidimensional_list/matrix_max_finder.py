"""
檔名：matrix_max_finder.py
功能：多維串列應用
學習重點：矩陣運算、巢狀迴圈與表格處理
"""
import random
lst = []
rows = eval(input('How many rows: '))
columns = eval(input('How many columns: '))
for i in range(rows):
    lst.append([])
    for j in range(columns):
        num = random.randint(1, 100)
        lst[i].append(num)

biggest = lst[0][0]
indexOfRow = 0
indexOfColumn = 0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] >biggest:
            biggest =lst[i][j]
            indexOfRow = i
            indexOfColumn = j

for x in range(rows):
    for y in range(columns):
        print(f"{(lst[x][y]):5d}", end='')
    print()

print(f"The Largest value is {biggest} at lst [{indexOfRow}][{indexOfColumn}]")