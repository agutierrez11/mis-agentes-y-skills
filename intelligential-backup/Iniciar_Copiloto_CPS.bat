@echo off
title Intelligential CPS Copilot Launcher
echo ==================================================================
echo 🚀 INICIANDO COPILOTO CPS & PWA DASHBOARD (INTELLIGENTIAL)
echo ==================================================================
echo.

cd /d "c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential"

echo [1/2] Verificando servidor Ollama...
powershell -Command "try { $r = Invoke-WebRequest -Uri 'http://localhost:11434/api/tags' -TimeoutSec 2; if ($r.StatusCode -eq 200) { Write-Host '✔ Ollama Activo' -ForegroundColor Green } } catch { Write-Host '⚠️ Iniciando Ollama...' -ForegroundColor Yellow; Start-Process 'ollama' -ArgumentList 'serve' }"

echo [2/2] Lanzando servidor agéntico y PWA Dashboard...
start "" http://localhost:8080/copilot.html
python app_copilot_server.py

pause
