from github import Github

# トークンを使って認証
g = Github("your_personal_access_token")

# 自分のユーザーアカウントを取得
user = g.get_user()

# リポジトリ作成
repo_name = "my-private-memo-repo"
description = "CLIベースのメモ管理用リポジトリ"

repo = user.create_repo(
    name=repo_name,
    description=description,
    private=True,             # ここがポイント
    has_issues=True,
    has_wiki=False,
    auto_init=True            # README.md を自動生成
)

print(f"リポジトリ作成完了: {repo.full_name}")
print(f"URL: {repo.html_url}")
