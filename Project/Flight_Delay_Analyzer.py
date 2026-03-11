"""
檔名：Flight_Delay_Analyzer.py
功能：模擬台灣國內航班誤點資料，分析各航線與時段的誤點趨勢並找出嚴重誤點航班
技術亮點：NumPy 隨機資料模擬、Pandas groupby 多維聚合、clip 處理異常值、apply lambda 格式化輸出
"""

import pandas as pd
import numpy as np

np.random.seed(42)

# 模擬200筆航班資料
airlines = ["CI", "BR", "AE", "B7", "IT"]  # 中華、長榮、華信、立榮、虎航
routes = ["TPE-KHH", "TPE-TNN", "TPE-RMQ", "TPE-HUN", "TPE-TTT"]
time_slots = ["清晨(06-09)", "上午(09-12)", "下午(12-18)", "晚間(18-21)", "深夜(21-24)"]

data = {
    "航班號": [
        f"{np.random.choice(airlines)}{np.random.randint(100, 999)}" for _ in range(200)
    ],
    "航線": np.random.choice(routes, 200),
    "時段": np.random.choice(time_slots, 200),
    "誤點分鐘": np.random.randint(-5, 120, 200),  # 負數代表提早
}

df = pd.DataFrame(data)

# 負數誤點視為準時（0分鐘）
df["誤點分鐘"] = df["誤點分鐘"].clip(lower=0)

print(f"原始資料（前5筆）：\n{df.head()}\n")

# 各航線平均誤點分鐘
print("各航線平均誤點分鐘：")
route_avg = df.groupby("航線")["誤點分鐘"].mean().sort_values(ascending=False)
print(route_avg.apply(lambda x: f"{x:.1f} 分鐘"), "\n")

# 誤點最嚴重的航線
worst_route = route_avg.idxmax()
print(f"誤點最嚴重的航線：{worst_route}（平均 {route_avg.max():.1f} 分鐘）\n")

# 各時段誤點統計
print("各時段誤點次數：")
slot_count = (
    df[df["誤點分鐘"] > 0]
    .groupby("時段")["誤點分鐘"]
    .count()
    .sort_values(ascending=False)
)
print(slot_count, "\n")

# 嚴重誤點（超過60分鐘）
serious = df[df["誤點分鐘"] > 60]
print(f"嚴重誤點航班（超過60分鐘，共{len(serious)}筆）：")
print(serious.sort_values("誤點分鐘", ascending=False).head(10))
