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