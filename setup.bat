@echo off
cd /d "%~dp0"

REM ============================================================
REM ���̃X�N���v�g�́APython���z�����쐬���A�K�v�ȃp�b�P�[�W���C���X�g�[�����܂��B
REM �܂��Aconfig.ini�t�@�C���𐶐����܂��B
REM ============================================================

REM config.ini���쐬
echo [github] > config.ini
echo token="your_github_token" >> config.ini
echo repository="your_repository_name" >> config.ini

REM python���z���쐬
python -m venv venv

REM ���z�����A�N�e�B�u��
call venv\Scripts\activate.bat

REM �K�v�ȃp�b�P�[�W���C���X�g�[��
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo setup successfully completed.
pause