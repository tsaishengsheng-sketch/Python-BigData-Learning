"""
檔名：totalOfEachCol.py
功能：多維串列應用
學習重點：矩陣運算、巢狀迴圈與表格處理
"""
lst34 = [
    [1, 2,   3,  4],
    [5, 6,   7,  8],
    [9,10,11,12]]

for col in range(len(lst34[0])):
    total = 0
    for row in range(len(lst34)):
        total += lst34[row][col]
    print(f"Total of {col} colimns ={total}")