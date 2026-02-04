import random

def main():
    while True:
        print("\n--- 🔢 全能數字研究員 (Number Lab) ---")
        print("1. 數字規律生成 (金字塔/九九乘法)")
        print("2. 質數/公因數分析器")
        print("3. 自動選號與排序系統")
        print("Q. 退出程式")
        
        choice = input("\n請選擇功能: ").upper()
        
        if choice == '1':
            # 整合你的金字塔代碼
            for i in range(1, 10):
                print(" " * (9 - i) + " ".join(str(j) for j in range(1, i + 1)))
        
        elif choice == '2':
            # 整合你的 GCD 與 質數代碼
            num = int(input("輸入欲分析的整數: "))
            # 這裡放入你寫過的 isPrime 邏輯...
            print(f"分析完畢：{num} 為質數狀態偵測中...")
            
        elif choice == '3':
            # 整合你的 Lotto 與 Selection Sort 代碼
            nums = [random.randint(1, 49) for _ in range(6)]
            print(f"原始號碼: {nums}")
            # 這裡放入你寫過的選擇排序邏輯...
            nums.sort() # 或者用你的手寫排序
            print(f"排序後的幸運號碼: {nums}")
            
        elif choice == 'Q':
            break

if __name__ == "__main__":
    main()