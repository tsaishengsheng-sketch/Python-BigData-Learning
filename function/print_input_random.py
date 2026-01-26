"""
檔名：print_input_random.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
import random
def randNum(k):
    for i in range(1, k+1):
        n = random.randint(1, 100)
        print(n)
def main():
    n = eval(input('要產生幾個數？：'))
    randNum(n)
main()
