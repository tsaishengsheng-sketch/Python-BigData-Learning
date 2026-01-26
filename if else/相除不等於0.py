# 相除不等於0
a = eval (input('Enter a number1: '))
b = eval (input('Enter a number2: '))
if b != 0:
        c = a / b
        print('%.2f /%.2f = %.2f'%(a, b, c))
else:
        print('Divisor con\'t be zero')        
print('Over')

