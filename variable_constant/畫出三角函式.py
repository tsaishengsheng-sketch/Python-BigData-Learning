"""
檔名：畫出三角函式.py
功能：基礎語法練習
學習重點：變數賦值、基本數學運算
"""
import math
#print sin
print('sin(0): %.2f'%(math.sin(0)))
print('sin(90): %.2f'%(math.sin((math.pi) / 2)))
print('sin(180): %.2f'%(math.sin(math.pi)))
print('sin(270): %.2f'%(math.sin((3 * math.pi) / 2)))
print('sin(360): %.2f'%(round(math.sin(2 * math.pi))))
print()

#print cos
print('cos(0): %.2f'%(math.cos(0)))
print('cos(90): %.2f'%(math.cos((math.pi) / 2)))
print('cos(180): %.2f'%(math.cos(math.pi)))
print('cos(270): %.2f'%(round(math.cos((3 * math.pi) / 2))))
print('cos(360): %.2f'%(math.cos(2 * math.pi)))
print()