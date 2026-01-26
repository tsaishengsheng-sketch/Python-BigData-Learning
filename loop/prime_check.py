"""
檔名：prime_check.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
data = eval(input('Enter a number : '))
isPrime = True
divisor = 2
while divisor <= data // 2:
    if data % divisor == 0:
        isPrime = False
        break
    divisor += 1    
if isPrime:
    print('%d is a prime number'%(data))
else:
    print('%d is not a prime number'%(data))