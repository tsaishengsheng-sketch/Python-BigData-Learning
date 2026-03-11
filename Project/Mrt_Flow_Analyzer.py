"""
檔名：MRT_Flow_Analyzer.py
功能：台北捷運五路線人流視覺化分析系統，模擬各站平日／週末人次，產出多種統計圖表
技術亮點：NumPy 隨機模擬與尖峰乘數設計、Pandas groupby 多維聚合、Matplotlib 長條圖／折線圖／圓餅圖整合輸出
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 設定中文字型（Mac 內建）
plt.rcParams["font.family"] = "Arial Unicode MS"

np.random.seed(42)

# ── 基本設定 ──────────────────────────────────────────
LINES = {
    "淡水信義線": [
        "淡水",
        "紅樹林",
        "竹圍",
        "關渡",
        "忠義",
        "復興崗",
        "北投",
        "新北投",
        "奇岩",
        "唭哩岸",
        "石牌",
        "明德",
        "芝山",
        "士林",
        "劍潭",
        "圓山",
        "民權西路",
        "中山",
        "台大醫院",
        "台北車站",
        "善導寺",
        "忠孝新生",
        "大安森林公園",
        "大安",
        "信義安和",
        "台北101",
        "象山",
    ],
    "新莊蘆洲線": [
        "蘆洲",
        "三民高中",
        "鷺洲",
        "三重國小",
        "三重",
        "菜寮",
        "台北橋",
        "大橋頭",
        "民權西路",
        "中山國小",
        "行天宮",
        "松江南京",
        "忠孝新生",
        "古亭",
        "台電大樓",
        "公館",
        "萬隆",
        "景美",
        "大坪林",
        "新店區公所",
        "新店",
    ],
    "松山新店線": [
        "松山",
        "南京三民",
        "台北小巨蛋",
        "南京復興",
        "忠孝復興",
        "大安",
        "科技大樓",
        "六張犁",
        "麟光",
        "辛亥",
        "萬芳醫院",
        "萬芳社區",
        "木柵",
        "動物園",
    ],
    "中和新蘆線": [
        "南勢角",
        "景安",
        "中和",
        "永安市場",
        "頂溪",
        "古亭",
        "東門",
        "忠孝新生",
        "松江南京",
        "行天宮",
        "中山國小",
        "民權西路",
        "大橋頭",
        "台北橋",
        "菜寮",
        "三重",
        "三重國小",
        "鷺洲",
        "三民高中",
        "蘆洲",
    ],
    "文湖線": [
        "動物園",
        "木柵",
        "萬芳社區",
        "萬芳醫院",
        "辛亥",
        "麟光",
        "六張犁",
        "科技大樓",
        "大安",
        "忠孝復興",
        "南京復興",
        "台北小巨蛋",
        "南京三民",
        "松山",
        "中山國中",
        "大直",
        "劍南路",
        "西湖",
        "港墘",
        "文德",
        "內湖",
        "大湖公園",
        "葫洲",
        "東湖",
        "南港軟體園區",
        "南港展覽館",
    ],
}

HOURS = list(range(6, 24))  # 營運時間 06:00 ~ 23:00


# ── 產生各站每小時人流資料 ────────────────────────────
def generate_station_flow(station_name, is_weekend=False):
    """模擬單站一天各時段人流（尖峰時段會特別高）"""
    base = np.random.randint(500, 3000)
    flow = []
    for h in HOURS:
        if not is_weekend and h in [8, 9]:  # 早尖峰
            multiplier = np.random.uniform(3.0, 5.0)
        elif not is_weekend and h in [18, 19]:  # 晚尖峰
            multiplier = np.random.uniform(2.5, 4.5)
        elif h in [12, 13]:  # 午休
            multiplier = np.random.uniform(1.5, 2.5)
        elif is_weekend and h in [13, 14, 15]:  # 週末下午
            multiplier = np.random.uniform(2.0, 3.5)
        elif h in [6, 23]:  # 首末班
            multiplier = np.random.uniform(0.2, 0.5)
        else:
            multiplier = np.random.uniform(0.8, 1.5)
        flow.append(int(base * multiplier))
    return flow


# 建立平日和週末資料
records = []
for line, stations in LINES.items():
    for station in stations:
        for is_weekend in [False, True]:
            flow = generate_station_flow(station, is_weekend)
            for i, h in enumerate(HOURS):
                records.append(
                    {
                        "路線": line,
                        "站名": station,
                        "時段": h,
                        "人次": flow[i],
                        "類型": "週末" if is_weekend else "平日",
                    }
                )

df = pd.DataFrame(records)

# ── 圖1：各路線平日總人流長條圖 ──────────────────────
line_total = (
    df[df["類型"] == "平日"].groupby("路線")["人次"].sum().sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))
colors = ["#E63946", "#457B9D", "#2A9D8F", "#E9C46A", "#F4A261"]
plt.bar(line_total.index, line_total.values / 10000, color=colors)
plt.title("台北捷運各路線平日總人流")
plt.xlabel("路線")
plt.ylabel("總人次（萬人）")
for i, v in enumerate(line_total.values):
    plt.text(i, v / 10000 + 0.5, f"{v / 10000:.0f}萬", ha="center", fontsize=9)
plt.tight_layout()
plt.show()

# ── 圖2：平日 vs 週末 各路線人流比較 ─────────────────
pivot = df.groupby(["路線", "類型"])["人次"].sum().unstack()
x = np.arange(len(pivot.index))
width = 0.35

plt.figure(figsize=(10, 5))
plt.bar(x - width / 2, pivot["平日"] / 10000, width, label="平日", color="#457B9D")
plt.bar(x + width / 2, pivot["週末"] / 10000, width, label="週末", color="#F4A261")
plt.title("台北捷運平日 vs 週末各路線人流比較")
plt.xlabel("路線")
plt.ylabel("總人次（萬人）")
plt.xticks(x, pivot.index, fontsize=9)
plt.legend()
plt.tight_layout()
plt.show()

# ── 圖3：台北車站 一天24小時人流折線圖 ──────────────
key_stations = ["台北車站", "忠孝復興", "西門"]
station_df = df[(df["站名"].isin(key_stations)) & (df["類型"] == "平日")]

plt.figure(figsize=(10, 5))
line_colors = ["#E63946", "#457B9D", "#2A9D8F"]
for i, station in enumerate(key_stations):
    s_data = station_df[station_df["站名"] == station].groupby("時段")["人次"].sum()
    plt.plot(
        s_data.index,
        s_data.values / 1000,
        "-o",
        label=station,
        color=line_colors[i],
        linewidth=2,
        markersize=5,
    )

plt.title("主要車站平日各時段人流")
plt.xlabel("時段")
plt.ylabel("人次（千人）")
plt.xticks(HOURS, [f"{h}時" for h in HOURS], rotation=45, fontsize=8)
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# ── 圖4：各路線尖峰 vs 離峰人流圓餅圖 ───────────────
peak_hours = [8, 9, 18, 19]
peak_df = df[(df["類型"] == "平日") & (df["時段"].isin(peak_hours))]
offpeak_df = df[(df["類型"] == "平日") & (~df["時段"].isin(peak_hours))]

peak_total = peak_df["人次"].sum()
offpeak_total = offpeak_df["人次"].sum()

plt.figure(figsize=(6, 6))
plt.pie(
    [peak_total, offpeak_total],
    labels=["尖峰時段\n(08-09, 18-19時)", "離峰時段"],
    autopct="%1.1f%%",
    colors=["#E63946", "#A8DADC"],
    explode=[0.05, 0],
    startangle=90,
)
plt.title("台北捷運平日尖峰 vs 離峰人流佔比")
plt.tight_layout()
plt.show()

print("\n📊 統計摘要：")
print(f"總站數：{df['站名'].nunique()} 站")
print(f"平日全網總人次：{df[df['類型'] == '平日']['人次'].sum():,}")
print(f"週末全網總人次：{df[df['類型'] == '週末']['人次'].sum():,}")
top5 = (
    df[df["類型"] == "平日"]
    .groupby("站名")["人次"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(f"\n平日人流前5名車站：")
for station, count in top5.items():
    print(f"  {station}：{count:,} 人次")
