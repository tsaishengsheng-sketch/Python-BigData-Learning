import random

def rand(n):
    for i in range(1, n+1):
        num = random.randint(1, 100)
        if i % 10 == 0:
            print(f"{num:4d}")
        else:
            print(f"{num:4d}", end= '')

def main():
    num = eval(input('要幾個亂數：'))
    rand(num)
main()