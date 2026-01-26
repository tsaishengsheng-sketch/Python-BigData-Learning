a = float(input('輸入第一個邊長 a:'))
b = float(input('輸入第一個邊長 b:'))
c = float(input('輸入第一個邊長 c:'))

if (a + b > c ) and (a + c > b) and (b + c > a):
    print ('這可以變成三角形')
    
    if a == b == c:
        print('正三角')
    elif a == b or b == c or a == c :
        print('等腰三角')
    else:
        print('不等邊三角')
else:
    print('無法組成三角')
