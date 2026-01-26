"""
檔名：lcm_finder.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
gcd = 1
n = 2
a = eval(input('Enter a number:'))
b = eval(input('Enter a number:'))
while n <= a and n <= b:
    if a % n == 0 and b % n == 0:
        gcd = n
    n += 1
print('GCD(%d,%d) = %d'%(a, b, gcd))
