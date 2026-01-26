"""
檔名：矩形面積和周長.py
功能：基礎語法練習
學習重點：變數賦值、基本數學運算
"""
length = eval(input('Enter a Length: '))
width = eval(input('Enter a Width: '))
rect_area = length * width
rect_perimeter = 2 * (length + width)
print('Length and width of the rectangle is %d and %d'%(length, width))
print('area is %d, perimeter is %d'%(rect_area, rect_perimeter))