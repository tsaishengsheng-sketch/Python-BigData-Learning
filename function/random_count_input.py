"""
檔名：random_count_input.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
import random
def rand(a, b, n):
    for i in range(1, n+1):
        rn =random.randint(a, b)
        if i % 10 == 0:
            print(f"{rn:4d}")
        else:
             print(f"{rn:4d}", end = '')

def main():
    x, y, rn = eval(input('Enter: x, y, num: '))
    rand(x, y, rn)

main()