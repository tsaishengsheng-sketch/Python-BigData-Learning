# 📦 Data Structures (串列與演算法實戰)
學習如何處理大量數據儲存，並實作經典的資料搜尋與排序演算法。

### 📝 學習重點
* **資料操作基礎**：清單生成、隨機取樣（Lotto 邏輯）、不重複資料檢核。
* **排序演算法 (Sorting)**：實作 **Bubble Sort** 與 **Selection Sort**，並紀錄排序過程以理解 $O(n^2)$ 複雜度。
* **高效搜尋 (Searching)**：理解線性搜尋與 **Binary Search** 的效能差異。
* **數據統計分析**：計算平均值、最大值、頻率分析，並應用於等級判定 (Grading)。

---

### 🌟 綜合實作專案：智慧電商大數據管理中心 (Smart Inventory System)
將 15+ 個演算法練習題，整合為一套模擬電商後台的數據分析系統。




#### 🔧 系統整合邏輯：
1. **數據庫初始化 (Lotto/Random)**：模擬生成不重複的商品 ID 與隨機價格庫存。
2. **庫存狀態判定 (Grading/Status)**：根據價格區間自動計算商品等級（如：奢華、平價、出清）。
3. **營運報表生成 (Frequency/Mean)**：分析所有庫存價格的平均值，並統計各價位區間的商品分佈頻率。
4. **高效倉儲檢索 (Sort/Binary Search)**：
   - 使用 **Selection/Bubble Sort** 完成 ID 排序。
   - 排序後提供客戶端使用 **Binary Search** 進行快速查價。

---

### 📂 檔案結構
* **核心整合**：[`Smart_Inventory_System.py`](./Smart_Inventory_System.py.py) - 核心作品，展示排序與搜尋的連鎖應用。
* **歸檔練習**：位於 [`learning/`](./learning/) 基礎練習歸檔，包含排序過程紀錄、頻率統計、樂透模擬等