@echo off
cd /d "%~dp0"

REM ============================================================
REM このスクリプトは、Python仮想環境を作成し、必要なパッケージをインストールします。
REM また、config.iniファイルを生成します。
REM ============================================================

REM config.iniを作成
echo [github] > config.ini
echo token="your_github_token" >> config.ini
echo repository="your_repository_name" >> config.ini

REM python仮想環境作成
python -m venv venv

REM 仮想環境をアクティブ化
call venv\Scripts\activate.bat

REM 必要なパッケージをインストール
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo setup successfully completed.
pause