"""
檔名：print_table.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
for i in range(1, 10):
    row = ""
    for j in range(1, i + 1):
        # 計算乘積並格式化為佔 3 格寬度
        res = i * j
        row += f"{res:<3}"
    print(f"{row}")