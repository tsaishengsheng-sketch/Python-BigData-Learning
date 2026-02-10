"""
標題：智慧門禁安全控制系統
應用：模擬門禁刷卡紀錄，具備黑名單驗證與通行日誌功能。
技術重點：
    1. 集合比對：利用 Set 進行 O(1) 極速黑名單驗證。
    2. 日誌管理：利用 Dictionary 追蹤通行頻率與最後出現時間。
    3. 模組整合：引入 time 模組進行系統時間紀錄。
"""
import time

def menu():
    print('\n--- 安全門禁控制中心 ---')
    print('1. 刷卡進入')
    print('2. 管理黑名單')
    print('3. 查閱通行日誌')
    print('4. 結束系統')
    try:
        return int(input('請選擇操作: '))
    except ValueError:
        return 0

def swipe_card(blacklist, logs):
    """核心邏輯：驗證黑名單並紀錄通行"""
    user_id = input("請刷卡或輸入 ID 編號: ").strip()
    
    # 1. 快速檢查 ID 是否在黑名單集合中
    if user_id in blacklist:
        print(f"⚠️ 存取拒絕：ID {user_id} 已列入黑名單！")
        return

    # 2. 通過檢查，將時間與次數更新至日誌字典
    current_time = time.strftime("%H:%M:%S", time.localtime())
    if user_id in logs:
        logs[user_id]['count'] += 1
        logs[user_id]['last_seen'] = current_time
    else:
        logs[user_id] = {'count': 1, 'last_seen': current_time}
    
    print(f"✅ 允許進入！ 歡迎 {user_id}。(時間: {current_time})")

def manage_blacklist(blacklist):
    """管理黑名單 Set (新增或移除)"""
    print(f"目前黑名單內容: {blacklist}")
    action = input("要新增還是移除黑名單？ (新增按 a / 移除按 r): ").lower()
    target = input("請輸入 ID: ").strip()
    
    if action == 'a':
        blacklist.add(target) # Set 新增元素
        print(f"已將 ID {target} 加入黑名單。")
    elif action == 'r' and target in blacklist:
        blacklist.remove(target) # Set 移除元素
        print(f"已從黑名單移除 ID {target}。")
    else:
        print("操作無效或找不到該 ID。")

def main():
    # 初始化黑名單 (Set)
    security_blacklist = {'ADMIN_TEST', '9999', 'BLOCK_USER'}
    # 初始化日誌 (Dictionary)
    access_logs = {}

    while True:
        choice = menu()
        if choice == 1:
            swipe_card(security_blacklist, access_logs)
        elif choice == 2:
            manage_blacklist(security_blacklist)
        elif choice == 3:
            print("\n--- 通行日誌紀錄 ---")
            for uid, info in access_logs.items():
                print(f"使用者: {uid} | 通行次數: {info['count']} | 最後出現時間: {info['last_seen']}")
        elif choice == 4:
            break
        else:
            print("無效選項。")

if __name__ == "__main__":
    main()