"""
檔名：RealEstate_Investment_Analyzer.py
功能：地產投資分析器 (財務運算與幾何估價綜合系統)
技術亮點：
    1. 數位拆解邏輯：運用模數運算 (%) 與整數除法 (//) 實作 6 位數編號的提取與反轉校驗。
    2. 科學運算整合：導入 math 模組進行弧度轉換與三角函數運算，實作不規則土地面積精確估算。
    3. 金融財務模型：
       - 實作「本息平均攤還」公式，計算複利環境下的月付金與利息總成本。
       - 構建對比分析邏輯，透過資料變數模擬不同還款年限下的利息節省方案。
    4. 資料格式化輸出：整合字串格式化 (:.2f) 與 eval 處理動態輸入，生成專業級投資分析報告。
"""
import math

# --- 第一階段：產權文件編號校驗 ---
print("=== Step 1: 產權文件編號校驗 (資料完整性驗證) ===")
doc_id = eval(input('請輸入 6 位數地籍編號 (如 123456): '))

# 數位拆解與反轉還原
d1 = doc_id % 10
d2 = (doc_id // 10) % 10
d3 = (doc_id // 100) % 10
d4 = (doc_id // 1000) % 10
d5 = (doc_id // 10000) % 10
d6 = (doc_id // 100000)
print(f'系統解析校驗碼：{d1}{d2}{d3}{d4}{d5}{d6}')


# --- 第二階段：不規則土地面積估價 ---
print("\n=== Step 2: 不規則土地面積估價 (三角測量) ===")
side_a = eval(input('土地第一邊長 (公尺): '))
side_b = eval(input('土地第二邊長 (公尺): '))
angle_degree = eval(input('兩邊夾角 (角度): '))

# Area = 0.5 * a * b * sin(θ)
radians = math.radians(angle_degree)
land_area = 0.5 * side_a * side_b * math.sin(radians)
print('測量土地總面積: %.2f 平方公尺'%(land_area))


# --- 第三階段：房貸本息攤還與提前還款對比 ---
print("\n=== Step 3: 房貸財務分析與省錢方案對比 ===")
loan_amount = eval(input('預計貸款總額: '))
annual_rate = eval(input('預計年利率 (%): '))
plan_a_years = eval(input('方案 A：原始貸款年限 (如 40 年): '))
plan_b_years = eval(input('方案 B：目標還清年限 (如 20 年): '))

# 統一計算邏輯 (封裝在計算邏輯內)
monthly_rate = annual_rate / 1200

# 方案 A 計算
months_a = plan_a_years * 12
factor_a = pow(1 + monthly_rate, months_a)
pay_a = (loan_amount * monthly_rate * factor_a) / (factor_a - 1)
total_interest_a = (pay_a * months_a) - loan_amount

# 方案 B 計算
months_b = plan_b_years * 12
factor_b = pow(1 + monthly_rate, months_b)
pay_b = (loan_amount * monthly_rate * factor_b) / (factor_b - 1)
total_interest_b = (pay_b * months_b) - loan_amount

# 省錢計算
saved_money = total_interest_a - total_interest_b

print('-' * 45)
print('【房產投資財務分析報告】')
print(f'方案 A ({plan_a_years}年) 月付金：${pay_a:.2f}')
print(f'方案 A 總利息成本：${total_interest_a:.2f}')
print(f'方案 A 利息佔本金比：{(total_interest_a/loan_amount)*100:.2f}%')
print('-' * 15)
print(f'方案 B ({plan_b_years}年) 月付金：${pay_b:.2f}')
print(f'方案 B 總利息成本：${total_interest_b:.2f}')
print('-' * 15)
print(f'🌟 決策分析：若選擇方案 B，您將省下 ${saved_money:.2f} 的利息！')
print(f'   (相當於省下了約 {saved_money / (loan_amount/100):.1f}% 的購屋成本)')
print('-' * 45)