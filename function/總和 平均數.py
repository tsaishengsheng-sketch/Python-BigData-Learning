def average(a, b):
    total = a + b 
    aver = total / 2
    return total, aver

def main():
    x, y = eval(input('輸入兩個數：'))
    tot2, aver2 = average(x,y)

    print(f"總和為：{tot2}, 平均為：{aver2:.2f}")

main()