@echo off
title Detener Copiloto CPS
echo ==================================================================
echo 🛑 DETENIENDO COPILOTO CPS Y LIBERANDO MEMORIA RAM
echo ==================================================================
echo.

taskkill /FI "WINDOWTITLE eq Intelligential CPS Copilot Launcher*" /F >nul 2>&1
wmic process where "commandline like '%app_copilot_server.py%'" delete >nul 2>&1

echo.
echo ✔ Servidor agéntico detenido. 100% de Memoria RAM y CPU liberada.
echo.
pause
