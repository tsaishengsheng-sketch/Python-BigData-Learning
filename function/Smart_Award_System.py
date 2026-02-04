import math
import random

# --- 1. 基礎數據模組 (BMI & 溫標) ---
def check_basic_info():
    print("\n[系統初始化：員工數據登錄]")
    w = float(input("請輸入體重 (kg): "))
    h = float(input("請輸入身高 (cm): "))
    c_t = float(input("請輸入當前辦公室攝氏溫度 (°C): "))
    
    bmi = w / ((h/100)**2)
    f_t = (c_t * 9/5) + 32  # 溫標練習
    # 隨機數練習：生成投票驗證碼
    v_code = random.randint(100000, 999999)
    return bmi, f_t, v_code

# --- 2. 考核模組 (總和平均 & GPA) ---
def evaluate_performance():
    print("\n[績效評估：成績結算]")
    # 總和平均練習
    s1, s2, s3 = eval(input("請輸入三項考核成績 (以逗號隔開, 如 80,90,85): "))
    avg = (s1 + s2 + s3) / 3
    
    # GPA 等第練習
    if avg >= 80: grade = 'A'
    elif avg >= 70: grade = 'B'
    elif avg >= 60: grade = 'C'
    else: grade = 'F'
    
    return avg, grade

# --- 3. 頒獎會場規劃 (多邊形面積 & 距離) ---
def plan_venue():
    print("\n[行政規劃：頒獎會場佈置]")
    n = int(input("請輸入頒獎台邊數 (正多邊形): "))
    s = float(input("請輸入單邊長度 (m): "))
    x, y = eval(input("請輸入會場中心座標 (x, y): "))
    
    area = (n * s ** 2) / (4 * math.tan(math.pi / n)) # 面積練習
    dist = math.sqrt(x**2 + y**2) # 距離練習
    return area, dist

# --- 4. 決策投票模組 (計票邏輯 + 驗證碼核對) ---
def start_voting(correct_code):
    print("\n[最終決選：身分安全驗證]")
    user_code = int(input("請輸入系統剛才發放的六位數驗證碼: "))
    
    if user_code != correct_code:
        print("❌ 驗證碼錯誤！安全機制已鎖定，無法投票。")
        return None

    print("✅ 驗證成功！請開始投票 (1) 小柯 (2) 小丁 (3) 小糖")
    v_results = [0, 0, 0]
    for i in range(3): # 模擬三位評審投票
        v = int(input(f"評審 {i+1} 投票編號: "))
        if 1 <= v <= 3: v_results[v-1] += 1
    return v_results

# --- 5. 主系統流程 ---
def main():
    print("🏆 企業年度優秀員工評選系統 (含安全驗證)")
    print("="*50)

    # A. 初始化並取得驗證碼
    bmi, f_temp, security_code = check_basic_info()
    print(f">> 系統紀錄：BMI {bmi:.1f}, 環境華氏 {f_temp:.1f}°F")
    print(f">> 【重要】您的投票驗證碼為：{security_code} (請牢記)")

    # B. 績效考核
    avg_score, grade = evaluate_performance()
    print(f">> 績效平均：{avg_score:.1f}，評定等級：{grade}")

    # C. 連貫邏輯判定：A 級員工才進入頒獎與投票
    if grade == 'A':
        print("\n🌟 績效優異！啟動優秀員工選拔流程...")
        
        # 規劃會場
        area, dist = plan_venue()
        print(f">> 會場面積：{area:.2f} m², 距離總部：{dist:.2f} km")
        
        # 安全投票
        votes = start_voting(security_code)
        
        if votes:
            print("\n" + "★" * 15 + " 最終評選結果 " + "★" * 15)
            print(f"小柯: {votes[0]} 票 | 小丁: {votes[1]} 票 | 小糖: {votes[2]} 票")
    else:
        print(f"\n❌ 很遺憾，等級 {grade} 未達優秀員工參選門檻 (需為 A)。")

    print("="*50)

if __name__ == "__main__":
    main()