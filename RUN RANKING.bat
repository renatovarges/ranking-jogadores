@echo off
cd /d "%~dp0"
echo ==========================================
echo   Iniciando Ranking de Jogadores...
echo ==========================================
echo.
streamlit run app.py
pause
