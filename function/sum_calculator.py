"""
檔名：sum_calculator.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
def S(x):
    tot = 0
    for i in range(1, x+1):
        tot += i/(i+1)
        print(f"{i:2d}, {tot:>10.2f}")

def main():
    x = eval(input('輸入數字：'))
    print(f"{'x':>2} {'S(x)':>10}")
    print('-' *14)
    print()

    S(x)

main()