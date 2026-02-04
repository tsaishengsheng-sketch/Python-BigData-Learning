"""
檔名：guess_0_100.py
功能：邏輯判斷練習
學習重點：條件分歧、布林邏輯運算
"""
# 這是根據「生日卡片原理」改寫的 Python 版本
print("請在心中想一個 1 到 100 的數字...")

answer = 0
# 1~100 需要 7 組數字 (2^7 = 128)
for i in range(7):
    weight = 2**i  # 每一組的基數：1, 2, 4, 8, 16, 32, 64
    
    print(f"\n--- 第 {i+1} 組數字 ---")
    
    # 建立卡片：找出所有二進位第 i 位是 1 的數字
    card = [str(n) for n in range(1, 101) if (n & weight)]
    
    # 漂亮地印出數字，每 10 個換一行
    for j in range(0, len(card), 10):
        print("  ".join(card[j:j+10]))
    
    choice = input("\n請問這裡面有你選的數字嗎？(y/n): ").lower()
    
    if choice == 'y':
        answer += weight

print("-" * 30)
print(f"神奇吧！你心裡的數字是：{answer}")
print("-" * 30)