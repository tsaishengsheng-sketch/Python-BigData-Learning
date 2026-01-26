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
