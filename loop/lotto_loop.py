"""
檔名：lotto_loop.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
import random
for i in range(1, 7):
    lottoNum = random.randint(1, 49)
    print(lottoNum, end = '')