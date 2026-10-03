@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

cls
echo.
echo ════════════════════════════════════════════════════
echo 🚀 DISCORD SUPPLIERS BOT - INSTALLATION AUTOMATIQUE
echo ════════════════════════════════════════════════════
echo.

REM Vérifier Python
echo ✓ Vérification de Python...
py --version >nul 2>&1
if errorlevel 1 (
    python --version >nul 2>&1
    if errorlevel 1 (
        echo ❌ Python n'est pas installé!
        echo.
        echo Téléchargez Python: https://www.python.org/downloads/
        echo.
        pause
        exit /b
    )
)
echo ✅ Python trouvé!
echo.

REM Créer un script temporaire pour installer pip si besoin
echo ✓ Installation des paquets...
echo.

py -m pip install discord.py python-dotenv --quiet >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Installation en cours...
    py -m pip install discord.py python-dotenv
)

echo ✅ Paquets prêts!
echo.

REM Demander le token avec VBS (fenêtre de dialogue)
cls
echo.
echo ════════════════════════════════════════════════════
echo 🔑 CONFIGURATION DU TOKEN DISCORD
echo ════════════════════════════════════════════════════
echo.

REM Créer un script VBS pour demander le token
(
    echo Set objIE = CreateObject("InternetExplorer.Application"^)
    echo strToken = InputBox("Collez votre token Discord ici:", "Configuration du Bot Discord"^)
    echo If strToken = "" Then
    echo     WScript.Quit
    echo End If
    echo Set objFSO = CreateObject("Scripting.FileSystemObject"^)
    echo Set objFile = objFSO.CreateTextFile(".env", True^)
    echo objFile.WriteLine("DISCORD_TOKEN=" ^& strToken^)
    echo objFile.Close
) > "%temp%\gettoken.vbs"

cscript.exe "%temp%\gettoken.vbs" >nul 2>&1

if not exist ".env" (
    echo.
    echo ❌ Token vide! Installation annulée.
    pause
    exit /b
)

cls
echo.
echo ════════════════════════════════════════════════════
echo 🎉 LANCEMENT DU BOT...
echo ════════════════════════════════════════════════════
echo.
echo ⚠️  IMPORTANT:
echo Ne fermez PAS cette fenêtre pendant que le bot est actif!
echo.
echo 📋 Une fois le bot lancé:
echo 1. Allez sur votre serveur Discord
echo 2. Écrivez: !setup
echo 3. Le bot créera automatiquement tous les canaux
echo.
echo ════════════════════════════════════════════════════
echo.

py bot.py

pause
