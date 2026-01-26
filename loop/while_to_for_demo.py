#定數
total = 0
for i in range(1, 6):
    a = eval(input('Enter a number: '))
    total += a
print('total = %d'%(total))
#不定數
total = 0
for i in range(1, 10000000):
    a = eval(input('Enter a number: '))
    if a != 999:
        total += a
    else:
        break
print('total = %d'%(total))
