for i in range(1, 10):
    row = ""
    for j in range(1, i + 1):
        # 計算乘積並格式化為佔 3 格寬度
        res = i * j
        row += f"{res:<3}"
    print(f"{row}")