"""
檔名：Job_Radar_104.py
功能：網頁資料擷取練習
學習重點：requests、BeautifulSoup、urllib3 網頁爬取與解析
"""

import requests
from collections import Counter

SKILL_KEYWORDS = [
    "Python",
    "Java",
    "JavaScript",
    "TypeScript",
    "C++",
    "C#",
    "Go",
    "Rust",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Redis",
    "Django",
    "Flask",
    "FastAPI",
    "React",
    "Vue",
    "Node.js",
    "AWS",
    "GCP",
    "Azure",
    "Docker",
    "Kubernetes",
    "Linux",
    "Git",
    "CI/CD",
    "Agile",
    "Scrum",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Tableau",
    "Power BI",
    "Excel",
    "R語言",
    "MATLAB",
]

AREA_OPTIONS = {
    "1": ("台北市", "6001001000"),
    "2": ("新北市", "6001002000"),
    "3": ("桃園市", "6001003000"),
    "4": ("台中市", "6001005000"),
    "5": ("台南市", "6001007000"),
    "6": ("高雄市", "6001008000"),
    "7": ("新竹縣市", "6001004000"),
    "0": ("不限", None),
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Referer": "https://www.104.com.tw/",
}


# =============================
# 互動式輸入
# =============================
def get_user_input():
    print("=" * 60)
    print("  104 職缺雷達")
    print("=" * 60)

    keyword = input("\n搜尋關鍵字（例如：Python、資料分析）：").strip()
    if not keyword:
        keyword = "Python"

    print("\n地區篩選：")
    for k, (name, _) in AREA_OPTIONS.items():
        print(f"  {k}. {name}")
    area_choice = input("請選擇地區（輸入數字，預設 0 不限）：").strip()
    if area_choice not in AREA_OPTIONS:
        print("  （輸入無效，自動設為不限）")
        area_choice = "0"
    area_name, area_code = AREA_OPTIONS[area_choice]
    print(f"  → 地區：{area_name}")

    remote = input("\n只看遠端/混合辦公職缺？(y/n，預設 n)：").strip().lower()
    remote_only = remote == "y"

    pages = input("\n爬取頁數（每頁 32 筆，預設 3）：").strip()
    max_pages = int(pages) if pages.isdigit() and int(pages) > 0 else 3

    return keyword, area_name, area_code, remote_only, max_pages


# =============================
# 爬取職缺
# =============================
def fetch_jobs(keyword, max_pages, area_code=None, remote_only=False):
    jobs = []
    print()
    for page in range(1, max_pages + 1):
        url = (
            "https://www.104.com.tw/jobs/search/api/jobs"
            f"?keyword={keyword}&order=15&asc=0&page={page}&mode=s&jobsource=2018indexpoc"
        )
        if area_code:
            url += f"&area={area_code}"
        if remote_only:
            url += "&remoteWork=1"

        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            print(f"  第 {page} 頁請求失敗（狀態碼 {r.status_code}）")
            break
        data = r.json()
        job_list = data.get("data", [])
        if not job_list:
            break
        jobs.extend(job_list)
        print(f"  第 {page} 頁：取得 {len(job_list)} 筆")
    return jobs


# =============================
# 薪資解析
# =============================
def parse_salary(job):
    low = job.get("salaryLow", 0)
    high = job.get("salaryHigh", 0)
    if low == 0 and high == 0:
        return None
    if high >= 9999999:
        high = 0
    avg = (low + high) // 2 if high > 0 else low
    if avg > 500000:  # 年薪換算月薪
        avg = avg // 12
    if avg < 15000:  # 過濾異常值
        return None
    return avg


def format_salary(job):
    low = job.get("salaryLow", 0)
    high = job.get("salaryHigh", 0)
    if low == 0 and high == 0:
        return "面議"
    if high >= 9999999:
        return f"{low:,} 以上"
    if high > 0:
        return f"{low:,} ~ {high:,}"
    return f"{low:,}"


# =============================
# 主程式
# =============================
keyword, area_name, area_code, remote_only, max_pages = get_user_input()

print(f"\n正在搜尋「{keyword}」", end="")
if area_name != "不限":
    print(f"（{area_name}）", end="")
if remote_only:
    print("（遠端/混合）", end="")
print("...")

jobs = fetch_jobs(keyword, max_pages, area_code, remote_only)

print(f"\n共取得 {len(jobs)} 筆職缺")

if not jobs:
    print("未取得任何職缺，請確認網路連線或關鍵字。")
    exit()

TOP_N = 10

# =============================
# 統計一：熱門公司
# =============================
company_counter = Counter()
for job in jobs:
    company = job.get("custName", "")
    if company:
        company_counter[company] += 1

print(f"\n【熱門公司 Top {TOP_N}】")
print("-" * 45)
for i, (company, count) in enumerate(company_counter.most_common(TOP_N), 1):
    print(f"  {i:>2}. {company:<28} {count} 筆")

# =============================
# 統計二：熱門技能
# =============================
skill_counter = Counter()
for job in jobs:
    job_name = job.get("jobName", "")
    tags = job.get("tags", {})
    tag_text = " ".join(str(v) for v in tags.values()) if isinstance(tags, dict) else ""
    desc = job.get("description", "")
    text = (job_name + " " + tag_text + " " + desc).lower()
    for skill in SKILL_KEYWORDS:
        if skill.lower() in text:
            skill_counter[skill] += 1

print(f"\n【熱門技能 Top {TOP_N}】")
print("-" * 45)
for i, (skill, count) in enumerate(skill_counter.most_common(TOP_N), 1):
    bar = "█" * min(count, 35)
    print(f"  {i:>2}. {skill:<20} {count:>3} 筆  {bar}")

# =============================
# 統計三：薪資分布
# =============================
salaries = [s for job in jobs for s in [parse_salary(job)] if s]

print(f"\n【薪資分布（月薪，共 {len(salaries)} 筆有效資料）】")
print("-" * 45)

if salaries:
    brackets = [
        (0, 30000, "30k 以下   "),
        (30000, 40000, "30k ~ 40k "),
        (40000, 50000, "40k ~ 50k "),
        (50000, 70000, "50k ~ 70k "),
        (70000, 100000, "70k ~ 100k"),
        (100000, 9999999, "100k 以上  "),
    ]
    for low, high, label in brackets:
        count = sum(1 for s in salaries if low <= s < high)
        bar = "█" * count
        print(f"  {label}  {count:>3} 筆  {bar}")

    print(f"\n  平均月薪：約 {sum(salaries) // len(salaries):,} 元")
    print(f"  最高月薪：約 {max(salaries):,} 元")
    print(f"  最低月薪：約 {min(salaries):,} 元")
else:
    print("  無有效薪資資料")

# =============================
# 統計四：職缺列表
# =============================
show_n = min(10, len(jobs))
print(f"\n【職缺列表（前 {show_n} 筆）】")
print("-" * 60)
for i, job in enumerate(jobs[:show_n], 1):
    title = job.get("jobName", "")
    company = job.get("custName", "")
    salary = format_salary(job)
    area = job.get("jobAddrNoDesc", "")
    url = job.get("link", {}).get("job", "")
    print(f"  {i:>2}. [{company}] {title}")
    print(f"      薪資：{salary}  地點：{area}")
    if url:
        print(f"      連結：{url}")
    print()

print("=" * 60)
print("  分析完成！")
print("=" * 60)
