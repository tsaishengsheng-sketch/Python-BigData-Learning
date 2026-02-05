# 🐍 我的 Python 學習筆記
> **新手村修練紀錄**：跟著蔡明志老師的《Python大數據》一步步學習程式邏輯。

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
![Format](https://img.shields.io/badge/Format-Jupyter_Notebook-orange?style=flat-square&logo=jupyter)

## 🌟 階段性小成果
* **[Smart_Logistics_Matrix_System.py](./multidimensional_list/Smart_Logistics_Matrix_System.py)**：**【重點】** 實作 100% 視覺化對齊報表，整合跨區庫存同步 (A+B=Total) 與物流路徑壓力分析。
* **[RealEstate_Investment_Analyzer.py](./variable_constant/RealEstate_Investment_Analyzer.py)**：**【重點】** 整合數位校驗、三角地產估價與房貸利息壓測，揭示 40 年房貸高達 71% 的資金成本。
* **[SmartLife_Toolbox.py](./if_else/SmartLife_Toolbox.py)**：整合 if-else 邏輯，包含 BMI、星座與閏年查詢。
* **[Loop_Practice_Tool.py](./loop/Loop_Practice_Tool.py)**：整合 25+ 迴圈練習，含九九乘法、質數分析與排序演算法。
* **[Smart_Award_System.py](./function/Smart_Award_System.py)**：整合 Function 模組化練習，實作具備安全驗證與門檻判定的評選系統。
* **[Smart_Inventory_System.py](./list/Smart_Inventory_System.py)**：整合 List 演算法，實作具備排序與二分搜尋功能的電商庫存管理系統。
* **[自動標註腳本](./utils/add_docstrings.py)**：自動化處理檔案說明，提升歸檔效率。

---

## 📂 專案導覽
**「.py 執行檔 + .ipynb 預覽檔」** 雙軌制，兼顧自動化處理與 GitHub 直接閱讀體驗：
| 單元目錄 | 內容說明 | 核心實作重點 | 狀態 |
| :--- | :--- | :--- | :--- |
| [📐 Variable Constant](./variable_constant/) | **地產投資分析器** | 數位拆解、財務複利、三角估價 | ✅ 完成 |
| [🔀 If-Else Logic](./if_else/) | **智慧生活工具箱** | 條件分歧、防呆機制、邏輯判定 | ✅ 完成 |
| [🔁 Loop Practice](./loop/) | **多功能迴圈工具** | 規律生成、質數判定、排序基礎 | ✅ 完成 |
| [📦 List Algorithm](./list/) | **電商大數據中心** | 串列操作、搜尋與排序演算法 | ✅ 完成 |
| [📦 Function Module](./function/) | **智慧年度評選系統** | 封裝邏輯、參數傳遞、系統整合 | ✅ 完成 |
| [📊 Multidimensional](./multidimensional_list/) | **智慧物流分析系統** | 矩陣同步、路徑優化、視覺化報表 | ✅ 完成 |
---

## 🛠️ 開發環境
- **Hardware**: macOS MacBook Air (M2)
- **Editor**: VS Code
- **Version Control**: Git / GitHub
---

## 🚀 快速開始

###  複製專案

```bash
### 1. 複製專案並進入資料夾
git clone https://github.com/tsaishengsheng-sketch/Python-BigData-Learning.git

### 2. 建立並啟動虛擬環境
python3 -m venv venv && source venv/bin/activate  # macOS/Linux

### 3. 安裝依賴套件
pip install --upgrade pip
pip install -r requirements.txt

```
- ## 📂 專案結構
```text
.
├── variable_constant/        # 📐 基礎變數運算與地產投資分析
│   ├── RealEstate_Investment_Analyzer.py  # 🏆 核心作品
│   └── learning/                          # 📚 練習題歸檔
├── if_else/                  # 🔀 邏輯判定與智慧生活工具
│   ├── SmartLife_Toolbox.py               # 🏆 核心作品
│   └── learning/                          # 📚 練習題歸檔
├── loop/                     # 🔁 迴圈控制與多功能工具
│   ├── Loop_Practice_Tool.py              # 🏆 核心作品
│   └── learning/                          # 📚 練習題歸檔
├── function/                 # 📦 函式模組化與年度評選系統
│   ├── Smart_Award_System.py              # 🏆 核心作品
│   └── learning/                          # 📚 練習題歸檔
├── list/                     # 📊 串列演算法與庫存管理系統
│   ├── Smart_Inventory_System.py          # 🏆 核心作品
│   └── learning/                          # 📚 練習題歸檔
├── multidimensional_list/    # 🧬 多維矩陣運算與物流分析系統 (New)
│   ├── Smart_Logistics_Matrix_System.py   # 🏆 核心作品
│   └── learning/                          # 📚 練習題歸檔
├── utils/                    # 🛠️ 專案輔助工具 (自動標註腳本)
└── README.md                 # 🗺️ 專案總覽導覽