def menu():
    print('--- 候選人名單 ---')
    print('(1) 小柯  (2) 小丁  (3) 小糖')

def candicate(n):
    n1 = n2 = n3 = others = 0
    for i in range(1, n + 1):
        print(f"\n第 {i} 位投票中...")
        menu()
        
        # 轉換輸入
        try:
            who = int(input('請輸入選擇的編號：'))
        except:
            who = 0 # 若輸入非數字則設為無效票
            
        if who == 1:
            n1 += 1
        elif who == 2:
            n2 += 1
        elif who == 3:
            n3 += 1
        else:
            others += 1
            
        print("\n--- 目前票數統計 ---")
        print(f"小柯: {n1:2d} 票")
        print(f"小丁: {n2:2d} 票")
        print(f"小糖: {n3:2d} 票")
        print(f"廢票: {others:2d} 票")

def main():  
    candicate(5) 

main()