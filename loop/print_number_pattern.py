for i in range(1, 10):
    # 建立該行的初始空白
    spaces = " " * (9 - i)
    numbers = ""
    for j in range(1, i + 1):
        # 累加數字與空白
        numbers += f"{j} "
    
    # 結合空白與數字後印出
    print(f"{spaces}{numbers}")