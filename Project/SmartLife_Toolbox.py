"""
檔名：SmartLife_Toolbox.py
功能：智慧生活工具箱 (多功能整合應用程式)
技術亮點：
    1. 互動式選單設計：實作無窮迴圈 (While True) 搭配條件分支，建構穩定且直覺的 CLI 操作介面。
    2. 資料解析與轉換：運用 split() 方法將單一字串輸入解析為動態串列 (List)，實作靈活的決策演算法。
    3. 邏輯分支應用：透過 BMI 數值區間判定，實作多層級的健康診斷邏輯與個性化建議輸出。
    4. 隨機性邏輯：整合 random.choice 進行非決定性運算，模擬真實生活中的隨機決策場景。
"""
import random

def health_check():
    print("\n--- 健康檢查模組 ---")
    weight = float(input('請輸入體重 (kg): '))
    height = float(input('請輸入身高 (cm): '))
    bmi = weight / ((height/100) ** 2)
    print(f'您的 BMI 是: {bmi:.2f}')
    
    # 這裡延伸你的 if-else，加入建議
    if bmi < 18.5:
        status = "過輕"
        advice = "多補充蛋白質，加強重量訓練！"
    elif bmi < 25:
        status = "正常"
        advice = "太棒了，請繼續保持運動習慣。"
    else:
        status = "肥胖"
        advice = "建議增加有氧運動，並控制糖分攝取。"
    
    print(f"診斷結果：{status} | 建議：{advice}")

def random_decision():
    print("\n--- 決策小幫手 ---")
    options = input("請輸入三個選項（用空格隔開，例如：火鍋 壽司 滷肉飯）: ").split()
    if len(options) < 3:
        print("選項太少啦，幫你隨機決定要不要出門：")
        decision = random.choice(["紅燈：待在家", "綠燈：出門走走", "黃燈：再想五分鐘"])
        print(decision)
    else:
        print(f"根據機率運算，推薦你吃：{random.choice(options)}")

# 主程式迴圈
while True:
    print("\n===== 智慧生活工具箱 =====")
    print("1. 健康檢查")
    print("2. 隨機決策")
    print("3. 退出程式")
    choice = input("請選擇功能 (1/2/3): ")
    
    if choice == '1':
        health_check()
    elif choice == '2':
        random_decision()
    elif choice == '3':
        print("感謝使用，再見！")
        break
    else:
        print("輸入錯誤，請重新選擇。")