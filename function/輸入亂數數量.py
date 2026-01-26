import random
def randNum(k):
    for i in range(1, k+1):
        n = random.randint(1, 100)
        print(n)
def main():
    n = eval(input('要產生幾個數？：'))
    randNum(n)
main()
