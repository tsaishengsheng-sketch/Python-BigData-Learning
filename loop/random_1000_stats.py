"""
檔名：random_1000_stats.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
import random
even = 0
multiple5 = 0 
for i in range(1, 1001):
    randNum = random.randint(1,200)
    if randNum % 2 == 0 :
        even += 1
    if randNum % 5 == 0 :
        multiple5 += 1
print('even number = %d'%(even))
print('odd number = %d'%(1000-even))
print('even number = %d'%(multiple5))
