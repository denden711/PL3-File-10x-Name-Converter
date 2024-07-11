import os
import re
from tkinter import Tk, filedialog
import traceback

def rename_files_in_directory(directory_path):
    # ディレクトリツリーを再帰的に探索
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            # .txpファイルのみを対象にする
            if filename.endswith(".txp"):
                try:
                    # ファイル名のパターンを解析
                    match = re.match(r"x=(\d+(\.\d+)?).txp", filename)
                    if match:
                        number_str = match.group(1)
                        number = float(number_str)
                        
                        # 0の場合は何もしない
                        if number == 0:
                            continue
                        
                        # 数字を10倍する
                        new_number = number * 10
                        
                        # 新しいファイル名を作成
                        new_filename = f"x={new_number}.txp"
                        
                        # ファイルのフルパスを作成
                        old_file_path = os.path.join(root, filename)
                        new_file_path = os.path.join(root, new_filename)
                        
                        # ファイル名の置換
                        os.rename(old_file_path, new_file_path)
                        print(f"Renamed {old_file_path} to {new_file_path}")
                except Exception as e:
                    print(f"Failed to rename {filename}: {e}")
                    traceback.print_exc()

def select_directory_and_rename_files():
    try:
        # GUIでディレクトリを選択
        root = Tk()
        root.withdraw()  # メインウィンドウを表示しない
        directory_path = filedialog.askdirectory(title="ディレクトリを選択")
        if directory_path:
            rename_files_in_directory(directory_path)
        else:
            print("ディレクトリが選択されませんでした")
    except Exception as e:
        print(f"An error occurred while selecting directory: {e}")
        traceback.print_exc()

# メイン関数を実行
if __name__ == "__main__":
    select_directory_and_rename_files()
