# git_memo


業務メモや日報を Git + GitHub で効率的に管理するための CLI ツールです。  
日々のメモ作成・履歴管理・復元・GitHub連携を簡単なコマンドで行え 
本プロジェクトはプログラム練習にて個人用に開発をしております。  
使用に際して発生した如何なる損害についても、対応しかねます。  

---

## 特徴  

Gitを使用しメモの履歴・差分管理を実現します。  
簡単な手順でメモの作成やGitへのコミット・pushを実現します。  
将来的にはGUIへの対応を検討中です。  

## インストール手順  

### 1. 仮想環境の作成と適用  

```bash
Python -m venv venv
venv\scripts\activate
```

### 必要パッケージのインストール  

```bash
pip install -r requirements.txt
```

## ディレクトリ構成  

```bash
root/
├── venv/              # 仮想環境
├── scripts/           # 機能別スクリプト
│   ├── memo_manager.py
│   ├── git_utils.py
│   └── config.py
├── memos/             # メモ格納場所（Gitで管理）
│   └── daily/
├── main.py            # エントリポイント
├── .gitignore
└── README.md          # このファイル
```

## ライセンス
MIT License  

## 作者  
RyosukeTakiguchi  
ryosuke_takiguchi@impcode.net  