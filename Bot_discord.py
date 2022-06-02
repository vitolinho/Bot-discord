import discord
from discord.ext import commands
from Arbre import *
import random 
from random import randint
import youtube_dl

Root = node1
questionPoser = False

default_intents = discord.Intents.default()
default_intents.members = True
# Défini le prefix nécessaire à utiliser pour appeler les commandes
client = commands.Bot(intents=default_intents,command_prefix="/")
# Enlève certaines commandes intégrées de base à discord pour pouvoir les personaliser
client.remove_command("help")

### A changer si vous êtes sur votre propre serveur :
## Ligne 470 : ID du channel help
## Ligne 524 : ID du channel general
## Ligne 534 : Token du bot

### Ligne 230 : Début des commandes du bot

## Hel
# Commande /help pour des informations sur les commandes du bot
@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title = "Commandes", description = "Utilise /help <commande> pour plus de détails sur une commande")

    embed.add_field(name='Aide', value='aide , aide_tips , back , reset , stop')
    embed.add_field(name='DM', value='dm')
    embed.add_field(name='Musique', value='join , leave , play , pause , resume , end')
    embed.add_field(name='Jeux', value='jp , pfc')
    embed.add_field(name='Bonus', value='bonus , punch , mdr , hi , secret , valorant , mario , pc , back , front')
    embed.add_field(name='Autres', value='suppr , clear')

    await ctx.send(embed=embed)

# Help - Aide
@help.command()
async def aide(ctx):
    embed = discord.Embed(title = "Aide", description = "Envoie une liste de questions posées par le bot à l'utilisateur")
    embed.add_field(name='**Syntaxe**', value='``/aide``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def aide_tips(ctx):
    embed = discord.Embed(title = "Aide - Exemple d'utilisation", description = "Envoie un exemple de conversation avec le bot")
    embed.add_field(name='**Syntaxe**', value='``/aide_tips``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def backconv(ctx):
    embed = discord.Embed(title = "Retour", description = "Reviens à la question précédente dans la discussion")
    embed.add_field(name='**Syntaxe**', value='``back``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def reset(ctx):
    embed = discord.Embed(title = "Réinitialisation", description = "Réinitialise la discussion")
    embed.add_field(name='**Syntaxe**', value='``reset``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def stop(ctx):
    embed = discord.Embed(title = "Stop", description = "Arrête la conversation avec le bot")
    embed.add_field(name='**Syntaxe**', value='``stop``', inline=False)

    await ctx.send(embed=embed)

# Help - DM
@help.command()
async def dm(ctx):
    embed = discord.Embed(title = "DM", description = "Envoie un message privé à la personne tag")
    embed.add_field(name='**Syntaxe**', value='``/dm @user message``', inline=False)

    await ctx.send(embed=embed)

# Help - Musique
@help.command()
async def join(ctx):
    embed = discord.Embed(title = "Bot join", description = "Fait venir le bot dans le channel vocal")
    embed.add_field(name='**Syntaxe**', value='``/join``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def leave(ctx):
    embed = discord.Embed(title = "Bot leave", description = "Fait partir le bot du channel vocal")
    embed.add_field(name='**Syntaxe**', value='``/leave``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def play(ctx):
    embed = discord.Embed(title = "Bot play music", description = "Le bot joue le lien envoyé")
    embed.add_field(name='**Syntaxe**', value='``/play lien_youtube``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def pause(ctx):
    embed = discord.Embed(title = "Bot pause music", description = "Met en pause la musique en cours")
    embed.add_field(name='**Syntaxe**', value='``/pause``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def resume(ctx):
    embed = discord.Embed(title = "Bot resume music", description = "Reprends la musique en cours")
    embed.add_field(name='**Syntaxe**', value='``/resume``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def end(ctx):
    embed = discord.Embed(title = "Bot end music", description = "Met fin à la musique")
    embed.add_field(name='**Syntaxe**', value='``/end``', inline=False)

    await ctx.send(embed=embed)

# Help - Jeux
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

# Help - Bonus
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

# Help - Autres
@help.command()
async def suppr(ctx):
    embed = discord.Embed(title = "Suppr", description = "Supprime 'nombre' message dans le channel")
    embed.add_field(name='**Syntaxe**', value='``/suppr nombre``', inline=False)

    await ctx.send(embed=embed)

@help.command()
async def clear(ctx):
    embed = discord.Embed(title = "clear", description = "Supprime tous les messages dans le channel")
    embed.add_field(name='**Syntaxe**', value='``/clear``', inline=False)

    await ctx.send(embed=embed)


## Début des commandes du bot
# aide_tips
@client.command(pass_context=True)
async def aide_tips(ctx):
    embed = discord.Embed(description = f"{ctx.author.mention} Voici un exemple de conversation avec le Bot")
    file = discord.File("screenshot/aide_tips.png", filename="image.png")
    embed.set_image(url=('attachment://image.png'))
    await ctx.send(file=file, embed=embed)

# punch
punch_gifs = ["https://c.tenor.com/1Sd82w25kacAAAAC/one-punch-man-punch.gif", "https://c.tenor.com/CLj5PsMhCLkAAAAC/naruto-sasuke.gif", "https://c.tenor.com/7JVff7vMCVkAAAAC/face-punch-punch.gif"]
punch_names = ["vous met une grosse golden chargé à 80 %"]

@client.command(pass_context=True)
async def punch(ctx):
    embed = discord.Embed(description = f"{ctx.author.mention} {(random.choice(punch_names))}")
    embed.set_image(url=(random.choice(punch_gifs)))
    await ctx.send(embed = embed)

# troll
troll_img= ["http://assets.stickpng.com/images/580b585b2edbce24c47b2a2a.png"]

@client.command(pass_context=True)
async def secret(ctx):
    embed = discord.Embed(title = "Trolololololooo", description = f"{ctx.author.mention} y'a pas de secret travaille dur !")
    embed.set_image(url=(random.choice(troll_img)))
    await ctx.send(embed = embed)

# mdr
mdr_gifs = ["https://c.tenor.com/wIxFiobxxbIAAAAd/john-jonah-jameson-lol.gif","https://c.tenor.com/TBk8shAAq8gAAAAC/laughin-lol.gif", "https://c.tenor.com/MCn_GMSSqAsAAAAd/lol-laughing-hysterically.gif", "https://c.tenor.com/Pgfo5pECixwAAAAC/laugh-lol.gif"]

@client.command(pass_context=True)
async def mdr(ctx):
    embed = discord.Embed(description = f"{ctx.author.mention}")
    embed.set_image(url=(random.choice(mdr_gifs)))
    await ctx.send(embed = embed)

# hi
hi_gifs = ["https://c.tenor.com/pvFJwncehzIAAAAM/hello-there-private-from-penguins-of-madagascar.gif", "https://c.tenor.com/UNTqMDwqh1gAAAAM/hello-hi.gif"]

@client.command(pass_context=True)
async def hi(ctx):
    embed = discord.Embed(description = f"Salut {ctx.author.mention}!")
    embed.set_image(url=(random.choice(hi_gifs)))
    await ctx.send(embed = embed)

# valorant
valorant_png = ["https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8a627ec10b57f4f2/5eb7cdc16509f3370a5a93b7/V_AGENTS_587x900_sage.png","https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt5599d0d810824279/6036ca30ce4a0d12c3ec1dfa/V_AGENTS_587x900_Astra.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt158572ec37653cf3/5eb7cdc19df5cf37047009d1/V_AGENTS_587x900_Cypher.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf11234f4775729b7/5ebf2c275e73766852c8d5d4/V_AGENTS_587x900_ALL_Sova_2.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blte5aefeb26bee12c8/60ca5aa30ece0255888d7faa/KAYO_KeyArt_587x900.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6f1392b30784e029/618d9da0d380f814d61f001c/WebUpdate_Chamber_KeyArt.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt53405c26141beff8/5f21fda671ec397ef9bf0894/V_AGENTS_587x900_KillJoy_.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6fef56a8182d0a81/5ebf2c2798f79d6925dbd6b4/V_AGENTS_587x900_ALL_Raze_2.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltd4080f8efb365751/5ff5660bb47cdf7fc7d6c3dc/V_AGENTS_587x900_yoru.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt4e5af408cc7a87b5/5eb7cdc17bedc8627eff8deb/V_AGENTS_587x900_Omen.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltceaa6cf20d328bd5/5eb7cdc1b1f2e27c950d2aaa/V_AGENTS_587x900_Jett.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt100d13bfa8286a3d/5eb7cdc11ea0c32e33b95fa2/V_AGENTS_587x900_Breach.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltc825c6589eda7717/5eb7cdc6ee88132a6f6cfc25/V_AGENTS_587x900_Viper.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt302fcb2b9628c376/5f7fa6ff8db9ea0f149ece0a/V_AGENTS_587x900_ALL_Skye.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt6577b1f58530e6b2/5eb7cdc121a5027d77420208/V_AGENTS_587x900_Reyna.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt26fcf1b5752514ee/5eb7cdbfc1dc88298d5d3799/V_AGENTS_587x900_Brimstone.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/bltf0200e1821b5b39f/5eb7cdc144bf8261a04d87f9/V_AGENTS_587x900_Phx.png", "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt516d37c6c84fcda0/625db737c9aa404b76ddd594/Fade_Key_Art_587x900_for_Website.png"]

@client.command(pass_context=True)
async def valorant(ctx):
    embed = discord.Embed(title = "Valorant", description = f"{ctx.author.mention} est :")
    embed.set_image(url=(random.choice(valorant_png)))
    await ctx.send(embed = embed)

# mario
mario_png = ["https://w7.pngwing.com/pngs/979/298/png-transparent-super-mario-bros-bowser-luigi-super-mario-super-mario-bros-nintendo-vertebrate-thumbnail.png", "https://e7.pngegg.com/pngimages/962/610/png-clipart-super-mario-character-illustration-new-super-mario-bros-super-mario-bros-2-mario-mammal-heroes.png", "https://cdn.imgbin.com/7/0/18/imgbin-luigi-s-mansion-2-mario-bros-boo-gTSa3Ui2tnaM3QrRrsRfAqXwt.jpg", "https://pngrow.com/preview/42359/super-mario-star-png", "https://w7.pngwing.com/pngs/923/449/png-transparent-super-mario-3d-land-super-mario-bros-3-super-mario-3d-world-bowser-princess-peach-mario-heroes-super-mario-bros-carnivoran-thumbnail.png", "https://w7.pngwing.com/pngs/350/292/png-transparent-super-mario-bros-super-mario-world-iphone-7-ice-power-s-super-mario-bros-hand-nintendo.png", "https://toppng.com/uploads/preview/fire-stephen-s-stuff-pinterest-bros-super-mario-mario-party-9-11563545937iogg3ozi4c.png", "https://e1.pngegg.com/pngimages/649/608/png-clipart-3d-yoshi-yoshi-3d-illustration-thumbnail.png", "https://e7.pngegg.com/pngimages/655/592/png-clipart-wario-land-super-mario-land-3-luigi-mario-wario-mario-party-island-tour-nintendo-video-game.png", "https://e7.pngegg.com/pngimages/9/832/png-clipart-mario-waluigi-bowser-wario-luigi-hand-nintendo-thumbnail.png", "https://e7.pngegg.com/pngimages/670/293/png-clipart-bowser-jr-super-mario-bros-3-paper-mario-sticker-star-bowser-food-heroes.png", "https://e7.pngegg.com/pngimages/432/975/png-clipart-super-mario-bros-bowser-luigi-mario-bros-carnivoran-super-mario-bros.png", "https://e7.pngegg.com/pngimages/154/579/png-clipart-toad-illustration-mario-party-8-mario-bros-toad-princess-peach-mario-bros-child-super-mario-bros.png", "https://e7.pngegg.com/pngimages/256/346/png-clipart-super-princess-peach-luigi-mario-princess-daisy-luigi-cartoon-fictional-character.png", "https://e7.pngegg.com/pngimages/791/755/png-clipart-princess-daisy-princess-peach-super-mario-land-mario-bros-mario-heroes-orange.png", "https://e7.pngegg.com/pngimages/882/770/png-clipart-mario-mario.png", "https://e7.pngegg.com/pngimages/99/464/png-clipart-super-mario-luigi-super-mario-bros-new-super-mario-bros-mario-luigi-superstar-saga-super-mario-galaxy-luigi-super-mario-bros-hand.png"]

@client.command(pass_context=True)
async def mario(ctx):
    embed = discord.Embed(title = "Mario's World", description = f"{ctx.author.mention} est :")
    embed.set_image(url=(random.choice(mario_png)))
    await ctx.send(embed = embed)

# suppr nb_de_messages
@client.command(pass_context=True)
async def suppr(ctx, arg):
    number_of_messages = arg
    messages = await ctx.channel.history(limit = int(number_of_messages) + 1).flatten()
    for each_message in messages:
        await each_message.delete()

# Supprime tous les messages du channel
@client.command()
async def clear(ctx, amount=10000):
    await ctx.channel.purge(limit=amount)

# Pourcentage de cool
@client.command(pass_context=True)
async def pc(ctx):
    embed = discord.Embed(title="pourcentage de cool", description=f"Tu es cool à {random.randrange(101)} % {ctx.author.mention}.")
    await ctx.send(embed = embed)

# Pourcentage de back end
@client.command(pass_context=True)
async def back(ctx):
    embed = discord.Embed(title="Calculateur de Back-end dans le sang", description=f"Tu es Back-end à {random.randrange(101)} % {ctx.author.mention}.")
    await ctx.send(embed=embed)

# Pourcentage de front end
@client.command(pass_context=True)
async def front(ctx):
    embed = discord.Embed(title="Calculateur de Front-end dans le sang", description=f"Tu es Front-end à {random.randrange(101)} % {ctx.author.mention}.")
    await ctx.send(embed=embed)

## Musique
# join
@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        voice_channel = ctx.message.author.voice.channel
        await voice_channel.connect()
    else:
        await ctx.send("Tu n'es pas connecté au channel vocal !")

# leave
@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("A plus dans le bus !")

# play
@client.command(pass_context=True)
async def play(ctx,url):
    if (ctx.voice_client):
        ctx.voice_client.stop()
        ffmpeg_options = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options':'-vn'}
        ydl_options = {'format':"bestaudio"}
        player = ctx.voice_client

        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**ffmpeg_options)
            player.play(source)

# pause
@client.command(pass_context=True)
async def pause(ctx):
    await ctx.send(f" {ctx.author.mention} Une petite pause s'impose !") 
    await ctx.voice_client.pause()

# resume
@client.command(pass_context=True)
async def resume(ctx):
    await ctx.send(f" {ctx.author.mention} C'est reparti zin !")
    await ctx.voice_client.resume()

# stop 
@client.command(pass_context=True)
async def end(ctx):
    await ctx.send(f" {ctx.author.mention} J'ai arrété la musique entièrement zin")
    await ctx.voice_client.stop()

# Mini jeux : le juste prix
prix = randint(1,100)
@client.command(pass_context=True)
async def jp(ctx, message : int):
    global prix
    answer = message
    if answer < 1 or answer > 100:
        await ctx.send(f"Erreur... Le prix est entre 1 et 100 ! {ctx.author.mention}")
    
    elif answer == prix:
        await ctx.send(f"Bravo 👏👏 {ctx.author.mention}! Le juste prix était: {prix} ")
        prix = randint(1,100)
    
    elif answer < prix:
        await ctx.send(f"Plus haut 👍👍 {ctx.author.mention} !")

    elif answer > prix:
        await ctx.send(f"Plus bas 👎👎{ctx.author.mention}!")

# Mini jeu : Pierre Feuille Ciseau
@client.command(pass_context=True)
async def pfc(ctx, message):
    answer = message.lower()
    pfc = ["pierre", "feuille", "ciseaux"]
    answer_ia = random.choice(pfc)
    if answer not in pfc:
        await ctx.send("C'est invalide. Veuillez entrez une de ces trois options: pierre, feuille, ciseaux !")
        return
    
    else:
        if answer_ia == answer:
            await ctx.send(f"Egalité 🤝🤝! Nous avons nous deux joués {answer}.")
        
        if answer_ia == "pierre":
            if answer == "feuille":
                await ctx.send(f"Tu as gagné 👏👏! J'ai joué {answer_ia} et tu as joué {answer} !")
        
        if answer_ia == "pierre":
            if answer == "ciseaux":
                await ctx.send(f"J'ai gagné 🥳🥳! J'ai joué {answer_ia} et tu as joué {answer}!")

        if answer_ia == "feuille" :
            if answer == "ciseaux":
                await ctx.send(f"Tu as gagné 👏👏! J'ai joué {answer_ia} et tu as joué {answer} !")

        if answer_ia == "feuille" :
            if answer == "pierre" :
                await ctx.send(f"J'ai gagné 🥳🥳! J'ai joué {answer_ia} et tu as joué {answer}!")

        if answer_ia == "ciseaux":
            if answer == "feuille" : 
               await ctx.send(f"J'ai gagné 🥳🥳! J'ai joué {answer_ia} et tu as joué {answer}!") 

        if answer_ia == "ciseaux":
            if answer == "pierre":
                await ctx.send(f"Tu as gagné 👏👏! J'ai joué {answer_ia} et tu as joué {answer} !")

# Rick roll
@client.command()
async def bonus(ctx):
    await ctx.send("<https://www.youtube.com/watch?v=iik25wqIuFo>")

# Commande principale du bot
@client.command()
async def aide(ctx):
    global questionPoser
    global Root
    global i
    questionPoser = True
    temp_root.clear()
    Root = node1
    i = 0
    await ctx.send(node1.question)

# Envoyer un message privé à un utilisateur
@client.command()
async def dm(ctx, user:discord.User, *, message=None):
    message = message
    await user.send(message)



temp_root = []
i = 0
@client.event
async def on_message(message):
    # éviter les messages à l'infini
    if message.author == client.user:
        return
    global i
    global Root
    global temp_root
    global questionPoser
    # C'est le channel où les réponses du bot seront
    Help_channel = client.get_channel(978583666517241906)
    if questionPoser == True:
        for child in Root.list_child_node:
            if len(Root.list_child_node) < 1:
                Root = node1
                questionPoser = False
                temp_root.clear()
                i = 0
                print("retour à la case départ")
                return 
            print("^^",Root.question)
            print("-->",child.keyword)
            print(i)
            for childKey in child.keyword:
                print(childKey)
                print(message.content)
                if childKey in message.content:
                    print(child.keyword)
                    temp_root.append(Root)
                    print(temp_root)
                    i = i + 1
                    print(i)
                    Root = child
                    await Help_channel.send(child.question)
                    return

#  Retour à la question d'avant si elle existe
    if message.content == "back" and len(temp_root) > 0 and len(Root.list_child_node) > 0:
        i = i - 1
        Root = temp_root[i]
        child = temp_root[i]
        temp_root.pop()
        print(child.question)
        await Help_channel.send(child.question)
#  On revient à la première question
    if message.content == "reset":
        Root = node1
        temp_root.clear()
        i = 0
        await Help_channel.send(node1.question)
        print(Root)
#  On arrête les questions du bot
    if message.content == "stop":
        Root = node1
        questionPoser = False
        temp_root.clear()
        i = 0
        await Help_channel.send("Au revoir ! ")

    await client.process_commands(message)

# Quand quelqu'un rejoins le serveur lui indique la commande à entrer pour avoir des indications sur l'utilisation du bot
@client.event
async def on_member_join(member):
    landing = client.get_channel(978583486963257437)
    await landing.send(f"Bienvenue, pour voir les commandes du bot, tapez /help dans le channel #help-me")

# Envoie un message dans le terminal pour dire que le bot est prêt à être utilisé
@client.event
async def on_ready():
    print("Le bot est connecté et prêt à être utilisé")

# Commande permettant de connecter son bot au serveur Discord
# Token du bot
client.run("OTc4MjI5MzQ1MzU1MTk4NDY0.GPwcuP.PCxrgZxv7vbJP_HQnO7w3R_uwFQn44sFjuj1QM")