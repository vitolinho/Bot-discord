from email.policy import default

from discord.ext import commands
from Arbre import *

client = commands.Bot(command_prefix="$")

@client.command()
async def coucou(ctx):
    await ctx.send("COUCOU !!!")

@client.command()
async def bot(ctx):
    await ctx.send("Bienvenue, voici la liste des commandes possible sur le serveur ! \n"+
    "$help : envoie une liste de question posée par le bot à l'utilisateur \n"+
    "$help_tips : envoie un exemple d'utilisation sur la commande $help \n"+
    "$admin : envoie un dm à un admin pour répondre au question de l'utilisateur\n"+
    "$bonus : envoie un lien bonus pour l'utilisateur \n"+
    "$cours : envoie la liste de cours proposé \n"+
    "$tuto : envoie la liste de cours en vidéo proposé par le bot")

# @client.command()
# async def help(ctx):
#     await ctx.send(node1)

@client.command()
async def bonus(ctx):
    await ctx.send("<https://www.youtube.com/watch?v=iik25wqIuFo>")
# @client.command()
# async def super_coucou(ctx, arg):
#     await ctx.send(arg)


@client.event
async def on_message(message):
    message.content = message.content.lower()

    # éviter les messages à l'infini
    if message.author == client.user:
        return
    # c'est le channel où les réponses du bot seront
    # changer '978272464683540530' en fonction de son channel
    Help_channel = client.get_channel(978234499177529364)

    # Si on écrit $help
    if message.channel == Help_channel and message.content.startswith('$help'):
        # le bot nous dira Bonjour!
        await Help_channel.send('Bonjour !')

    # Si on écrit del
    if message.content == "del":
        # le bot supprimera les 3 derniers messages
        await message.channel.purge(limit=7)

    if message.content.startswith('$dm'): # $dm @lapersonne msg
        user = message.mentions[0]
        strs = message.content.split(" ")
        await user.send(' '.join(strs[2:]))

    await client.process_commands(message)

# commande permettant de connecter son bot au serveur Discord
# changer par rapport à son bot OTc4MjI5MzQ1MzU1MTk4NDY0.GQQW_r.r8xPYJiyOwtskNhupCanrq5FDGKNmY8fbLVgQI
client.run("OTc4MjI5MzE5ODk5OTQ3MDA4.G2Nqaw.Nop0HfAjM4cAguagp7LdRiMmGSYVdKExyQjHA4")
