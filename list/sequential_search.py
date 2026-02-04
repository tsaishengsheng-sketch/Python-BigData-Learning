"""
檔名：sequential_search.py
功能：資料結構與排序
學習重點：串列操作、演算法效率優化
"""
import random
def randNum():  
    randLst = []
    count = 1
    while count <= 6:
        num = random.randint(1, 49)
        if num not in randLst:
            randLst.append(num)
            print(f"{num:3d}" , end= '')
            count += 1
    print()
    return randLst

def seqSearch(key, Lst2):
    for i in range(len(Lst2)):
        if key == Lst2[i]:
            print(f"I got{key,i:d}")
            return True
    
def main():
    Lst = randNum()
    sn = eval(input('what number do you search? '))
    bool = seqSearch(sn, Lst)
    if bool !=True:
        print(f"is not found {sn:d}")

main()