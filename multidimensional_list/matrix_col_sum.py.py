"""
檔名：matrix_col_sum.py.py
功能：多維串列應用
學習重點：矩陣運算、巢狀迴圈與表格處理
"""
lst44=[
    [11, 2, 3, 14],
    [5, 16, 7, 8],
    [9, 10, 11, 12],
    [3, 2, 5, 1]]

smallest = 999999
indexOfCol = -1
for col in range(0,len(lst44[0])):
    total = 0
    for row in range(len(lst44)):
        total += lst44[row][col]
    print(f"Total of {col} columns ={total}")

    if total < smallest:
        smallest = total
        indexOfCol =col
print(f"The smallest value is {smallest}, at column is {indexOfCol}")