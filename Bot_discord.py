import discord
from discord.ext import commands

# Associe le prefix pour faire des commandes à /
client = commands.Bot(command_prefix="/")
# Enlève la commande help intégrée de base
client.remove_command("help")

# Affiche le message dans le terminal pour dire que le bot est fonctionnel
@client.event
async def on_ready():
    print('Bot is ready.')

# Commande help pour des informations sur les commandes du bot
@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title = "Commandes", description = "Utilise /help <commande> pour plus de détails sur une commande")

    embed.add_field(name='Aide', value='aide')
    embed.add_field(name='Liste des :', value='cours , tuto')
    embed.add_field(name='DM', value='dm')
    embed.add_field(name='Admin', value='clear , stop')

    await ctx.send(embed=embed)

@help.command()
async def aide(ctx):
    embed = discord.Embed(title = "Aide", description = "Envoie une liste de questions posées par le bot à l'utilisateur")
    embed.add_field(name='**Syntaxe**', value='``/aide``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def cours(ctx):
    embed = discord.Embed(title = "Cours", description = "Envoie la liste des cours écris proposés par le bot")
    embed.add_field(name='**Syntaxe**', value='``/cours``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def tuto(ctx):
    embed = discord.Embed(title = "Tuto", description = "Envoie la liste des cours en vidéo proposés par le bot")
    embed.add_field(name='**Syntaxe**', value='``/tuto``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def dm(ctx):
    embed = discord.Embed(title = "DM", description = "Envoie un message privé à la personne tag")
    embed.add_field(name='**Syntaxe**', value='``/dm @user message``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def clear(ctx):
    embed = discord.Embed(title = "Clear **(Commande admin)**", description = "Efface les 100 messages précédent du salon")
    embed.add_field(name='**Syntaxe**', value='``/clear``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def stop(ctx):
    embed = discord.Embed(title = "Stop **(Commande admin)**", description = "Stop le bot")
    embed.add_field(name='**Syntaxe**', value='``/stop``', inline=False)

    await ctx.send(embed=embed)

# Permet d'envoyer un dm à une personne
@client.command()
async def dm(ctx, user:discord.User, *, message=None):
    message = message
    embed = discord.Embed(title=message)
    await user.send(embed=embed)

# Enlève les 100 précédent messages du chat
@client.command()
@commands.is_owner()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

# Stop le bot
@client.command()
@commands.is_owner()
async def stop(ctx):
    exit()

# Lance le bot 
client.run("bot_token")