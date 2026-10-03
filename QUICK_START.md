# ⚡ Démarrage rapide - 5 minutes

## 🎯 Résumé

Vous avez un **bot Discord complet** qui crée un serveur professionnel de A à Z avec:
- ✅ Système de vérification (règles à cocher)
- ✅ Rôles automatiques
- ✅ 9 catégories organisées
- ✅ 25+ canaux
- ✅ Base de fournisseurs (5000+)

## 📝 Les 5 étapes

### 1️⃣ Créer un Bot Discord (2 min)

[Allez ici →](https://discord.com/developers/applications)

1. "New Application" → Nommez-le
2. Onglet "Bot" → "Add Bot"
3. Copiez le **TOKEN**
4. Activez "Message Content Intent"
5. Allez à "OAuth2" → "URL Generator"
6. Cochez: `bot`
7. Cochez les permissions:
   - ☑️ Manage Channels
   - ☑️ Manage Roles
   - ☑️ Send Messages
   - ☑️ Add Reactions
8. Copiez le lien et invitez le bot sur votre serveur

### 2️⃣ Configurer le token (1 min)

```bash
# Ouvrir .env
nano .env

# Ajouter votre token
DISCORD_TOKEN=votre_token_ici
```

### 3️⃣ Installer les dépendances (1 min)

```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer le bot (1 min)

```bash
python bot.py
```

Vous devriez voir:
```
✅ YourBot est connecté à Discord!
```

### 5️⃣ Configurer le serveur (30 sec)

Sur votre serveur Discord, écrivez:
```
!setup
```

**LE BOT VA CRÉER:**
- ✅ 9 catégories
- ✅ 25+ canaux
- ✅ 4 rôles
- ✅ Système de vérification
- ✅ Messages de bienvenue
- ✅ Annonces

## 🎮 Commandes importantes

```
!help
```
Affiche l'aide

```
!fournisseurs cosmétique
```
Affiche les fournisseurs cosmétique

```
!info
```
Informations du serveur

## ✅ Verification System

1. Nouvel utilisateur arrive → #🤝-présentation
2. Lit les règles → #📋-règles
3. Clique ✅ pour accepter
4. **Obtient automatiquement** les rôles Member + Verified
5. Accès complet au serveur

## 📦 Données incluses

| Catégorie | Fournisseurs |
|-----------|-------------|
| 💄 Cosmétique | 5 |
| 👗 Textile Femme | 5 |
| 🎨 Personnalisation | 4 |
| 👔 Textile Homme | 4 |
| 🔌 Accessoires Tech | 3 |
| 📱 Tech Téléphone | 3 |
| **Total** | **24** |
| **Pack Complet** | **5000+** |

## 🆘 Si ça ne marche pas

### Le bot ne démarre pas
```bash
# Vérifiez le token
echo $DISCORD_TOKEN

# Vérifiez discord.py
pip install discord.py --upgrade
```

### Les canaux ne se créent pas
- Vérifiez que le bot a les permissions (admin temporaire)
- Essayez: `!setup` à nouveau

### Les réactions ne fonctionnent pas
- Vérifiez "Message Content Intent" dans Developer Portal

## 📁 Fichiers importants

```
.env                  → Votre token (NE PAS COMMITTER)
bot.py               → Le bot principal
suppliers_data.json  → Les données des fournisseurs
README.md            → Documentation complète
```

## 🔐 Sécurité

⚠️ **IMPORTANT:**
- Ne partagez **JAMAIS** votre token
- Gardez `.env` **SECRET**
- Supprimez le token si compromis et créez un nouveau

## 🚀 Vous êtes prêt!

C'est tout! Votre serveur Discord est maintenant:
- ✅ Complètement automatisé
- ✅ Professionnel
- ✅ Dynamique
- ✅ Prêt à accueillir des utilisateurs

**Pour plus de détails:** Consultez `README.md`

---

**Questions?** Consultez #❓-questions sur votre serveur Discord! 😎
