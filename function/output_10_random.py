"""
檔名：output_10_random.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
import random

def rand(n):
    for i in range(1, n+1):
        num = random.randint(1, 100)
        if i % 10 == 0:
            print(f"{num:4d}")
        else:
            print(f"{num:4d}", end= '')

def main():
    num = eval(input('要幾個亂數：'))
    rand(num)
main()