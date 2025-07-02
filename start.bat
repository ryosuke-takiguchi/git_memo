@echo off
cd /d "%~dp0"

REM ============================================================
REM このスクリプトは、Python仮想環境をアクティベートし
REM メインスクリプトを実行します。
REM ============================================================

REM 仮想環境をアクティブ化
call venv\Scripts\activate.bat

REM main.pyの実行
python -m main
