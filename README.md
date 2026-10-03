# 🚀 Discord Suppliers Marketplace Server

Un serveur Discord automatisé pour gérer et organiser une marketplace de **5000+ fournisseurs** par catégorie.

## 📌 À propos

Ce projet crée automatiquement un serveur Discord avec :
- ✅ **6 catégories principales** de fournisseurs
- ✅ **Sélection premium** de fournisseurs vérifiés
- ✅ **Informations détaillées** (pays, site web, contact)
- ✅ **Accès au pack complet** de 5000+ fournisseurs
- ✅ **Système de commandes** pour gérer les fournisseurs

## 🎯 Catégories

1. **💄 Cosmétique** - Produits de beauté et cosmétiques
2. **🎨 Personnalisation** - Services de personnalisation textile
3. **👗 Textile Femme** - Vêtements et textiles pour femme
4. **👔 Textile Homme** - Vêtements et textiles pour homme
5. **🔌 Accessoires Tech** - Équipements technologiques
6. **📱 Tech Téléphone** - Accessoires et équipements téléphoniques

## 📊 Données incluses

Ceci est une **sélection premium** de fournisseurs. Pour chaque catégorie :
- **5 fournisseurs** de pays différents (sélection)
- **5000+ fournisseurs** disponibles dans le pack complet

### Exemple de données par fournisseur :
- 🌍 Pays d'origine
- 🔗 Site web professionnel
- 📞 Coordonnées de contact
- 📧 Email/Social media

## 🛠️ Installation

### Prérequis
- Python 3.8+
- Un compte Discord Developer
- Un serveur Discord de test

### Étapes

1. **Cloner le repository**
```bash
git clone <repo-url>
cd serveur-discord
```

2. **Créer un bot Discord**
   - Allez sur [Discord Developer Portal](https://discord.com/developers/applications)
   - Créez une nouvelle application
   - Allez à "Bot" et créez un bot
   - Copiez le token

3. **Configurer les variables d'environnement**
```bash
cp .env.example .env
# Éditez .env et ajoutez votre token Discord
nano .env
```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Lancer le bot**
```bash
python bot.py
```

## 📝 Commandes

### Setup initial
```
!setup_suppliers
```
Crée automatiquement tous les canaux et catégories avec les fournisseurs.

**Permissions requises:** Administrateur du serveur

### Afficher les fournisseurs
```
!list_suppliers [category]
```

Exemples :
```
!list_suppliers cosmétique
!list_suppliers textile-femme
!list_suppliers textile-homme
```

## 📦 Structure du projet

```
serveur-discord/
├── bot.py                    # Bot Discord principal
├── suppliers_data.json       # Données des fournisseurs
├── requirements.txt          # Dépendances Python
├── .env.example             # Exemple de configuration
└── README.md                # Ce fichier
```

## 🔐 Sécurité

- ✅ Ne commitez **JAMAIS** votre `.env` réel (seulement `.env.example`)
- ✅ Gardez votre token Discord **secret**
- ✅ Utilisez des variables d'environnement pour les données sensibles

## 🎨 Personnalisation

### Modifier les données des fournisseurs

Éditez `suppliers_data.json` :
```json
{
  "categories": {
    "ma-categorie": {
      "emoji": "🎯",
      "description": "Description de ma catégorie",
      "suppliers": [
        {
          "name": "Mon Fournisseur",
          "country": "🇫🇷 France",
          "website": "https://example.com",
          "contact": "+33 1 23 45 67 89"
        }
      ]
    }
  }
}
```

### Modifier les couleurs et styles

Éditez les `discord.Color` dans `bot.py` :
```python
color=discord.Color.blue()      # Bleu
color=discord.Color.green()     # Vert
color=discord.Color.gold()      # Or
```

## 📞 Support

Pour les questions ou les problèmes :
1. Vérifiez que votre token Discord est correct
2. Vérifiez que votre bot a les permissions nécessaires
3. Consultez la [documentation discord.py](https://discordpy.readthedocs.io/)

## 📜 Licence

Créé avec Claude Code
Generated: 2026-10-03
