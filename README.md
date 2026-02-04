# 🐍 我的 Python 學習筆記
> **新手村修練紀錄**：跟著蔡明志老師的《Python大數據》一步步學習程式邏輯。

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
![Format](https://img.shields.io/badge/Format-Jupyter_Notebook-orange?style=flat-square&logo=jupyter)

## 🌟 階段性小成果
* **[SmartLife_Toolbox.py](./if_else/SmartLife_Toolbox.py)**：整合 if-else 邏輯，包含 BMI、星座與閏年查詢。
* **[Loop_Practice_Tool.py](./loop/Loop_Practice_Tool.py)**：整合 25+ 迴圈練習，含九九乘法、質數分析與排序演算法。
* **[Smart_Award_System.py](./function/Smart_Award_System.py)**：**【New】** 整合 Function 模組化練習，實作具備安全驗證與門檻判定的年度評選系統。
* **[自動標註腳本](./utils/add_docstrings.py)**：自動化處理檔案說明，提升歸檔效率。

---

## 📂 專案導覽
專案採 **「.py 執行檔 + .ipynb 預覽檔」** 雙軌制，兼顧自動化處理與 GitHub 直接閱讀體驗：

| 單元目錄 | 內容說明 | 核心實作重點 |
| :--- | :--- | :--- |
| **[Logic](./if_else)** | 邏輯判定與歸檔 | 條件分支、SmartLife 整合工具 |
| **[Loops](./loop)** | 迭代結構 | 質數搜尋、選擇排序、Loop 整合工具 |
| **[Functions](./function)** | 程式模組化 | **安全驗證、權限控管、幾何與統計模組整合** |
| **[Multi-List](./multidimensional_list)** | 多維串列應用 | 矩陣運算、巢狀迴圈、資料表格 |
| **[Data Structures](./list)** | 資料結構 | 氣泡排序、二元搜尋 |
| **[Basics](./variable_constant)** | 基礎運算 | 變數處理、幾何公式計算 |

---

## 🛠️ 開發環境
- **Hardware**: macOS MacBook Air (M2)
- **Editor**: VS Code
- **Version Control**: Git / GitHub(這是我學最久的地方 😂)
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

### 4. 自動化工具使用 (可選)
# 針對歸檔資料夾進行轉檔
python3 utils/add_docstrings.py
jupytext --to notebook **/learning/*.py
```


- ## 📂 專案結構
```text
.
├── if_else/             
│   ├── SmartLife_Toolbox.py  # 🏆 邏輯整合作品
│   └── learning/             # 📚 練習題歸檔 (ipynb)
├── loop/                
│   ├── Loop_Practice_Tool.py # 🏆 迴圈整合作品
│   └── learning/             # 📚 練習題歸檔 (ipynb)
├── function/                
│   ├── Smart_Award_System.py # 🏆 函式整合作品 (年度評選系統)
│   └── learning/             # 📚 練習題歸檔 (ipynb)
├── list/                    # 演算法與資料結構練習 (排序、搜尋)
├── multidimensional_list/    # 多維串列與矩陣練習
├── variable_constant/        # 基礎變數運算練習
├── utils/                   # 🛠️ 專案輔助工具 (自動標註腳本)
└── README.md