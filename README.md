# PL3-File-10x-Name-Converter

## 概要

`PL3-File-10x-Name-Converter`は、指定したディレクトリ内およびそのサブディレクトリ内のすべての`.pl3`ファイルの名前を変換するツールです。ファイル名の形式は`x=数字.pl3`であり、この数字を10倍にした新しいファイル名に変換します。ただし、`x=0.pl3`はそのままにします。

## 使用方法

1. スクリプトを実行すると、ディレクトリ選択ダイアログが表示されます。
2. 変換したいファイルが含まれるディレクトリを選択します。
3. スクリプトがディレクトリ内のすべての`.pl3`ファイルを再帰的に検索し、名前を変換します。

## 前提条件

- Python 3.x
- `tkinter`ライブラリ（通常のPythonインストールに含まれています）

## インストール

特別なインストール手順は必要ありません。Pythonがインストールされていることを確認してください。

## スクリプト

以下は、`PL3-File-10x-Name-Converter`のスクリプトです。

```python
import os
import re
from tkinter import Tk, filedialog
import traceback

def rename_files_in_directory(directory_path):
    # ディレクトリツリーを再帰的に探索
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            # .pl3ファイルのみを対象にする
            if filename.endswith(".pl3"):
                try:
                    # ファイル名のパターンを解析
                    match = re.match(r"x=(\d+(\.\d+)?).pl3", filename)
                    if match:
                        number_str = match.group(1)
                        number = float(number_str)
                        
                        # 0の場合は何もしない
                        if number == 0:
                            continue
                        
                        # 数字を10倍する
                        new_number = number * 10
                        
                        # 新しいファイル名を作成
                        new_filename = f"x={new_number}.pl3"
                        
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
```

## エラーハンドリング

- ファイルのリネームが失敗した場合にエラーメッセージを表示します。
- ディレクトリ選択がキャンセルされた場合にメッセージを表示します。
- 読み取り専用のファイルやアクセス権限がないファイルに対して適切なエラーメッセージを表示します。

## ライセンス

このプロジェクトは個人利用のためフリーです。
