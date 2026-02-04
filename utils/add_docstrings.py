import os

def get_info_by_folder(folder_name, file_name=""):
    # ✨ 新增：如果是 SmartLife_Toolbox.py，給它專屬的高級標註
    if file_name == "SmartLife_Toolbox.py":
        return ("綜合生活工具箱實作", "模組化整合、CLI 互動介面設計")

    info = {
        "function": ("函式封裝練習", "參數傳遞、Return 回傳值應用"),
        "loop": ("迴圈演算法練習", "for/while 迭代、控制流程"),
        "if_else": ("邏輯判斷練習", "條件分歧、布林邏輯運算"),
        "list": ("資料結構與排序", "串列操作、演算法效率優化"),
        "variable_constant": ("基礎語法練習", "變數賦值、基本數學運算"),
        "utils": ("工具程式", "專案輔助腳本與自動化工具"),
        "multidimensional_list": ("多維串列應用", "矩陣運算、巢狀迴圈與表格處理")
    }
    return info.get(folder_name, ("基礎 Python 練習", "語法熟悉與邏輯實作"))

def update_files():
    # 這裡確保包含了你所有的資料夾
    target_folders = ["function", "loop", "if_else", "list", "variable_constant", "utils", "multidimensional_list"]
    
    # 取得目前腳本所在的根目錄路徑 (避免路徑跑掉)
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    for folder in target_folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            continue
            
        for file in os.listdir(folder_path):
            if file.endswith(".py") and file != "add_docstrings.py":
                file_path = os.path.join(folder_path, file)
                
                # 🛠️ 這裡傳入 file 檔名，讓 get_info_by_folder 可以判斷
                feature, point = get_info_by_folder(folder, file)
                docstring = f'"""\n檔名：{file}\n功能：{feature}\n學習重點：{point}\n"""\n'
                
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                # 判斷是否已經有標註，如果有就更新，沒有就插入
                if lines and lines[0].startswith('"""'):
                    # 找到舊標註的結尾
                    end_index = 0
                    for i, line in enumerate(lines):
                        if i > 0 and line.strip() == '"""':
                            end_index = i
                            break
                    # 替換掉舊的標註
                    new_content = docstring + "".join(lines[end_index+1:])
                else:
                    new_content = docstring + "".join(lines)
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"✅ 已更新標註: [{folder}] {file}")

if __name__ == "__main__":
    update_files()