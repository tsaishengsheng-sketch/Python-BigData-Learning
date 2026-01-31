# 🐍 Python Big Data Learning
> **課程實作紀錄**：蔡明志老師《Python大數據》練習題彙整

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
![Format](https://img.shields.io/badge/Format-Jupyter_Notebook-orange?style=flat-square&logo=jupyter)

## 📂 專案導覽
本專案已完成全英文命名重構，並全面轉化為 **Jupyter Notebook (.ipynb)** 格式，提供更佳的語法高亮與執行結果展示：

| 單元目錄 | 內容說明 | 關鍵技術 |
| :--- | :--- | :--- |
| **[Logic](./if_else)** | 選擇結構與條件分支 | 邏輯判斷、例外處理 |
| **[Loops](./loop)** | 迭代結構與演算法 | 質數搜尋、排序演算法 |
| **[Functions](./function)** | 程式模組化與封裝 | 函式定義、參數傳遞 |
| **[Data Structures](./list)** | 串列與進階排序 | 氣泡排序、二元搜尋 |
| **[Basics](./variable_constant)** | 基礎運算與幾何 | 變數運算、幾何公式 |

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
cd Python-BigData-Learning

### 2. 建立並啟動虛擬環境
python3 -m venv venv
source venv/bin/activate  # macOS/Linux


### 3. 安裝依賴套件
pip install --upgrade pip
pip install -r requirements.txt

### 4. 自動化工具使用 (可選)
# 幫練習題加上標註並同步轉檔為 Notebook
python3 utils/add_docstrings.py
jupytext --to notebook */*.py
```


- ## 📂 專案結構
```text
.
├── function/            # 16 個函式練習 (互動式筆記本)
├── if_else/             # 14 個邏輯判斷練習 (互動式筆記本)
├── list/                # 14 個演算法與資料結構練習
├── loop/                # 25 個迴圈控制練習 (排序、質數搜尋等)
├── variable_constant/   # 5 個基礎運算練習
├── utils/               # 專案輔助工具
├── LICENSE              # MIT 開源授權書
├── README.md            # 專案說明文件
└── requirements.txt     # 套件依賴清單 
```