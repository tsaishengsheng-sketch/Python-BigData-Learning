def bmi(wei,hei):
    heiM = hei /100
    bmi = wei / (heiM ** 2)
    print(f"{bmi:.2f}")

    if bmi < 18.5:
        print('過瘦')
    elif bmi < 25:
        print('正常')
    elif bmi < 30:
        print('過胖')
    else:
        print('危險')
def main():

    print("--- BMI 計算器 (輸入 0 或 stop 結束) ---")
while True:  # 開啟無窮迴圈
        user_input = input('\n請輸入體重 (kg) 或輸入 stop 離開：').lower()
        
        # 檢查是否輸入 stop 或 0
        if user_input == 'stop' or user_input == '0':
            print("程式結束，再見！")
            break  # 跳出 while 迴圈
            
        try:
            wei = float(user_input)
            hei = float(input('請輸入身高 (cm)：'))
            
            bmi(wei, hei)
            
        except ValueError:
            print("錯誤：請輸入正確的數字或 'stop'")

main()