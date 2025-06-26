import configparser
import os

class IniReader:
    def __init__(self, filepath: str):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"指定されたファイルが存在しません: {filepath}")
        self.filepath = filepath
        self.config = configparser.ConfigParser()
        self.config.read(filepath, encoding='utf-8')

    def get(self, section: str, key: str) -> str:
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            raise KeyError(f"指定されたキーが見つかりません: [{section}] {key}") from e