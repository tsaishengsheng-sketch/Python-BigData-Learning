import random
# bubble sort 
def bubbleSort(Lst2):
    for i in range(len(Lst2) -1):
        flag = 0
        for j in range(len(Lst2) -i-1):
            if Lst2[j] > Lst2[j+1]:
                Lst2[j], Lst2[j+1] = Lst2[j+1], Lst2[j]
                flag =1
            if flag == 0 :
                break

#-----------------------------

def main():
    Lst = []
    for i in range(1,11):
        num = random.randint(1, 100)
        Lst.append(num)

    print('Original data:')
    for x in Lst:
        print(f"{x:3d}", end='')
    print('\n')

    bubbleSort(Lst)
    print('Sorted data:')
    for x in Lst:
        print(f"{x:3d}", end ='')
    
    print()
main()