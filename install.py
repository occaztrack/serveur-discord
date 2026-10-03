#!/usr/bin/env python3
"""Installation et lancement automatique du Discord Bot"""

import subprocess
import sys
import os
from pathlib import Path

def clear():
    """Nettoie l'écran"""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_command(cmd, show_output=False):
    """Exécute une commande"""
    try:
        if show_output:
            subprocess.run(cmd, shell=True, check=True)
        else:
            subprocess.run(cmd, shell=True, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    clear()
    print("════════════════════════════════════════════════════")
    print("🚀 DISCORD SUPPLIERS BOT - INSTALLATION")
    print("════════════════════════════════════════════════════")
    print()

    # 1. Installer les dépendances
    print("📦 Installation des dépendances...")
    print("(Cela peut prendre 1-2 minutes)")
    print()

    if not run_command(f"{sys.executable} -m pip install discord.py python-dotenv", show_output=True):
        print()
        print("❌ Erreur lors de l'installation des dépendances!")
        print("Essayez manuellement:")
        print(f"  {sys.executable} -m pip install discord.py python-dotenv")
        input("Appuyez sur ENTRÉE pour continuer...")
        return

    print()
    print("✅ Dépendances installées!")
    print()

    # 2. Demander le token
    print("🔑 Configuration du token Discord")
    print()
    print("Où trouver votre token?")
    print("1. Allez sur: https://discord.com/developers/applications")
    print("2. Cliquez sur votre application")
    print("3. À gauche, cliquez sur 'Bot'")
    print("4. Cliquez 'Copy' pour copier le token")
    print()

    token = input("Collez votre token Discord ici: ").strip()

    if not token:
        print()
        print("❌ Token vide! Installation annulée.")
        input("Appuyez sur ENTRÉE pour continuer...")
        return

    print("✅ Token reçu!")
    print()

    # 3. Créer .env
    print("💾 Création du fichier .env...")
    env_file = Path(".env")
    env_file.write_text(f"DISCORD_TOKEN={token}\n")
    print("✅ Fichier .env créé!")
    print()

    # 4. Lancer le bot
    print("════════════════════════════════════════════════════")
    print("🎉 LANCEMENT DU BOT...")
    print("════════════════════════════════════════════════════")
    print()
    print("⚠️  IMPORTANT:")
    print("Ne fermez PAS cette fenêtre pendant que le bot est actif!")
    print()
    print("📋 Une fois le bot lancé:")
    print("1. Allez sur votre serveur Discord")
    print("2. Écrivez: !setup")
    print("3. Le bot créera automatiquement tous les canaux")
    print()
    print("════════════════════════════════════════════════════")
    print()

    # Lancer le bot
    if Path("bot.py").exists():
        subprocess.run([sys.executable, "bot.py"])
    else:
        print("❌ Fichier bot.py non trouvé!")
        input("Appuyez sur ENTRÉE pour continuer...")

if __name__ == "__main__":
    main()
