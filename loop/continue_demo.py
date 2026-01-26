"""
檔名：continue_demo.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
total = 0
i = 1
while i <= 100:
    if i == 9 or i == 99:
        i += 1
        continue
    else:
        total += i
        i += 1
        print('total = %d'%(total))