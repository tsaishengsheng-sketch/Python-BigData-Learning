# 🐍 我的 Python 學習筆記
> **新手村修練紀錄**：《Python程式設計大數據資料分析》一步步學習程式邏輯。

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
![Format](https://img.shields.io/badge/Format-Jupyter_Notebook-orange?style=flat-square&logo=jupyter)

---

## 📂 專案導覽 (Navigation)
我將學習歷程分為「基礎實驗室」與「實戰作品集」兩大入口：

| 類別 | 內容說明 |
| :--- | :--- |
| **🏆 [Featured Projects](./Project/)** | 延伸模組化開發作品 |
| **📚 [Learning Labs](./Learning/)** | 章節基礎練習 |

---

## 🏆 實戰作品亮點 (Featured Projects)
1. **[Smart_Security_Access_System](./Project/Smart_Security_Access_System.py)**：整合 Set 權限過濾與 Dict 通行紀錄系統。
2. **[Cloud_Finance_Manager](./Project/Cloud_Finance_Manager.py)**：實作三層架構設計與 `pickle` 資料持久化。
3. **[Smart_Inventory_System](./Project/Smart_Inventory_System.py)**：運用二分搜尋與氣泡排序優化檢索效率。
4. **[Smart_Logistics_Matrix](./Project/Smart_Logistics_Matrix_System.py)**：物件導向處理二維矩陣運算與視覺化報表。
5. **[RealEstate_Investment_Analyzer](./Project/RealEstate_Investment_Analyzer.py)**：整合科學運算實作土地估價與房貸財務模型。
6. **[Smart_Award_System](./Project/Smart_Award_System.py)**：結合隨機驗證碼機制與多層級業務邏輯判定。
7. **[Loop_Practice_Tool](./Project/Loop_Practice_Tool.py)**：整合質數分析、選擇排序與規律生成工具。
8. **[SmartLife_Toolbox](./Project/SmartLife_Toolbox.py)**：結合 BMI 診斷邏輯與隨機決策系統的生活應用。

---


## 🛠️ 開發環境
- **Hardware**: macOS MacBook Air (M2)
- **Editor**: VS Code
- **Version Control**: Git / GitHub(紀錄所有從錯誤到修正的真實開發歷程)
---

## 🚀 快速開始

```bash
git clone https://github.com/tsaishengsheng-sketch/Python-BigData-Learning.git

cd Python-BigData-Learning

python3 -m venv venv && source venv/bin/activate

pip install -r requirements.txt

```
---
## 📂 專案結構
```text
.
├── Project/            # 🏆 核心實戰作品 (手動維護專業註解)
├── Learning/           # 📚 各章節基礎練習 (自動標註腳本管理)
│   ├── ...
│   ├── OOP # 🎯 正在進行中
├── utils/              # 🛠️ 專案輔助工具 (add_docstrings.py)
└── .gitignore          # 🛡️ 檔案排除規則

---
## 📝 Git 提交規範 (Commit Message Convention)

為了保持開發紀錄整潔，本專案採用以下標籤開頭：

| 標籤 | 說明 | 範例 |
| :--- | :--- | :--- |
| feat: | 新增功能 / 檔案 | feat: add Circle class |
| fix: | 修復錯誤 / 邏輯 | fix: correct matrix sum logic |
| docs: | 文件更新 / 備註 | docs: update README conventions |
| style: | 格式調整 (不影響邏輯) | style: fix indentation |
| refactor: | 程式碼重構 | refactor: simplify loop structure |
| chore: | 雜務 (工具、設定) | chore: update .gitignore |