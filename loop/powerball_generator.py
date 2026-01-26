"""
檔名：powerball_generator.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
import random
for i in range(1, 7):
    Lotto = random.randint(1, 38)
    print(Lotto , end = ' ')
Lotto2 = random.randint(1, 8)
print()
print('特別號碼,',( Lotto2))
