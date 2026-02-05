"""
檔名：Smart_Logistics_Matrix_System.py
功能：基礎 Python 練習
學習重點：語法熟悉與邏輯實作
"""
import random

class LogisticsAnalytics:
    def __init__(self, warehouse_id, rows=3, cols=4):
        self.wid = warehouse_id
        self.inventory = [[random.randint(1, 50) for _ in range(cols)] for _ in range(rows)]

    def display_inventory(self, label="庫存狀態"):
        col_count = len(self.inventory[0])
        # 重新精算：每個欄位鎖定 10 格寬
        cell_w = 10
        label_w = 8
        line_len = label_w + (col_count * (cell_w + 1))
        
        # 標題獨立出來，不干擾邊框
        print(f"\n📢 [數據源]: {self.wid} | {label}")
        
        # 繪製頂部邊框
        print("┌" + "─" * (label_w - 1) + ("┬" + "─" * cell_w) * col_count + "┐")
        
        # 繪製表頭 (用簡單的空格與 | 確保絕對對齊)
        header = f"│{'ID':^7}"
        for i in range(col_count):
            header += f"│  Col {i:<2}  "
        print(header + "│")
        
        # 繪製中隔線
        print("├" + "─" * (label_w - 1) + ("┼" + "─" * cell_w) * col_count + "┤")
        
        # 繪製數據列
        for i, row in enumerate(self.inventory):
            row_str = f"│ Row {i:<2} "
            for val in row:
                row_str += f"│ {val:^8} "
            print(row_str + "│")
            
            if i < len(self.inventory) - 1:
                print("├" + "─" * (label_w - 1) + ("┼" + "─" * cell_w) * col_count + "┤")
        
        # 繪製底部
        print("└" + "─" * (label_w - 1) + ("┴" + "─" * cell_w) * col_count + "┘")

def run_demo():
    print("\n" + " ✨ 跨區域庫存同步系統 (100% 對齊修正版) ".center(50, "="))
    
    wh_north = LogisticsAnalytics("Taipei_North")
    wh_south = LogisticsAnalytics("Taipei_South")
    
    wh_north.display_inventory("分區數據 A")
    wh_south.display_inventory("分區數據 B")
    
    print(f"\n[系統動作] 執行矩陣加法：[A] + [B] ...")
    
    rows, cols = len(wh_north.inventory), len(wh_north.inventory[0])
    merged_data = [[wh_north.inventory[r][c] + wh_south.inventory[r][c] for c in range(cols)] for r in range(rows)]
    
    wh_total = LogisticsAnalytics("GLOBAL_TOTAL")
    wh_total.inventory = merged_data
    wh_total.display_inventory("跨區域同步總計報表")

if __name__ == "__main__":
    run_demo()