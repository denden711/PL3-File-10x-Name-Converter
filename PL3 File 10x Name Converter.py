import os
import shutil
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# ファイル名から数値を抽出し、10倍にして新しいファイル名を作成する関数
def create_new_file_name(file_name):
    # 正規表現を使用してファイル名から数値部分を抽出
    match = re.search(r"x=(\d+\.?\d*)", file_name)
    if match:
        number = float(match.group(1))
        if number == 0:
            return None  # 数値が0の場合はファイルを無視
        new_number = int(number * 10)  # 数値を10倍にする
        new_file_name = f"x={new_number}.pl3"  # 新しいファイル名を生成
        return new_file_name
    return None

# ファイルの変換を行う関数
def process_files(target_directory):
    error_log = []  # エラーログを保存するリスト

    # 指定されたディレクトリ以下のすべてのファイルを再帰的に探索
    for root, dirs, files in os.walk(target_directory):
        for file_name in files:
            if file_name.endswith(".pl3"):  # .pl3ファイルのみを対象とする
                old_file_path = os.path.join(root, file_name)  # 元のファイルパスを取得
                try:
                    new_file_name = create_new_file_name(file_name)  # 新しいファイル名を生成
                    if new_file_name:
                        new_file_path = os.path.join(root, new_file_name)  # 新しいファイルパスを生成
                        if old_file_path != new_file_path:
                            # ファイルをコピーして名前を変更
                            shutil.copy(old_file_path, new_file_path)
                            # 元のファイルを削除
                            os.remove(old_file_path)
                            print(f"{old_file_path} を {new_file_path} に変換しました。")
                except FileNotFoundError:
                    # ファイルが見つからない場合のエラーハンドリング
                    error_message = f"ファイルが見つかりません: {old_file_path}"
                    error_log.append(error_message)
                    messagebox.showerror("ファイルエラー", error_message)
                except PermissionError:
                    # ファイルへのアクセスが拒否された場合のエラーハンドリング
                    error_message = f"ファイルへのアクセスが拒否されました: {old_file_path}"
                    error_log.append(error_message)
                    messagebox.showerror("アクセスエラー", error_message)
                except shutil.SameFileError:
                    # 同じファイルをコピーしようとした場合のエラーハンドリング
                    error_message = f"同じファイルをコピーしようとしました: {old_file_path}"
                    error_log.append(error_message)
                    messagebox.showerror("ファイルエラー", error_message)
                except Exception as e:
                    # その他の例外のエラーハンドリング
                    error_message = f"{file_name} の処理中にエラーが発生しました: {str(e)}"
                    error_log.append(error_message)
                    messagebox.showerror("エラー", error_message)

    # エラーログが存在する場合、error_log.txtに保存
    if error_log:
        with open(os.path.join(target_directory, "error_log.txt"), "w") as log_file:
            for log in error_log:
                log_file.write(log + "\n")

    # 処理完了のメッセージを表示
    messagebox.showinfo("完了", "すべてのファイルが変換されました。エラーが発生した場合は、error_log.txt を確認してください。")

# ディレクトリ選択ダイアログを表示する関数
def select_directory():
    target_directory = filedialog.askdirectory()  # ディレクトリ選択ダイアログを表示
    if target_directory:
        process_files(target_directory)  # 選択されたディレクトリを処理

# メインウィンドウの設定
root = tk.Tk()
root.title("PL3 File 10x Name Converter")  # ウィンドウのタイトルを設定

# ディレクトリ選択ボタンの設定
select_button = tk.Button(root, text="ディレクトリを選択", command=select_directory)
select_button.pack(pady=20)  # ボタンをウィンドウに配置

# メインループの開始
root.mainloop()
