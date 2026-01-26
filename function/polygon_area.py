import math
def nArea(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi/n))
    return area

def main():
    num = eval(input('邊數：'))
    side = eval(input('邊長：'))
    area2 = nArea(num, side)
    print(f"{num}邊形面積是:{area2:.2f}")

main()