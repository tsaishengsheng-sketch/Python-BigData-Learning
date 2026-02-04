"""
檔名：six_digit_lotto.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
import random
def int(n):
    for i in range(1, n+1):
        for i in range(1, 7):
            int = random.randint(1,49)
            print(f"{int:3d}", end = ' ')
        print()
def main():
    num = eval(input('要幾組：'))
    int(num)

main()
