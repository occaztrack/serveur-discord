# Script d'installation automatique - Discord Suppliers Bot
# Double-cliquez sur ce fichier pour lancer l'installation!

Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "🚀 DISCORD SUPPLIERS BOT - INSTALLATION AUTOMATIQUE" -ForegroundColor Green
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Fonction pour pause
function Pause {
    Write-Host "Appuyez sur une touche pour continuer..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}

# 1. Vérifier Python
Write-Host "✓ Étape 1/5: Vérification de Python..." -ForegroundColor Cyan
try {
    $pythonVersion = py --version 2>&1
    Write-Host "✅ Python trouvé: $pythonVersion" -ForegroundColor Green
} catch {
    try {
        $pythonVersion = python --version 2>&1
        Write-Host "✅ Python trouvé: $pythonVersion" -ForegroundColor Green
    } catch {
        Write-Host "❌ Python n'est pas installé!" -ForegroundColor Red
        Write-Host "Téléchargez Python depuis: https://www.python.org/downloads/" -ForegroundColor Yellow
        Pause
        exit
    }
}

# 2. Demander le token
Write-Host ""
Write-Host "✓ Étape 2/5: Configuration du token..." -ForegroundColor Cyan
Write-Host "Où trouver votre token?" -ForegroundColor Yellow
Write-Host "1. Allez sur: https://discord.com/developers/applications"
Write-Host "2. Cliquez sur votre application"
Write-Host "3. À gauche, cliquez sur 'Bot'"
Write-Host "4. Cliquez 'Copy' pour copier le token"
Write-Host ""

$token = Read-Host "Collez votre token Discord ici"

if ([string]::IsNullOrWhiteSpace($token)) {
    Write-Host "❌ Token vide! Installation annulée." -ForegroundColor Red
    Pause
    exit
}

Write-Host "✅ Token reçu!" -ForegroundColor Green

# 3. Créer .env
Write-Host ""
Write-Host "✓ Étape 3/5: Création du fichier .env..." -ForegroundColor Cyan

# Obtenir le chemin du script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path

# Créer le fichier .env
$envContent = "DISCORD_TOKEN=$token"
$envFile = Join-Path $scriptPath ".env"

Set-Content -Path $envFile -Value $envContent
Write-Host "✅ Fichier .env créé: $envFile" -ForegroundColor Green

# 4. Installer les dépendances
Write-Host ""
Write-Host "✓ Étape 4/5: Installation des dépendances..." -ForegroundColor Cyan
Write-Host "Cela peut prendre quelques minutes..." -ForegroundColor Yellow

$requirementsFile = Join-Path $scriptPath "requirements.txt"

if (Test-Path $requirementsFile) {
    try {
        py -m pip install -r $requirementsFile --quiet
        Write-Host "✅ Dépendances installées!" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Erreur lors de l'installation des dépendances" -ForegroundColor Yellow
        Write-Host "Essayez manuellement: py -m pip install -r requirements.txt" -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ Fichier requirements.txt non trouvé!" -ForegroundColor Red
    Pause
    exit
}

# 5. Lancer le bot
Write-Host ""
Write-Host "✓ Étape 5/5: Lancement du bot..." -ForegroundColor Cyan
Write-Host ""
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "🎉 LANCEMENT DU BOT..." -ForegroundColor Green
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "⚠️  IMPORTANT:" -ForegroundColor Yellow
Write-Host "Ne fermez PAS cette fenêtre pendant que le bot est actif!" -ForegroundColor Yellow
Write-Host ""
Write-Host "📋 Une fois le bot lancé:" -ForegroundColor Cyan
Write-Host "1. Allez sur votre serveur Discord"
Write-Host "2. Écrivez: !setup"
Write-Host "3. Le bot créera automatiquement tous les canaux"
Write-Host ""
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Lancer le bot
$botFile = Join-Path $scriptPath "bot.py"

if (Test-Path $botFile) {
    py $botFile
} else {
    Write-Host "❌ Fichier bot.py non trouvé!" -ForegroundColor Red
    Write-Host "Assurez-vous d'être dans le bon dossier" -ForegroundColor Yellow
    Pause
    exit
}
