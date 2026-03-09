"""
檔名：cafe_order_system.py
功能：咖啡廳點餐系統，模擬菜單瀏覽、點餐、結帳流程
技術亮點：
  - 繼承（MenuItem → HotDrink / ColdDrink / Dessert / Snack）
  - 多型（不同品項統一呼叫 getInfo()，各自輸出不同內容）
  - 自訂異常（OutOfStockError）
  - Private 屬性與 getter/setter 封裝
"""

# ============================================================
# 自訂異常類別
# ============================================================


class OutOfStockError(Exception):
    """當點餐的品項已售完時，拋出此異常"""

    pass


# ============================================================
# 父類別：MenuItem
# ============================================================


class MenuItem:
    """菜單品項基底類別，所有品項都有名稱、價格、庫存"""

    def __init__(self, name, price, stock):
        self.__name = name  # 品項名稱（private）
        self.__price = price  # 價格（private）
        self.__stock = stock  # 庫存數量（private）

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getStock(self):
        return self.__stock

    def getStatus(self):
        """回傳庫存狀態文字，子類別的 getInfo() 直接呼叫這個就好"""
        if self.__stock > 0:
            return "供應中"
        return "已售完"

    def reduceStock(self):
        """減少庫存，庫存為零時拋出異常"""
        if self.__stock <= 0:
            raise OutOfStockError(f"「{self.__name}」已售完，無法點餐！")
        self.__stock -= 1

    def getInfo(self):
        """子類別會覆寫這個方法"""
        print(f"  [{self.getStatus()}] {self.__name}  NT${self.__price}")


# ============================================================
# 子類別：各自只加自己獨有的屬性
# ============================================================


class HotDrink(MenuItem):
    """熱飲，加上溫度"""

    def __init__(self, name, price, stock, temp):
        super().__init__(name, price, stock)
        self.__temp = temp

    def getInfo(self):
        print(
            f"  [{self.getStatus()}] ☕ {self.getName()}  NT${self.getPrice()}  (溫度：{self.__temp})"
        )


class ColdDrink(MenuItem):
    """冷飲，加上容量"""

    def __init__(self, name, price, stock, volume):
        super().__init__(name, price, stock)
        self.__volume = volume

    def getInfo(self):
        print(
            f"  [{self.getStatus()}] 🧊 {self.getName()}  NT${self.getPrice()}  ({self.__volume}ml)"
        )


class Dessert(MenuItem):
    """甜點，加上卡路里"""

    def __init__(self, name, price, stock, calories):
        super().__init__(name, price, stock)
        self.__calories = calories

    def getInfo(self):
        print(
            f"  [{self.getStatus()}] 🍰 {self.getName()}  NT${self.getPrice()}  ({self.__calories} kcal)"
        )


class Snack(MenuItem):
    """素食葷食"""

    def __init__(self, name, price, stock, is_vegan):
        super().__init__(name, price, stock)
        self.__is_vegan = is_vegan

    def getInfo(self):
        if self.__is_vegan:
            vegan = "素食"
        else:
            vegan = "葷食"
        print(
            f"  [{self.getStatus()}] 🥐 {self.getName()}  NT${self.getPrice()}  ({vegan})"
        )


# ============================================================
# Order 類別：管理一筆訂單
# ============================================================


class Order:
    """訂單類別，記錄顧客點了哪些品項"""

    def __init__(self, customer_name):
        self.__customer = customer_name
        self.__item_names = []  # 存品項名稱
        self.__item_prices = []  # 存品項價格

    def addItem(self, item):
        """加入品項，庫存不足時由外部 try/except 處理"""
        item.reduceStock()
        self.__item_names.append(item.getName())
        self.__item_prices.append(item.getPrice())
        print(f"  ✓ 已加入：{item.getName()}")

    def getTotal(self):
        """計算訂單總金額"""
        total = 0
        for price in self.__item_prices:
            total += price
        return total

    def printReceipt(self):
        """印出結帳收據"""
        print()
        print("=" * 35)
        print("   ☕ Sheng's Café  收據")
        print(f"   顧客：{self.__customer}")
        print("-" * 35)
        for i in range(len(self.__item_names)):
            print(f"   {self.__item_names[i]}  NT${self.__item_prices[i]}")
        print("-" * 35)
        print(f"   合計：NT${self.getTotal()}")
        print("=" * 35)


# ============================================================
# 主程式
# ============================================================

if __name__ == "__main__":
    # ── 建立菜單品項 ──
    item1 = HotDrink("美式咖啡", 80, 5, "85°C")
    item2 = HotDrink("拿鐵", 110, 3, "80°C")
    item3 = ColdDrink("抹茶拿鐵", 120, 4, 500)
    item4 = ColdDrink("檸檬氣泡水", 90, 2, 400)
    item5 = Dessert("提拉米蘇", 150, 2, 320)
    item6 = Dessert("草莓塔", 130, 1, 280)
    item7 = Snack("可頌", 65, 6, False)
    item8 = Snack("酪梨吐司", 110, 3, True)

    menu = [item1, item2, item3, item4, item5, item6, item7, item8]

    # ── 印出菜單（多型：每種品項自動呼叫自己的 getInfo()）──
    print("================================")
    print("     ☕ Sheng's Café 菜單")
    print("================================")
    for item in menu:
        item.getInfo()

    # ── 顧客點餐 ──
    print("\n【顧客 Sheng 開始點餐】")
    order = Order("Sheng")
    try:
        order.addItem(item2)  # 拿鐵
        order.addItem(item5)  # 提拉米蘇
        order.addItem(item7)  # 可頌
    except OutOfStockError as e:
        print(f"  ✗ 點餐失敗：{e}")

    order.printReceipt()

    # ── 測試異常：草莓塔只剩 1 個，點兩次 ──
    print("\n【測試：草莓塔只剩 1 個，連續點兩次】")
    try:
        order.addItem(item6)  # 第一次：成功
        order.addItem(item6)  # 第二次：售完，拋出異常
    except OutOfStockError as e:
        print(f"  ✗ 異常攔截：{e}")
