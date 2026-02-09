"""
檔名：Smart_Inventory_System.py
功能：實戰專案開發
學習重點：模組化整合與系統實作
"""
import random
import math

# --- 1. 庫存生成 (List 基礎與隨機數) ---
def generate_inventory(size=50):
    # 生成 50 組不重複的商品 ID (100-999)
    product_ids = random.sample(range(100, 1000), size)
    # 生成對應的價格 (50-5000)
    prices = [random.randint(50, 5000) for _ in range(size)]
    return product_ids, prices

# --- 2. 庫存排序 (Bubble Sort - 按 ID 排序) ---
def sort_inventory(ids, prices):
    n = len(ids)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if ids[j] > ids[j+1]:
                # 連動交換：ID 交換時，價格也要跟著換，邏輯才正確
                ids[j], ids[j+1] = ids[j+1], ids[j]
                prices[j], prices[j+1] = prices[j+1], prices[j]
                swapped = True
        if not swapped: break
    return ids, prices

# --- 3. 高效檢索 (Binary Search) ---
def search_product(ids, target_id):
    low, high = 0, len(ids) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if ids[mid] == target_id:
            return mid, count
        elif ids[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1, count

# --- 4. 營運統計 (統計與 Max 邏輯) ---
def analyze_data(prices):
    avg_price = sum(prices) / len(prices)
    max_price = max(prices)
    max_index = prices.index(max_price)
    # 計算變異數 (Variance) 觀察價格波動
    variance = math.sqrt(sum((x - avg_price)**2 for x in prices) / len(prices))
    return avg_price, max_price, max_index, variance

# --- 主程式流程 ---
def main():
    print("📦 智慧電商庫存管理系統")
    print("="*40)

    # A. 系統初始化
    ids, prices = generate_inventory()
    ids, prices = sort_inventory(ids, prices)
    print(f"✅ 已成功導入 {len(ids)} 筆商品數據並完成排序。")

    # B. 營運數據摘要
    avg, m_price, m_idx, var = analyze_data(prices)
    print(f"📊 營運摘要：平均售價 ${avg:.1f} | 最高價商品 ID: #{ids[m_idx]} (${m_price})")
    print(f"📈 價格波動標準差: {var:.2f}")

    # C. 客戶檢索模擬
    print("\n" + "-"*40)
    try:
        search_id = int(input("🔎 請輸入欲查詢的商品 ID: "))
        idx, steps = search_product(ids, search_id)
        
        if idx != -1:
            print(f"✅ 找到商品！價格為: ${prices[idx]}")
            print(f"⚡ 效率： {steps} 次比對。")
        else:
            print(f"❌ 查無此商品 (搜尋次數: {steps})")
    except ValueError:
        print("⚠️ 輸入錯誤，請輸入整數 ID。")

if __name__ == "__main__":
    main()