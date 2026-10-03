import discord
from discord.ext import commands
import json
import os

# Configuration
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load suppliers data
def load_suppliers_data():
    with open('suppliers_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

SUPPLIERS_DATA = load_suppliers_data()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('------')

@bot.command(name='setup_suppliers', help='Setup the suppliers server with all categories and channels')
@commands.has_permissions(administrator=True)
async def setup_suppliers(ctx):
    """Create all supplier categories and channels"""
    guild = ctx.guild

    # Check if categories already exist
    existing_categories = [c.name for c in guild.categories]

    for category_id, category_data in SUPPLIERS_DATA['categories'].items():
        category_name = category_data['emoji'] + ' ' + category_id.replace('-', ' ').title()

        # Skip if category already exists
        if category_name in existing_categories:
            await ctx.send(f'❌ Catégorie {category_name} existe déjà')
            continue

        # Create category
        category = await guild.create_category(
            name=category_name,
            reason='Automated suppliers server setup'
        )

        # Create channel for suppliers list
        channel = await guild.create_text_channel(
            name='📋-fournisseurs',
            category=category,
            topic=category_data['description']
        )

        # Send supplier list
        embed = discord.Embed(
            title=f"{category_data['emoji']} {category_id.replace('-', ' ').title()}",
            description=category_data['description'],
            color=discord.Color.blue()
        )

        # Add suppliers to embed
        for i, supplier in enumerate(category_data['suppliers'], 1):
            supplier_info = f"""
**🌍 Pays:** {supplier['country']}
**🔗 Site Web:** {supplier['website'] if supplier['website'] != 'N/A' else 'Non disponible'}
**📞 Contact:** {supplier['contact']}
"""
            embed.add_field(
                name=f"{i}. {supplier['name']}",
                value=supplier_info,
                inline=False
            )

        embed.set_footer(
            text=f"⚠️  Ceci est une sélection premium - Accédez au pack COMPLET de 5000+ fournisseurs pour plus d'options | Session: {os.environ.get('CLAUDE_SESSION', 'N/A')[:20]}"
        )

        await channel.send(embed=embed)

        # Create "Full Pack" link channel
        pack_channel = await guild.create_text_channel(
            name='📦-pack-complet-5000',
            category=category,
            topic='Accédez au pack complet de 5000+ fournisseurs'
        )

        pack_embed = discord.Embed(
            title=f"📦 Pack Complet de Fournisseurs - {category_id.replace('-', ' ').title()}",
            description=f"""Cette catégorie affiche seulement une sélection premium de fournisseurs.

**Le pack complet contient plus de 5000 fournisseurs** dans ce domaine avec :
- ✅ Informations détaillées
- ✅ Contacts vérifiés
- ✅ Sites web et réseaux sociaux
- ✅ Classement par pays
- ✅ Évaluations et avis

**👉 [Accédez au pack complet des 5000+ fournisseurs](https://your-pack-link-here)**

*Powered by Claude Code - Suppliers Discord Server*
""",
            color=discord.Color.green()
        )

        await pack_channel.send(embed=pack_embed)

        await ctx.send(f'✅ Catégorie {category_name} créée avec succès!')

    # Create main info channel
    info_category = await guild.create_category(name='📌 INFORMATIONS')
    info_channel = await guild.create_text_channel(
        name='📢-bienvenue',
        category=info_category,
        topic='Bienvenue sur le serveur Discord Suppliers Marketplace'
    )

    welcome_embed = discord.Embed(
        title="🎉 Bienvenue sur Discord Suppliers Marketplace",
        description="""Bienvenue! Vous êtes sur le serveur officiel des **Fournisseurs Premium**.

**📌 À propos de ce serveur:**
- Sélection premium de fournisseurs par catégorie
- Plus de **5000 fournisseurs** disponibles dans le pack complet
- Fournisseurs vérifiés de différents pays
- Mise à jour régulière des contacts

**🔍 Comment utiliser ce serveur:**
1. Explorez les catégories disponibles
2. Consultez les fournisseurs recommandés
3. Contactez directement les fournisseurs via les informations fournies
4. Pour plus d'options, accédez au **pack complet de 5000+ fournisseurs**

**📦 Catégories disponibles:**
- 💄 Cosmétique
- 🎨 Personnalisation (Textile)
- 👗 Textile Femme
- 👔 Textile Homme
- 🔌 Accessoires Tech
- 📱 Tech Téléphone

*Powered by Claude Code*
""",
        color=discord.Color.gold()
    )

    await info_channel.send(embed=welcome_embed)

    await ctx.send('✅ Serveur configuré avec succès! Toutes les catégories ont été créées.')

@bot.command(name='list_suppliers', help='List all suppliers for a category')
async def list_suppliers(ctx, category: str = None):
    """List suppliers for a specific category"""
    if not category:
        categories = ', '.join(SUPPLIERS_DATA['categories'].keys())
        await ctx.send(f'Veuillez spécifier une catégorie: {categories}')
        return

    category_lower = category.lower().replace(' ', '-')

    if category_lower not in SUPPLIERS_DATA['categories']:
        await ctx.send(f'❌ Catégorie "{category}" non trouvée')
        return

    category_data = SUPPLIERS_DATA['categories'][category_lower]

    embed = discord.Embed(
        title=f"{category_data['emoji']} {category_lower.replace('-', ' ').title()}",
        description=category_data['description'],
        color=discord.Color.blue()
    )

    for i, supplier in enumerate(category_data['suppliers'], 1):
        supplier_info = f"""
**🌍 Pays:** {supplier['country']}
**🔗 Site Web:** {supplier['website'] if supplier['website'] != 'N/A' else 'Non disponible'}
**📞 Contact:** {supplier['contact']}
"""
        embed.add_field(
            name=f"{i}. {supplier['name']}",
            value=supplier_info,
            inline=False
        )

    embed.set_footer(text="⚠️  Pack complet disponible avec 5000+ fournisseurs")
    await ctx.send(embed=embed)

# Run the bot
if __name__ == '__main__':
    token = os.environ.get('DISCORD_TOKEN')
    if not token:
        print('Error: DISCORD_TOKEN environment variable not set')
        print('Please set your Discord bot token: export DISCORD_TOKEN="your_token_here"')
    else:
        bot.run(token)
