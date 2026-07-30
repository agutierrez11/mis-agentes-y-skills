@echo off
title Iniciar Copiloto de Telegram (Intelligential)
color 0A
echo ===================================================
echo 🤖 INICIANDO BOT DE TELEGRAM (COPILOTO COMERCIAL)
echo ===================================================
echo.
cd /d "c:\Users\Antonio\.gemini\antigravity-ide\scratch\intelligential"

IF "%TELEGRAM_BOT_TOKEN%"=="" (
    echo ⚠️ ATENCION: La variable TELEGRAM_BOT_TOKEN no esta configurada.
    echo.
    echo Pasos rapidos para activarlo:
    echo 1. Abre Telegram y busca a @BotFather
    echo 2. Escribe /newbot y ponle nombre (Ej: CopilotoAntonioBot)
    echo 3. Copia el TOKEN que te da BotFather
    echo 4. Ejecuta en tu terminal: setx TELEGRAM_BOT_TOKEN "tu_token_aqui"
    echo.
    set /p BOT_TOKEN="O pega tu Token de Telegram aqui ahora mismo: "
    set TELEGRAM_BOT_TOKEN=%BOT_TOKEN%
)

echo 🚀 Arrancando Bot de Telegram en segundo plano...
python telegram_cps_bot.py
pause
