# PL3 File 10x Name Converter

## 概要

"PL3 File 10x Name Converter" は、指定されたディレクトリ以下の `.pl3` ファイルの名前に含まれる数値を10倍に変換し、新しいファイル名でコピーするPythonツールです。元のファイルは削除され、変換後のファイル名で保存されます。

## 特徴

- ディレクトリ以下のすべての `.pl3` ファイルを再帰的に処理
- ファイル名に含まれる数値を10倍に変換
- エラーハンドリング機能を強化し、エラーログを保存
- GUIを使用してディレクトリを簡単に選択可能

## 使用方法

1. このリポジトリをクローンまたはダウンロードします。

    ```bash
    git clone https://github.com/yourusername/pl3-file-10x-name-converter.git
    ```

2. 必要なPythonパッケージをインストールします。

    ```bash
    pip install tkinter
    ```

3. `converter.py` ファイルを実行します。

    ```bash
    python converter.py
    ```

4. プログラムが起動したら、「ディレクトリを選択」ボタンをクリックして、変換したいファイルが含まれるディレクトリを選択します。

5. 選択されたディレクトリ内の `.pl3` ファイルが自動的に処理されます。エラーが発生した場合は、エラーログが `error_log.txt` に保存されます。

## コードの説明

### `create_new_file_name`

この関数は、ファイル名から数値を抽出し、その数値を10倍にして新しいファイル名を生成します。数値が `0` の場合は無視します。

```python
def create_new_file_name(file_name):
    match = re.search(r"x=(\d+\.?\d*)", file_name)
    if match:
        number = float(match.group(1))
        if number == 0:
            return None
        new_number = int(number * 10)
        new_file_name = f"x={new_number}.pl3"
        return new_file_name
    return None
```

### `process_files`

この関数は、指定されたディレクトリ以下のすべての `.pl3` ファイルを処理し、新しいファイル名でコピーします。処理中にエラーが発生した場合は、エラーログに記録します。

```python
def process_files(target_directory):
    error_log = []
    for root, dirs, files in os.walk(target_directory):
        for file_name in files:
            if file_name.endswith(".pl3"):
                old_file_path = os.path.join(root, file_name)
                try:
                    new_file_name = create_new_file_name(file_name)
                    if new_file_name:
                        new_file_path = os.path.join(root, new_file_name)
                        if old_file_path != new_file_path:
                            shutil.copy(old_file_path, new_file_path)
                            os.remove(old_file_path)
                            print(f"{old_file_path} を {new_file_path} に変換しました。")
                except FileNotFoundError:
                    error_message = f"ファイルが見つかりません: {old_file_path}"
                    error_log.append(error_message)
                    messagebox.showerror("ファイルエラー", error_message)
                except PermissionError:
                    error_message = f"ファイルへのアクセスが拒否されました: {old_file_path}"
                    error_log.append(error_message)
                    messagebox.showerror("アクセスエラー", error_message)
                except shutil.SameFileError:
                    error_message = f"同じファイルをコピーしようとしました: {old_file_path}"
                    error_log.append(error_message)
                    messagebox.showerror("ファイルエラー", error_message)
                except Exception as e:
                    error_message = f"{file_name} の処理中にエラーが発生しました: {str(e)}"
                    error_log.append(error_message)
                    messagebox.showerror("エラー", error_message)
    if error_log:
        with open(os.path.join(target_directory, "error_log.txt"), "w") as log_file:
            for log in error_log:
                log_file.write(log + "\n")
    messagebox.showinfo("完了", "すべてのファイルが変換されました。エラーが発生した場合は、error_log.txt を確認してください。")
```

### `select_directory`

この関数は、ディレクトリ選択ダイアログを表示し、選択されたディレクトリを処理します。

```python
def select_directory():
    target_directory = filedialog.askdirectory()
    if target_directory:
        process_files(target_directory)
```

### メインウィンドウの設定

この部分では、メインウィンドウを設定し、「ディレクトリを選択」ボタンを配置します。

```python
root = tk.Tk()
root.title("PL3 File 10x Name Converter")
select_button = tk.Button(root, text="ディレクトリを選択", command=select_directory)
select_button.pack(pady=20)
root.mainloop()
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 貢献

バグ報告や新機能の提案は、[Issues](https://github.com/yourusername/pl3-file-10x-name-converter/issues) ページからお願いします。プルリクエストも歓迎します。
```