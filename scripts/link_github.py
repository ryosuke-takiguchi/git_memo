def main():
    # iniファイルの読み込み
    from read_ini import IniReader
    try:
        iniread = IniReader("config.ini")
    except FileNotFoundError as e:
        print(f"iniファイルが見つかりません: {e}")
        exit(1) 
        
    try:
        iniread.get("github", "token")
        iniread.get("github", "repository")
    except KeyError as e:
        print(f"iniファイルのキーが見つかりません: {e}")
        exit(1)
        
if __name__ == "__main__":
    main()