"""
檔名：random_list_sort_desc.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
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