"""
檔名：random_sum.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random
data =[]
total = 0 
for i in range(10):
    data.append(random.randint(1, 10))
    total += data[i]
print(data)
print(f"total = {total}")                   