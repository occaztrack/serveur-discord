@echo off
chcp 65001 >nul
cls

echo.
echo ════════════════════════════════════════════════════
echo 🚀 DISCORD SUPPLIERS BOT - INSTALLATION AUTOMATIQUE
echo ════════════════════════════════════════════════════
echo.

REM Vérifier Python
echo Vérification de Python...
py --version >nul 2>&1
if errorlevel 1 (
    python --version >nul 2>&1
    if errorlevel 1 (
        echo ❌ Python n'est pas installé!
        echo Téléchargez Python depuis: https://www.python.org/downloads/
        pause
        exit /b
    )
)

echo ✅ Python trouvé!
echo.

REM Demander le token
echo ✓ Configuration du token
echo.
echo Où trouver votre token?
echo 1. Allez sur: https://discord.com/developers/applications
echo 2. Cliquez sur votre application
echo 3. À gauche, cliquez sur "Bot"
echo 4. Cliquez "Copy" pour copier le token
echo.

set /p token="Collez votre token Discord ici: "

if "%token%"=="" (
    echo ❌ Token vide! Installation annulée.
    pause
    exit /b
)

echo ✅ Token reçu!
echo.

REM Créer .env
echo ✓ Création du fichier .env...
echo DISCORD_TOKEN=%token% > .env
echo ✅ Fichier .env créé!
echo.

REM Installer dépendances
echo ✓ Installation des dépendances...
echo Cela peut prendre quelques minutes...
py -m pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ⚠️  Erreur lors de l'installation
    echo Essayez manuellement: py -m pip install -r requirements.txt
)

echo ✅ Dépendances installées!
echo.

REM Lancer le bot
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
