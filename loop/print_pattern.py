"""
檔名：print_pattern.py
功能：迴圈演算法練習
學習重點：for/while 迭代、控制流程
"""
for i in range(6, 0, -1):
    stars = "*" * i
    # 直接將組好的星號字串放入 f-string 印出
    print(f"{stars}")