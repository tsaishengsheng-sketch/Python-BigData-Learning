# 提示使用者一次輸入 a, b, c
a, b, c = map(float, input("請輸入 a b c (用空格隔開): ").split())

# 1. 先計算判別式 D
d = b**2 - 4*a*c

# 2. 判斷 a 是否為 0 (a 不能為 0 否則不是二次方程式)
if a == 0:
    print("a 不能為 0，這不是一元二次方程式。")
else:
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print(f"有兩個實根: {root1} 與 {root2}")
    elif d == 0:
        root = -b / (2*a)
        print(f"有重根: {root}")
    else:
        print("無實根 (結果為虛根)")