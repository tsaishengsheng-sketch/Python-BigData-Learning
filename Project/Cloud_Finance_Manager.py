"""
檔名：Cloud_Finance_Manager.py
功能：個人雲端財務管理系統 (三層架構開發實作)
技術亮點：
    1. 分層架構設計：
       - 資料層 (Data Layer)：負責 pickle 二進位物件持久化。
       - 邏輯層 (Logic Layer) : 負責數值統計分析。
       - 展示層 (Presentation Layer)：負責 CLI 互動介面。
    2. 安全防禦邏輯：
       - 整合 os.path 進行檔案存在檢查，避免讀取崩潰。
       - 實作 try...except 多重例外捕捉，過濾 eval 非法輸入與檔案 IO 異常。
    3. 資料處理效能：
       - 運用串列生成式 (List Comprehension) 提取字典數據，並進行浮點數精確度格式化 (:.2f)。
"""

import pickle
import os

# --- 1. 資料存取模組 (Data Access Layer) ---

def load_records(filename):
    """從二進位檔還原物件 (學習點：pickle.load)"""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'rb') as infile:
            return pickle.load(infile) #
    except (IOError, EOFError):
        return []

def save_records(filename, data):
    """將物件封裝並寫入二進位檔 (學習點：pickle.dump)"""
    try:
        with open(filename, 'wb') as outfile:
            pickle.dump(data, outfile) #
            print(f"✅ 資料已成功同步至 {filename}")
    except IOError:
        print("❌ 儲存失敗，請檢查權限")

# --- 2. 業務邏輯模組 (Business Logic Layer) ---

def analyze_statistics(records):
    """數據分析與統計 (延伸自 File_Score_Statistical_Analyzer)"""
    if not records:
        return 0, 0
    
    # 提取所有金額並轉為數值
    amounts = [r['amount'] for r in records] #
    total = sum(amounts)
    average = total / len(records)
    return total, average

# --- 3. 主介面模組 (Presentation Layer) ---

def main():
    DB_NAME = "finance_vault.dat"
    records = load_records(DB_NAME)

    while True:
        print("\n--- 智慧帳單管理系統 ---")
        print("1. 新增消費紀錄")
        print("2. 顯示統計分析報表")
        print("3. 存檔並離開")
        
        choice = input("請選擇功能: ").strip()

        if choice == '1':
            try:
                item = input("輸入項目名稱: ").strip()
                # 結合 eval 或 float 處理輸入
                val = eval(input("輸入金額: "))
                records.append({"item": item, "amount": val})
            except (SyntaxError, NameError, ValueError): #
                print("⚠️ 金額格式輸入錯誤，請輸入純數字")
        
        elif choice == '2':
            total, avg = analyze_statistics(records)
            print(f"\n📊 [統計結果]")
            print(f"總計支出: ${total:.2f}") #
            print(f"平均每筆: ${avg:.2f}") #
            print(f"紀錄總數: {len(records)} 筆")

        elif choice == '3':
            save_records(DB_NAME, records)
            break
        else:
            print("⚠️ 無效的選擇")

if __name__ == "__main__":
    main()