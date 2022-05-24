from email.policy import default
import discord 

from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def coucou(ctx):
    await ctx.send("COUCOU !!!")

@client.command()
async def super_coucou(ctx, arg):
    await ctx.send(arg)
    
@client.event
async def on_message(message):
    message.content = message.content.lower()

    # éviter les messages à l'infini
    if message.author == client.user:
        return
    # c'est le channel où les réponses du bot seront
    # changer '978272464683540530' en fonction de son channel
    Help_channel = client.get_channel(978583666517241906)

    # Si on écrit $help
    if message.channel == Help_channel and message.content.startswith('$help'):
        # le bot nous dira Bonjour!
        await Help_channel.send('Bonjour !')

    # Si on écrit del
    if message.content == "del":
        # le bot supprimera les 3 derniers messages
        await message.channel.purge(limit=3)

    if message.content.startswith('$dm'): # $dm @lapersonne msg
        user = message.mentions[0]
        strs = message.content.split(" ")
        await user.send(' '.join(strs[2:]))

    await client.process_commands(message)

# commande permettant de connecter son bot au serveur Discord
# changer par rapport à son bot OTc4MjI5MzQ1MzU1MTk4NDY0.GQQW_r.r8xPYJiyOwtskNhupCanrq5FDGKNmY8fbLVgQI
client.run("OTc4MjI5MzQ1MzU1MTk4NDY0.GmtTj-.m-DZcC0V-XkPTCNoTMNgyFlxQjn2XbhPXguazU")