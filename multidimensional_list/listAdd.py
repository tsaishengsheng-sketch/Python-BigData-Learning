"""
檔名：listAdd.py
功能：多維串列應用
學習重點：矩陣運算、巢狀迴圈與表格處理
"""
lst1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]

lst2=[
    [2,4,6],
    [8,10,12],
    [14,16,18]]

lst3=[]
for i in range(len(lst1)):
    lst3.append([])
    for j in range(len(lst2)):
        num = lst1[i][j] +lst2[i][j]
        lst3[i].append(num)

for row in lst3:
    for value in row:
        print(f"{value:3d}", end='')
    print()