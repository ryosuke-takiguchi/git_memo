from pathlib import Path
from scripts.make_file import FileCreator

def main():
    # 20250626作成開始
    print("Hello, World!")
    
    while True:
        print("\n=== メニュー選択 ===")
        print("1: ファイル作成")
        print("2: 終了")

        choice = input("選択肢を入力してください: ")

        if choice == "1":
            print("\nファイル作成が選択されました。")
            base_path = Path("./memos/")
            exclude = ["archive", "tmp", r"\.git"]  # 任意の除外ディレクトリ

            creator = FileCreator(base_path, exclude_dirs=exclude)

            if not creator.is_valid_directory():
                print("無効なベースディレクトリです。")
                continue

            subdirs = creator.list_subdirectories()
            if not subdirs:
                print("有効なサブディレクトリが見つかりません。")
                continue

            selected_dir = creator.select_directory()
            new_file = creator.create_file(selected_dir)
            print(f"\nファイルを作成しました: {new_file}")

        elif choice == "2":
            print("終了します。")
            break
        else:
            print("無効な選択肢です。もう一度選んでください。")

if __name__ == "__main__":
    main()
