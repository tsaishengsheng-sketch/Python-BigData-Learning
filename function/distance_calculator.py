"""
檔名：distance_calculator.py
功能：函式封裝練習
學習重點：參數傳遞、Return 回傳值應用
"""
import math 

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def main():
    while True:
        try:
            user_input = input('輸入 x1, y1, x2, y2 (或輸入 0 結束): ')
            if user_input == '0':
                break
                
            # eval 拆解輸入四個值
            x1, y1, x2, y2 = eval(user_input)
            
            d = distance(x1, y1, x2, y2)
            
            # 格式化輸出說明：
            # (x1, y1) 與 (x2, y2) 用來呈現座標
            # {d:.2f} 用來呈現距離並取小數點後兩位
            print(f"點 ({x1}, {y1}) 到 點 ({x2}, {y2}) 的距離是: {d:.2f}")
            print("-" * 30) # 分隔線
            
        except:
            print("輸入格式錯誤，請確保輸入四個數字並用逗號隔開（例如：1,2,4,6）")

main()