@echo off
cd /d "%~dp0"

REM ============================================================
REM githubとのリンクを作成するバッチファイル
REM このバッチファイルは、Python仮想環境をアクティブにし、
REM link_github.py スクリプトを実行します。 
REM ============================================================

call venv\Scripts\activate.bat
python scripts\link_github.py

pause