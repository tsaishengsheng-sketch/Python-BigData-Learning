"""
檔名：lotto_simulator.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random
lotto = []
count = 1
while count <= 6:
    num = random.randint(1, 49)
    if num not in lotto:
            lotto.append(num)
            count += 1
guess = []
count = 1
while count <= 6:
    a = eval(input('Enter a lotto number (1~49): '))
    if a not in guess:
        guess.append(a)
        count += 1
lotto.sort()
print('The Lotto numbers are: ')
for x in lotto:
    print(f"{x:3d}", end= '')
print('\n')

guess.sort()
print('Your guess numbers are: ')
for x in guess:
    print(f"{x:3d}", end= '')
print('\n')

correct = 0
for i in range(len(guess)):
    if guess[i] in lotto:
         correct += 1
print('Correct number(s): %d'%(correct))
     