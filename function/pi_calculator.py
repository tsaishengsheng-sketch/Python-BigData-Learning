"""
檔名：pi_calculator.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
def pi (x):
    sum = 0
    for i in range(1, x+2, 100):
        for j in range(1, i+1):
            sum += 4 *(pow(-1, j+1) / (2*j -1))
        print(f"{i:4d}{sum:>10.5f}")
        sum = 0
def main():
    x= eval(input('輸入數字:'))
    print(f"{'x':>4}, {'pi(x)':>10}")
    print('-'*15)
    print()

    pi(x)

main()

