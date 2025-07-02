import requests
from git import Repo
import os
from scripts.read_ini import IniReader
import urllib3

# SSL警告を無効に（開発用途）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    try:
        # iniファイルから読み込み
        ini = IniReader("config.ini")
        token = ini.get("github", "token")
        full_repo_name = ini.get("github", "repository").replace("\\", "/")

        # GitHub API URL
        api_url = f"https://api.github.com/repos/{full_repo_name}"

        # APIコール（SSL無効で）
        response = requests.get(api_url, headers={
            "Authorization": f"token {token}"
        }, verify=False)

        if response.status_code != 200:
            raise Exception(f"GitHub APIエラー: {response.status_code} {response.text}")

        repo_info = response.json()
        print(f"GitHubリポジトリをクローンします...\n{repo_info['full_name']}")
        print(f"説明: {repo_info.get('description', 'なし')}")

        # クローン先パス
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        clone_dir = os.path.join(project_root, "memos", os.path.basename(full_repo_name))
        clone_url = f"https://{token}:x-oauth-basic@github.com/{full_repo_name}.git"

        if not os.path.exists(clone_dir):
            print(f"クローン中: {clone_dir}")
            Repo.clone_from(clone_url, clone_dir)
            print("クローン完了")
        else:
            print(f"既に存在します: {clone_dir}")

    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    main()

