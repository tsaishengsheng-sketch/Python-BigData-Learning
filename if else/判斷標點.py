# 取得使用者輸入的座標
x, y = map(float, input("請輸入 x,y: ").split(','))
# 計算點到原點距離的平方
distance_squared = x**2 + y**2

# 判斷是否在半徑為 10 的圓內 (10的平方是 100)
if distance_squared < 100:
    print(f'點 ({x}, {y}) 在圓體內部')
elif distance_squared == 100:
    print(f'點 ({x}, {y}) 正好在圓周上')
else:
    print(f'點 ({x}, {y}) 在圓體外部')