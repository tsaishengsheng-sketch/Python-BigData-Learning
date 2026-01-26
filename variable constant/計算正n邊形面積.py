import math
num = eval(input('How many sides: '))
side = eval(input('Enter Length of a side: '))
area = (num * side ** 2) / (4 * math.tan(math.pi/num))
print('Area of n-side is %.2f'%(area))
