import os
import zipfile
import shutil
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

print("==========================================================")
print("📦 EMPAQUETADOR AUTOMÁTICO DE ANTIGRAVITY (LAPTOP MIGRATION)")
print("==========================================================")

home = os.path.expanduser("~")
desktop = os.path.join(home, "Desktop")
backup_zip_path = os.path.join(desktop, "RESPALDO_COMPLETO_ANTIGRAVITY_ANTONIO.zip")

config_dir = os.path.join(home, ".gemini", "config")
scratch_dir = os.path.join(home, ".gemini", "antigravity-ide", "scratch")

print(f"\n1. Verificando rutas de origen...")
print(f" - Config Global: {config_dir} ({'OK' if os.path.exists(config_dir) else 'No encontrado'})")
print(f" - Scratch Repos: {scratch_dir} ({'OK' if os.path.exists(scratch_dir) else 'No encontrado'})")

print(f"\n2. Creando archivo ZIP comprimido en Escritorio:")
print(f" ➔ {backup_zip_path}")

# Generar script de restauración bat
restore_bat_content = """@echo off
echo ==========================================================
echo 🚀 RESTAURADOR DE 1-CLIC DE ANTIGRAVITY PARA LAPTOP NUEVA
echo ==========================================================
echo.
echo Restaurando configuraciones globales y proyectos...

set DEST_HOME=%USERPROFILE%
set DEST_CONFIG=%DEST_HOME%\\.gemini\\config
set DEST_SCRATCH=%DEST_HOME%\\.gemini\\antigravity-ide\\scratch

if not exist "%DEST_CONFIG%" mkdir "%DEST_CONFIG%"
if not exist "%DEST_SCRATCH%" mkdir "%DEST_SCRATCH%"

powershell -Command "Expand-Archive -Path '%~dp0RESPALDO_COMPLETO_ANTIGRAVITY_ANTONIO.zip' -DestinationPath '%~dp0temp_restore' -Force"

if exist "%~dp0temp_restore\\config" (
    echo Copiando skills y reglas globales...
    xcopy "%~dp0temp_restore\\config" "%DEST_CONFIG%" /E /I /Y /H
)

if exist "%~dp0temp_restore\\scratch" (
    echo Copiando proyectos y repositorios...
    xcopy "%~dp0temp_restore\\scratch" "%DEST_SCRATCH%" /E /I /Y /H
)

rd /s /q "%~dp0temp_restore"

echo.
echo ==========================================================
echo ✅ ¡MIGRACIÓN COMPLETADA CON ÉXITO!
echo Abre Antigravity IDE y todo estará exactamente como en tu laptop anterior.
echo ==========================================================
pause
"""

temp_dir = os.path.join(home, ".gemini", "temp_backup_staging")
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)

os.makedirs(temp_dir, exist_ok=True)
os.makedirs(os.path.join(temp_dir, "config"), exist_ok=True)
os.makedirs(os.path.join(temp_dir, "scratch"), exist_ok=True)

# Ignorar carpetas pesadas prescindibles (node_modules, __pycache__, .venv)
def ignore_patterns(path, names):
    ignored = []
    for name in names:
        if name in ['node_modules', '__pycache__', '.venv', 'venv']:
            ignored.append(name)
    return ignored

print("\n3. Copiando archivos a staging...")
if os.path.exists(config_dir):
    shutil.copytree(config_dir, os.path.join(temp_dir, "config"), ignore=ignore_patterns, dirs_exist_ok=True)

if os.path.exists(scratch_dir):
    shutil.copytree(scratch_dir, os.path.join(temp_dir, "scratch"), ignore=ignore_patterns, dirs_exist_ok=True)

# Escribir el bat dentro de staging
with open(os.path.join(temp_dir, "RESTAURAR_EN_LAPTOP_NUEVA.bat"), "w", encoding="utf-8") as f:
    f.write(restore_bat_content)

print("\n4. Comprimiendo paquete completo...")
with zipfile.ZipFile(backup_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, temp_dir)
            zipf.write(file_path, arcname)

shutil.rmtree(temp_dir)

print("\n==========================================================")
print(f"🎉 ¡PAQUETE DE MIGRACIÓN CREADO EXITOSAMENTE!")
print(f"Ubicación: {backup_zip_path}")
print(f"Tamaño: {os.path.getsize(backup_zip_path) / (1024*1024):.2f} MB")
print("==========================================================")
