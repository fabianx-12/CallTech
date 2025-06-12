@echo off
title CallTech - Sistema de Agenda de Contactos
color 0A
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                        CALLTECH                              ║
echo  ║                Sistema de Agenda de Contactos                ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo  Iniciando CallTech...
echo.

cd /d "c:\Users\Fabia\Documents\curso-git"

echo  Verificando dependencias...
pip install -r requirements.txt >nul 2>&1

echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║  CallTech se está iniciando...                               ║
echo  ║                                                              ║
echo  ║  Accede desde tu navegador:                                  ║
echo  ║  • Local: http://localhost:5000                              ║
echo  ║  • Red:   http://tu-ip-local:5000                            ║
echo  ║                                                              ║
echo  ║  Para detener: Presiona Ctrl + C                             ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.

python app.py

echo.
echo  CallTech se ha detenido.
echo  Presiona cualquier tecla para cerrar...
pause >nul
