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
    Help_channel = client.get_channel(978272464683540530)

    # Si on écrit $help
    if message.channel == Help_channel and message.content.startswith('$help'):
        # le bot nous dira Bonjour!
        await Help_channel.send('Bonjour !')

    # Si on écrit del
    if message.content == "del":
        # le bot supprimera les 3 derniers messages
        await message.channel.purge(limit=3)

    if message.content.startswith('$dm'): # $dm @lapersonnequelonveut msg
        user = message.mentions[0]
        strs = message.content.split(" ")
        await user.send(strs[2:])

    await client.process_commands(message)

# default_intents = discord.Intents.default()
# default_intents.members = True
# client = discord.Client(intents=default_intents)

# @client.event
# async def on_member_join(member):
#     arrival_channel = client.get_channel(978295746325545010)
#     member.send(member.display_name,"a rejoint le serveur !")
    

# commande permettant de connecter son bot au serveur Discord
client.run("OTc4MjI5MzQ1MzU1MTk4NDY0.GQQW_r.r8xPYJiyOwtskNhupCanrq5FDGKNmY8fbLVgQI")