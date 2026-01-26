"""
檔名：even_sum_1_100.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(f"total = {total}")