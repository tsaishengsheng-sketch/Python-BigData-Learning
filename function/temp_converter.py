"""
檔名：temp_converter.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
def FtoC (start, end):
    for i in range(start, end+1, 5):
        C = (5/9*(i-32))
        print(f"{i:15d}, {C:>10.2f}")

def main():
    start, end = eval(input('start, çend: '))
    print(f"{'i':>15}, {'C':>10}")
    print('-' *20)

    FtoC(start, end)

main()