import discord
from discord.ext import commands
from discord.utils import get
import json
import os
from datetime import datetime

# Configuration
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load suppliers data
def load_suppliers_data():
    with open('suppliers_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

SUPPLIERS_DATA = load_suppliers_data()

# Emojis
VERIFICATION_EMOJI = "✅"

# Colors
COLOR_PRIMARY = discord.Color.blue()
COLOR_SUCCESS = discord.Color.green()
COLOR_WARNING = discord.Color.gold()
COLOR_DANGER = discord.Color.red()
COLOR_INFO = discord.Color.blurple()

class ServerSetup:
    """Classe pour gérer la création du serveur"""

    @staticmethod
    async def create_roles(guild):
        """Créer les rôles du serveur"""
        roles_to_create = {
            'Admin': {'color': discord.Color.red(), 'permissions': discord.Permissions.all()},
            'Moderator': {'color': discord.Color.orange(), 'permissions': discord.Permissions(manage_messages=True, kick_members=True)},
            'Member': {'color': discord.Color.green(), 'permissions': discord.Permissions(view_channel=True, send_messages=True)},
            'Verified': {'color': discord.Color.blue(), 'permissions': discord.Permissions(view_channel=True)}
        }

        created_roles = {}
        for role_name, role_data in roles_to_create.items():
            if not get(guild.roles, name=role_name):
                role = await guild.create_role(
                    name=role_name,
                    color=role_data['color'],
                    permissions=role_data['permissions'],
                    reason='Automated server setup'
                )
                created_roles[role_name] = role
                print(f"✅ Rôle créé: {role_name}")
            else:
                created_roles[role_name] = get(guild.roles, name=role_name)

        return created_roles

    @staticmethod
    async def setup_server(guild):
        """Configuration complète du serveur"""
        print(f"\n🚀 Début de la configuration du serveur: {guild.name}")

        # 1. Créer les rôles
        print("\n📌 Création des rôles...")
        roles = await ServerSetup.create_roles(guild)

        # 2. Créer les catégories et canaux
        print("\n📂 Création des catégories et canaux...")

        categories_config = {
            '📜 RÈGLES & INFO': [
                ('📋-règles', 'Lisez et acceptez les règles du serveur'),
                ('📢-annonces-importantes', 'Annonces importantes du serveur'),
                ('ℹ️-informations', 'Informations utiles et FAQ'),
            ],
            '📢 ANNONCES': [
                ('🎯-annonces-générales', 'Annonces générales du serveur'),
                ('🆕-nouveautés', 'Nouvelles catégories et fournisseurs'),
                ('💡-suggestions', 'Suggestions et améliorations'),
            ],
            '💬 DISCUSSION': [
                ('💬-général', 'Discussion générale'),
                ('🤝-présentation', 'Présentez-vous et bienvenue'),
                ('💼-affaires', 'Discussion professionnelle'),
            ],
            '🤝 SUPPORT': [
                ('❓-questions', 'Posez vos questions'),
                ('🐛-problèmes', 'Signalez les problèmes'),
                ('📞-contact', 'Contacter le support'),
            ],
            '💄 FOURNISSEURS - COSMÉTIQUE': [
                ('📋-cosmétique', 'Liste des fournisseurs cosmétique'),
                ('💬-discussion-cosmétique', 'Discussion sur les fournisseurs'),
            ],
            '👗 FOURNISSEURS - TEXTILE FEMME': [
                ('📋-textile-femme', 'Liste des fournisseurs textile femme'),
                ('💬-discussion-textile-femme', 'Discussion textile femme'),
            ],
            '👔 FOURNISSEURS - TEXTILE HOMME': [
                ('📋-textile-homme', 'Liste des fournisseurs textile homme'),
                ('💬-discussion-textile-homme', 'Discussion textile homme'),
            ],
            '🎨 FOURNISSEURS - PERSONNALISATION': [
                ('📋-personnalisation', 'Services de personnalisation'),
                ('💬-discussion-personnalisation', 'Discussion personnalisation'),
            ],
            '🔌 FOURNISSEURS - ACCESSOIRES TECH': [
                ('📋-accessoires-tech', 'Accessoires technologiques'),
                ('💬-discussion-tech', 'Discussion accessoires tech'),
            ],
            '📱 FOURNISSEURS - TECH TÉLÉPHONE': [
                ('📋-tech-telephone', 'Équipements téléphoniques'),
                ('💬-discussion-telephone', 'Discussion tech téléphone'),
            ],
            '⚙️ MODÉRATION': [
                ('🛡️-modération', 'Canal de modération'),
                ('📊-logs', 'Logs du serveur'),
            ],
        }

        for category_name, channels in categories_config.items():
            # Créer la catégorie
            category = await guild.create_category(
                name=category_name,
                reason='Automated server setup'
            )

            # Créer les canaux
            for channel_name, channel_topic in channels:
                await guild.create_text_channel(
                    name=channel_name,
                    category=category,
                    topic=channel_topic,
                    reason='Automated server setup'
                )
                print(f"  ✅ Canal créé: {channel_name}")

        print("✅ Serveur configuré avec succès!\n")
        return roles

@bot.event
async def on_ready():
    print(f'\n✅ {bot.user} est connecté à Discord!')
    print(f'Latence: {bot.latency*1000:.0f}ms')
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="les fournisseurs | !help")
    )

@bot.event
async def on_member_join(member):
    """Message de bienvenue"""
    channel = discord.utils.get(member.guild.text_channels, name='🤝-présentation')
    if channel:
        embed = discord.Embed(
            title=f"👋 Bienvenue {member.name}!",
            description=f"""Bienvenue sur notre serveur **{member.guild.name}**!

Pour accéder au serveur, veuillez:
1. Lire les règles dans #📋-règles
2. Réagir avec ✅ pour accepter les règles
3. Explorez nos catégories de fournisseurs

Besoin d'aide? Posez vos questions dans #❓-questions""",
            color=COLOR_SUCCESS,
            timestamp=datetime.now()
        )
        embed.set_thumbnail(url=member.avatar.url)
        await channel.send(f"{member.mention}", embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
    """Ajouter le rôle Member quand un utilisateur accepte les règles"""
    if payload.emoji.name != VERIFICATION_EMOJI:
        return

    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if member.bot:
        return

    # Vérifier que c'est dans le bon canal
    channel = bot.get_channel(payload.channel_id)
    if channel.name != '📋-règles':
        return

    # Ajouter le rôle
    member_role = get(guild.roles, name='Member')
    verified_role = get(guild.roles, name='Verified')

    if member_role:
        await member.add_roles(member_role)
    if verified_role:
        await member.add_roles(verified_role)

    # Message de confirmation
    try:
        embed = discord.Embed(
            title="✅ Vérification complète!",
            description="Vous avez accepté les règles et avez accès au serveur.",
            color=COLOR_SUCCESS
        )
        await member.send(embed=embed)
    except:
        pass

@bot.command(name='setup', help='Configuration complète du serveur')
@commands.has_permissions(administrator=True)
async def setup_command(ctx):
    """Configurer le serveur complètement"""
    await ctx.send("🚀 Configuration du serveur en cours...")

    roles = await ServerSetup.setup_server(ctx.guild)

    # Obtenir le canal des règles
    rules_channel = get(ctx.guild.text_channels, name='📋-règles')

    if rules_channel:
        # Créer le message des règles
        embed = discord.Embed(
            title="📜 RÈGLES DU SERVEUR",
            description="""Bienvenue sur notre serveur **Discord Suppliers Marketplace**!

Veuillez lire et accepter les règles ci-dessous pour accéder au serveur.""",
            color=COLOR_PRIMARY,
            timestamp=datetime.now()
        )

        embed.add_field(
            name="1️⃣ Respect et Courtoisie",
            value="Soyez respectueux avec tous les membres du serveur. Aucune insulte, discrimination ou harcèlement.",
            inline=False
        )

        embed.add_field(
            name="2️⃣ Pas de Spam",
            value="Pas de messages répétitifs, de liens suspects ou de contenu publicitaire non autorisé.",
            inline=False
        )

        embed.add_field(
            name="3️⃣ Contenu Approprié",
            value="Pas de contenu violent, explicite ou illégal.",
            inline=False
        )

        embed.add_field(
            name="4️⃣ Utilisation des Canaux",
            value="Utilisez les canaux appropriés pour chaque type de discussion.",
            inline=False
        )

        embed.add_field(
            name="5️⃣ Vérification des Fournisseurs",
            value="Les fournisseurs affichés sont une sélection premium. Pour plus d'options, accédez au pack complet de 5000+ fournisseurs.",
            inline=False
        )

        embed.add_field(
            name="✅ ACCEPTER LES RÈGLES",
            value=f"Réagissez avec {VERIFICATION_EMOJI} ci-dessous pour accepter et accéder au serveur.",
            inline=False
        )

        embed.set_footer(text="Merci de respecter ces règles! 🙏")

        msg = await rules_channel.send(embed=embed)
        await msg.add_reaction(VERIFICATION_EMOJI)

        await ctx.send("✅ Serveur configuré avec succès!")

        # Créer un message dans le canal annonces
        announcements = get(ctx.guild.text_channels, name='🎯-annonces-générales')
        if announcements:
            embed_announce = discord.Embed(
                title="🎉 Serveur Discord Suppliers Marketplace",
                description="""Bienvenue sur votre nouvelle marketplace de fournisseurs!

**📦 Plus de 5000 fournisseurs** organisés par catégorie:
- 💄 Cosmétique
- 👗 Textile Femme
- 👔 Textile Homme
- 🎨 Personnalisation
- 🔌 Accessoires Tech
- 📱 Tech Téléphone

**🚀 Pour commencer:**
1. Vérifiez-vous dans #📋-règles
2. Explorez les catégories de fournisseurs
3. Contactez directement les fournisseurs

Besoin d'aide? Consultez #❓-questions""",
                color=COLOR_SUCCESS,
                timestamp=datetime.now()
            )
            await announcements.send(embed=embed_announce)

@bot.command(name='fournisseurs', help='Afficher les fournisseurs d\'une catégorie')
async def list_suppliers_command(ctx, *, category: str = None):
    """Afficher les fournisseurs"""
    if not category:
        categories = ', '.join(SUPPLIERS_DATA['categories'].keys())
        embed = discord.Embed(
            title="📋 Catégories disponibles",
            description=f"Utilisez: `!fournisseurs [catégorie]`\n\n{categories}",
            color=COLOR_INFO
        )
        return await ctx.send(embed=embed)

    category_lower = category.lower().replace(' ', '-')

    if category_lower not in SUPPLIERS_DATA['categories']:
        await ctx.send(f"❌ Catégorie '{category}' non trouvée")
        return

    category_data = SUPPLIERS_DATA['categories'][category_lower]

    embed = discord.Embed(
        title=f"{category_data['emoji']} {category_lower.replace('-', ' ').upper()}",
        description=category_data['description'],
        color=COLOR_PRIMARY
    )

    for i, supplier in enumerate(category_data['suppliers'], 1):
        supplier_info = f"""
**🌍 Pays:** {supplier['country']}
**🔗 Site Web:** {supplier['website'] if supplier['website'] != 'N/A' else '❌ Non disponible'}
**📞 Contact:** {supplier['contact']}
"""
        embed.add_field(
            name=f"{i}. {supplier['name']}",
            value=supplier_info,
            inline=False
        )

    embed.set_footer(
        text="⚠️  Sélection premium - Pack complet de 5000+ fournisseurs disponible"
    )

    await ctx.send(embed=embed)

@bot.command(name='info', help='Informations sur le serveur')
async def info_command(ctx):
    """Informations du serveur"""
    embed = discord.Embed(
        title=f"ℹ️ À propos de {ctx.guild.name}",
        description="Votre marketplace de fournisseurs premium",
        color=COLOR_INFO
    )

    embed.add_field(
        name="📊 Statistiques",
        value=f"""
**Membres:** {ctx.guild.member_count}
**Canaux:** {len(ctx.guild.channels)}
**Rôles:** {len(ctx.guild.roles)}
**Créé le:** {ctx.guild.created_at.strftime('%d/%m/%Y')}
""",
        inline=False
    )

    embed.add_field(
        name="📦 Fournisseurs",
        value=f"""
**Catégories:** {len(SUPPLIERS_DATA['categories'])}
**Sélection Premium:** {sum(len(cat['suppliers']) for cat in SUPPLIERS_DATA['categories'].values())} fournisseurs
**Pack Complet:** 5000+ fournisseurs
""",
        inline=False
    )

    embed.add_field(
        name="🔗 Catégories",
        value=", ".join([f"{data['emoji']} {key.replace('-', ' ').title()}" for key, data in SUPPLIERS_DATA['categories'].items()]),
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command(name='help', help='Aide du bot')
async def help_command(ctx):
    """Aide"""
    embed = discord.Embed(
        title="🆘 Aide & Commandes",
        color=COLOR_INFO
    )

    embed.add_field(
        name="⚙️ Administration",
        value="""
`!setup` - Configurer le serveur (Admin only)
`!info` - Informations du serveur
""",
        inline=False
    )

    embed.add_field(
        name="📋 Fournisseurs",
        value="""
`!fournisseurs [catégorie]` - Afficher les fournisseurs d'une catégorie
`!fournisseurs` - Lister toutes les catégories
""",
        inline=False
    )

    embed.add_field(
        name="❓ Besoin d'aide?",
        value="Posez vos questions dans #❓-questions ou contactez un modérateur.",
        inline=False
    )

    await ctx.send(embed=embed)

# Gestion des erreurs
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Erreur",
            description="Vous n'avez pas les permissions pour cette commande.",
            color=COLOR_DANGER
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        print(f"Erreur: {error}")

# Lancer le bot
if __name__ == '__main__':
    token = os.environ.get('DISCORD_TOKEN')
    if not token:
        print('❌ Erreur: Variable DISCORD_TOKEN non définie')
        print('Définissez votre token: export DISCORD_TOKEN="votre_token"')
    else:
        print("🚀 Lancement du bot...")
        bot.run(token)
