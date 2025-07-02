

REM ============================================================
REM githubとのリンクを作成するバッチファイル
REM このバッチファイルは、Python仮想環境をアクティブにし、
REM link_github.py スクリプトを実行します。 
REM ============================================================

call venv\Scripts\activate.bat
cd /d "%~dp0"
python -m scripts.link_github

pause