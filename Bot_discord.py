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

    embed.add_field(name='Aide', value='aide , aide_tips')
    embed.add_field(name='Liste des :', value='cours , tuto')
    embed.add_field(name='DM', value='dm')
    embed.add_field(name='Musique', value='join , kick , play , pause , resume , end')
    embed.add_field(name='Jeux', value='jp , pfc')
    embed.add_field(name='Bonus', value='bonus , punch , mdr , hi , secret , valorant , mario , pc , back , front')
    embed.add_field(name='Admin', value='suppr , stop')

    await ctx.send(embed=embed)

# Help Aide
@help.command()
async def aide(ctx):
    embed = discord.Embed(title = "Aide", description = "Envoie une liste de questions posées par le bot à l'utilisateur")
    embed.add_field(name='**Syntaxe**', value='``/aide``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def aide_tips(ctx):
    embed = discord.Embed(title = "Aide tips", description = "Envoie un exemple de conversation avec le bot")
    embed.add_field(name='**Syntaxe**', value='``/aide``', inline=False)

    await ctx.send(embed=embed)

# Help Liste des :
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

# Help DM
@help.command()
async def dm(ctx):
    embed = discord.Embed(title = "DM", description = "Envoie un message privé à la personne tag")
    embed.add_field(name='**Syntaxe**', value='``/dm @user message``', inline=False)

    await ctx.send(embed=embed)

# Help Musique
@help.command()
async def join(ctx):
    embed = discord.Embed(title = "Bot join", description = "Fait venir le bot dans le channel vocal")
    embed.add_field(name='**Syntaxe**', value='``/join``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def kick(ctx):
    embed = discord.Embed(title = "Kick", description = "Fait partir le bot du channel vocal")
    embed.add_field(name='**Syntaxe**', value='``/kick``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def play(ctx):
    embed = discord.Embed(title = "Play", description = "Le bot joue le lien envoyé")
    embed.add_field(name='**Syntaxe**', value='``/play lien_youtube``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def pause(ctx):
    embed = discord.Embed(title = "Pause", description = "Met en pause la musique en cours")
    embed.add_field(name='**Syntaxe**', value='``/pause``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def resume(ctx):
    embed = discord.Embed(title = "Resume", description = "Reprends la musique en cours")
    embed.add_field(name='**Syntaxe**', value='``/resume``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def end(ctx):
    embed = discord.Embed(title = "End", description = "Met fin à la musique")
    embed.add_field(name='**Syntaxe**', value='``/end``', inline=False)

    await ctx.send(embed=embed)

# Help Jeux
@help.command()
async def jp(ctx):
    embed = discord.Embed(title = "Juste Prix", description = "Jeu du juste prix existant entre 1 et 100")
    embed.add_field(name='**Syntaxe**', value='``/jp nombre``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def pfc(ctx):
    embed = discord.Embed(title = "Pierre Feuille Ciseaux", description = "Jeu du pierre feuille ciseaux")
    embed.add_field(name='**Syntaxe**', value='``/pfc (pierre / feuille / ciseaux)``', inline=False)

    await ctx.send(embed=embed)

# Help Bonus
@help.command()
async def bonus(ctx):
    embed = discord.Embed(title = "Bonus", description = "Envoie un lien bonus")
    embed.add_field(name='**Syntaxe**', value='``/bonus``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def punch(ctx):
    embed = discord.Embed(title = "Punch", description = "Envoie un gif de 'coup de poing'")
    embed.add_field(name='**Syntaxe**', value='``/punch``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def mdr(ctx):
    embed = discord.Embed(title = "Mdr", description = "Envoie un gif de 'mdr'")
    embed.add_field(name='**Syntaxe**', value='``/mdr``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def hi(ctx):
    embed = discord.Embed(title = "Hi", description = "Envoie un gif de 'hello/hi'")
    embed.add_field(name='**Syntaxe**', value='``/hi``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def secret(ctx):
    embed = discord.Embed(title = "Secret", description = "Envoie le secret pour avoir des bonnes notes")
    embed.add_field(name='**Syntaxe**', value='``/secret``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def valorant(ctx):
    embed = discord.Embed(title = "Valorant", description = "Envoie quel personnage de valorant tu es")
    embed.add_field(name='**Syntaxe**', value='``/valorant``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def mario(ctx):
    embed = discord.Embed(title = "Mario", description = "Envoie quel personnage de mario tu es")
    embed.add_field(name='**Syntaxe**', value='``/mario``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def pc(ctx):
    embed = discord.Embed(title = "Pourcentage cool", description = "Affiche à combien de % tu es cool")
    embed.add_field(name='**Syntaxe**', value='``/pc``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def back(ctx):
    embed = discord.Embed(title = "Back", description = "Affiche à combien de % tu es back")
    embed.add_field(name='**Syntaxe**', value='``/back``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def front(ctx):
    embed = discord.Embed(title = "front", description = "Affiche à combien de % tu es front")
    embed.add_field(name='**Syntaxe**', value='``/front``', inline=False)

    await ctx.send(embed=embed)

# Help Admin
@help.command()
async def suppr(ctx):
    embed = discord.Embed(title = "Suppr **(Commande admin)**", description = "Supprime 'nombre' message dans le channel")
    embed.add_field(name='**Syntaxe**', value='``/suppr nombre``', inline=False)

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
async def suppr(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

# Stop le bot
@client.command()
@commands.is_owner()
async def stop(ctx):
    exit()

# Lance le bot 
client.run("bot_token")