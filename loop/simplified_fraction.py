gcd = 1 
n = 2

x, y = eval(input('Enter a fraction(x/y): '))
p, q = eval(input('Enter a fraction(p/q): '))
a = x*q + p*y
b = y*q
while n <= a and n<= b:
    if a % n == 0 and b % n == 0 :
        gcd = n
    n += 1
print('GCD(%d, %d) = %d'%(a, b, gcd))
fa = a // gcd
fb = b // gcd
print('%d/%d + %d%d = %d%d'%(x, y, p, q, fa, fb))
