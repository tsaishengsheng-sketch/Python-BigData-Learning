"""
檔名：break_demo.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
total = 0
a = eval(input('Enter a number : '))
while a != 999:
    total += a
    a = eval(input('Enter a number : '))
    print('total = %d'%(total))