"""
檔名：sum_1_100.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
total = 0
i = 1 
while i<=100:
    total += i
    i += 1
    print('total = %d'%(total))
    
#偶數和
even_total = 0
i = 2
while i <= 100:
    even_total += i
    i += 2
    print('even_total = %d'%(even_total))

#奇數和
odd_total = 0
i = 1
while i <= 100:
    odd_total += i
    i += 2
    print('odd_total = %d'%(odd_total))
    