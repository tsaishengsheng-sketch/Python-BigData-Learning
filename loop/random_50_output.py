"""
檔名：random_50_output.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
import random
for i in range(1, 51):
    randNum = random.randint(1, 49)
    print(f"randNum:{randNum:4d}")
