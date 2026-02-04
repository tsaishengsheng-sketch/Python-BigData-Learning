"""
檔名：lst2Dim.py
功能：多維串列應用
學習重點：矩陣運算、巢狀迴圈與表格處理
"""
import random
lst =[]
rows = eval(input('How many rows: '))
columns = eval(input('How many columns: '))
for i in range(rows):
    lst.append([])
    for j in range(columns):
        num = random.randint(1, 49)
        lst[i].append(num)

for x in range(rows):
    for y in range(columns):
        print(f"{lst[x][y]:3d}", end='')
    print()