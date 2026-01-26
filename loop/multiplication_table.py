"""
檔名：multiplication_table.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
for i in range(1, 10):
    for j in range(1, 10):
        print('%d*%d=%2d  '%(j, i, i*j), end = '')
print()