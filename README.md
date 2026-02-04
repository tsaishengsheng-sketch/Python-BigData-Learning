# 🐍 Python Big Data Learning
> **從基礎邏輯到大數據開發**：蔡明志老師《Python大數據》實作紀錄與專案整合。

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
![Format](https://img.shields.io/badge/Format-Jupyter_Notebook-orange?style=flat-square&logo=jupyter)

## 🌟 亮點作品：SmartLife Toolbox
本專案不只是練習題，更將零散的邏輯整合為具備實務價值的工具：
* **[SmartLife_Toolbox.py](./if_else/SmartLife_Toolbox.py)**：整合 BMI 診斷、星座運勢、閏年判定等多項邏輯的 CLI 互動工具。
* **[add_docstrings.py](./utils/add_docstrings.py)**：自主開發的自動化腳本，一鍵為大量程式碼加上標準標註與功能說明。

---

## 📂 專案導覽
專案採 **「.py 執行檔 + .ipynb 預覽檔」** 雙軌制，兼顧自動化處理與 GitHub 直接閱讀體驗：

| 單元目錄 | 內容說明 | 核心技術展示 |
| :--- | :--- | :--- |
| **[Logic](./if_else)** | 邏輯判定與歸檔 | 條件分支、SmartLife 整合工具 |
| **[Multi-List](./multidimensional_list)** | 多維串列應用 | 矩陣運算、巢狀迴圈、資料表格 |
| **[Loops](./loop)** | 迭代結構 | 質數搜尋、排序演算法 |
| **[Functions](./function)** | 程式模組化 | 函式定義、參數傳遞 |
| **[Data Structures](./list)** | 資料結構 | 氣泡排序、二元搜尋 |
| **[Basics](./variable_constant)** | 基礎運算 | 變數處理、幾何公式計算 |

---

## 🛠️ 開發環境
- **Hardware**: macOS MacBook Air (M series)
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

### 4. 自動化工具使用 (可選)
# 針對歸檔資料夾進行轉檔
python3 utils/add_docstrings.py
jupytext --to notebook **/learning/*.py
```


- ## 📂 專案結構
```text
.
├── if_else/             
│   ├── SmartLife_Toolbox.py  # 🏆 核心整合專案
│   └── learning/             # 📚 邏輯練習題歸檔 (ipynb)
├── function/                # 函式模組化練習
├── list/                    # 演算法與資料結構練習
├── loop/                    # 迴圈控制練習
├── multidimensional_list/    # 多維串列與矩陣練習
├── variable_constant/        # 基礎變數運算練習
├── utils/                   # 🛠️ 專案開發輔助工具 (自動標註腳本)
└── README.md
```


