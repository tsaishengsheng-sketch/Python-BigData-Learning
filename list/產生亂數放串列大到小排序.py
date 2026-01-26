import random
def main():
    Lst = []
    for i in range (1, 11):
        num = random.randint(1, 100)
        Lst.append(num)

    print('Original data: ')
    for x in Lst:
        print(f"{x:3d}", end = '')
    print('\n')

    Lst.sort()
    Lst.reverse()
    print('Decending sorting.....')
    print('Sorted data: ')
    for x in Lst:
        print(f"{x:3d}", end='')
    print()

main()