@echo off
cd /d "%~dp0"

REM ============================================================
REM ���̃X�N���v�g�́APython���z�����A�N�e�B�x�[�g��
REM ���C���X�N���v�g�����s���܂��B
REM ============================================================

REM ���z�����A�N�e�B�u��
call venv\Scripts\activate.bat

REM main.py�̎��s
python -m main
