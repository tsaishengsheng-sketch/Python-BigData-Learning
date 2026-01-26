"""
檔名：multiples_of_5_sum.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
# for 
total = 0
for i in range(5, 101, 5):
    total += i
print(f"total:{total}")

#while loop
total = 0
i = 5
while i <= 100:
    total += i
    i += 5
print(f"total:{total}")
