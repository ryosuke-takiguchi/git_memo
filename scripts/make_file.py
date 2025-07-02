from pathlib import Path
import datetime

class FileCreator:
    def __init__(self, base_dir: Path, exclude_dirs: list[str] = None):
        self.base_dir = base_dir.expanduser().resolve()
        self.exclude_dirs = [self.base_dir / Path(p) for p in (exclude_dirs or [])]
        self.subdirectories = []

    def is_valid_directory(self) -> bool:
        return self.base_dir.is_dir()

    def list_subdirectories(self):
        # 除外ディレクトリで始まらないものをフィルタ
        self.subdirectories = [
            p for p in self.base_dir.rglob("*") if p.is_dir()
            and not any(str(p).startswith(str(exclude)) for exclude in self.exclude_dirs)
        ]
        return self.subdirectories

    def select_directory(self) -> Path:
        print("\n=== ディレクトリ一覧 ===")
        for i, d in enumerate(self.subdirectories):
            print(f"{i}: {d.relative_to(Path.cwd())}")
        while True:
            try:
                choice = int(input("ディレクトリ番号を選んでください: "))
                if 0 <= choice < len(self.subdirectories):
                    return self.subdirectories[choice]
            except ValueError:
                pass
            print("無効な入力です。もう一度。")

    def create_file(self, directory: Path, filename: str = None) -> Path:
        if not filename:
            now = datetime.datetime.now()
            input_name = input("作成するファイル名を入力してください。")
            filename = now.strftime(f"{input_name}_%Y%m%d_%H%M%S.md")
        new_file = directory / filename
        new_file.touch(exist_ok=False)
        return new_file
