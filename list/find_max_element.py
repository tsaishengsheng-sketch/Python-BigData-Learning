"""
檔名：find_max_element.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random
def randomNum():
    lst = []
    for i in range(1, 101):
        num = random.randint(1, 100)
        lst.append(num)
    return lst

def display(lst2):
    for i in range(len(lst2)):
        if (i+1) % 10 == 0:
            print(f"{lst2[i]:3d}")
        else:
            print(f"{lst2[i]:3d}", end= '')

def biggest(lst2):
    large = lst2[0]
    for i in range(1, len(lst2)):
        if lst2[i] > large:
            large = lst2[i]
            index = i
    return index, large

def main():
    lst2 = randomNum()
    display(lst2)
    index, big = biggest(lst2)
#   print ('The biggest value is %d, it \'s index is %d'%(big,index))
    print(f"The biggest value is {big}, it's index is {index}")


main()