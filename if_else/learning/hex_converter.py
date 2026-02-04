"""
檔名：hex_converter.py
功能：邏輯判斷練習
學習重點：條件分歧、布林邏輯運算
"""
num = int(input("請輸入一個 0~15 之間的數字: "))

if 0 <= num <= 15:
    # hex(num) 會得到 '0xa'，我們用 [2:] 去掉開頭的 '0x'，並用 upper() 轉大寫
    result = hex(num)[2:].upper()
    print(f"數字 {num} 的十六進位值為: {result}")
else:
    print("錯誤！請輸入 0~15 之間的數字。")