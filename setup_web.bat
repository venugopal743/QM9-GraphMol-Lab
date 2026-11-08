@echo off
cd /d "%~dp0"
python -m pip install -r requirements.txt
python -m pip install -r web\requirements-web.txt
python run_web.py
