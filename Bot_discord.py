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
    Help_channel = client.get_channel(978272410069516359)

    # Si on écrit $help
    if message.channel == Help_channel and message.content.startswith('$help'):
        # le bot nous dira Bonjour!
        await Help_channel.send('Bonjour !')

    # Si on écrit del
    if message.content == "del":
        # le bot supprimera les 3 derniers messages
        await message.channel.purge(limit=7)

    if message.content.startswith('$dm'): # $dm @lapersonnequelonveut msg
        user = message.mentions[0]
        strs = message.content.split(" ")
        await user.send(strs[2:])

    await client.process_commands(message)

class Node:

    def __init__(self, question, keyword, list_child_node):
        self.question = question
        self.keyword = keyword
        self.list_child_node = list_child_node
    
    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
            if child.keyword in txt:
                child.user_response()

first_node = Node("Comment puis-je vous aider ?", "help", [Node("Sur quel sujet ?", "cours", []), Node("Sur quel domaine ?", "fichier", [])])

Node.user_response(first_node)

# default_intents = discord.Intents.default()
# default_intents.members = True
# client = discord.Client(intents=default_intents)

# @client.event
# async def on_member_join(member):
#     arrival_channel = client.get_channel(978295746325545010)
#     member.send(member.display_name,"a rejoint le serveur !")
    

# commande permettant de connecter son bot au serveur Discord
client.run("OTc4MjI5MzQ1MzU1MTk4NDY0.GQQW_r.r8xPYJiyOwtskNhupCanrq5FDGKNmY8fbLVgQI")
