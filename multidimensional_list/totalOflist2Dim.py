"""
檔名：totalOflist2Dim.py
功能：多維串列應用
學習重點：矩陣運算、巢狀迴圈與表格處理
"""
lst34 =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

total = 0
for i in range(len(lst34)):
    for j in range(len(lst34[i])):
        total += lst34[i][j]

print(f"Total:{total}")