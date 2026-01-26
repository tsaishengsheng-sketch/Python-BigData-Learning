"""
檔名：lotto_list_10.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random

lotto = []
lotto.append(random.randint(1,49))

for m in range(1,6):
    n = 0
    while n < m :
        temp = random.randint(1, 49)
        if(temp ==lotto[n]):
            n = 0
        else:
            n += 1
    lotto.append(temp)

print(f"the lottery numbers are: {temp}")
for i in lotto :
    print(f"{(i):4d}")
print()


