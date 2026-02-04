"""
檔名：add spaces.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
for i in range(1, 10):
    for j in range(9, i, -1):
        print(' ', end = '')
        
    for k in range(1, i+1):
        print(i, end = ' ')
    print()    