@echo off
cd /d "%~dp0"
.venv\Scripts\python.exe -m streamlit run enterprise_agent\ui.py --server.address 127.0.0.1
