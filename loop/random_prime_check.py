"""
檔名：random_prime_check.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
import random
data = random.randint(1, 1000)
isPrime = True
divisor = 2
while divisor <= data / 2:
    if data % divisor ==0 :
        isPrime = False
        break
    divisor += 1
if isPrime:
    print('%d is a prime number. '%(data))
else:
    print('%d is not a prime number. '%(data))