import os

def get_info_by_folder(folder_name, file_name):
    # 根據資料夾名稱自動給出專業的分類
    info = {
        "function": ("函式封裝練習", "參數傳遞、Return 回傳值應用"),
        "loop": ("迴圈演算法練習", "for/while 迭代、控制流程"),
        "if_else": ("邏輯判斷練習", "條件分歧、布林邏輯運算"),
        "list": ("資料結構與排序", "串列操作、演算法效率優化"),
        "variable_constant": ("基礎語法練習", "變數賦值、基本數學運算")
    }
    return info.get(folder_name, ("基礎 Python 練習", "語法熟悉與邏輯實作"))

def update_files():
    for root, dirs, files in os.walk("."):
        folder = os.path.basename(root)
        for file in files:
            if file.endswith(".py") and file != "add_docstrings.py":
                file_path = os.path.join(root, file)
                
                feature, point = get_info_by_folder(folder, file)
                
                docstring = f'"""\n檔名：{file}\n功能：{feature}\n學習重點：{point}\n"""\n'
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # 只有當檔案開頭不是 """ 時才寫入，避免重複
                if not content.startswith('"""'):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(docstring + content)
                    print(f"✅ 已完成分類標註: [{folder}] {file}")

if __name__ == "__main__":
    update_files()