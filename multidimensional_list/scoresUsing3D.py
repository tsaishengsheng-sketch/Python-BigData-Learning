"""
檔名：scoresUsing3D.py
功能：多維串列應用
學習重點：矩陣運算、巢狀迴圈與表格處理
"""
scores3Dim=[
    [[80, 88, 90],[78, 76, 88],[90, 91, 90]],
    [[70, 68, 89],[88, 86, 82],[80, 86, 92]],
    [[77, 78, 92],[74, 86, 88],[90, 94, 95]],
    [[72, 87, 92],[74, 86, 88],[90, 94, 95]],
    [[82, 68, 90],[67, 66, 68],[70, 71, 82]]]

print(f"{'calcu':>13s} {'Accou':>8s} {'prog':>8s}")
print("-------------------------------")

for i in range(len(scores3Dim)):
    print(f"{(i+1):3d}", end='')
    for j in range(len(scores3Dim[i])):
        total = 0
        for k in range(len(scores3Dim[i][j])):
            total += scores3Dim[i][j][k]
        average = total / 3
        print(f"{average:9.2f}", end='')
    print()

