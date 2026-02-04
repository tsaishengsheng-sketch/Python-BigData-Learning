"""
檔名：lotto_generator.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
import random
def lotto():
    for i in range(1,7):
        n = random.randint(1, 49)
        print(n)

def main():
    again = 1
    while again ==1 :
        lotto()
        again = eval(input('再一次？ 1 or 0: '))
main()