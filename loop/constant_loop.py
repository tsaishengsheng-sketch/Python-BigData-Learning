"""
檔名：constant_loop.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
total = 0
i = 1
while i <= 5:
    a = eval(input('Enter a number: '))
    total += a
    i += 1
print('The total is', total)