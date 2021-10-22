# bot.py

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

description = '''Bot Discord réalisé par Alexis.R.\n Chaque commande doit être utilisée avec le préfixe "!" pour fonctionner.'''

intents = discord.Intents.default()
intents.reactions = True
intents.members = True
bot = commands.Bot(command_prefix='!', description=description, intents = intents)

# Évènements 

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f'Connexion réussie ! \n{bot.user} est connecté sur le serveur {guild.name} (ID : {guild.id})\n')

    channel = bot.get_channel(850484147965394964) # Affiche un message de confirmation dans le salon textuel "générale"
    await channel.send('Connexion au serveur réussie !')


@bot.event
async def on_member_join(member):
    RoleNew = discord.utils.get(member.guild.roles, id=851796151362387968) # Identifiant du rôle Recrue
    await member.add_roles(RoleNew)

    for guild in bot.guilds:
        channel = bot.get_channel(843196170620633140) # Affiche un message de confirmation dans le salon textuel "général"
        await channel.send(f'**Bienvenue à _{member.name}_ sur le serveur :tools: {guild.name}** !')

@bot.event
async def on_raw_reaction_add(payload):
    msgID = 853775690112565270

    if msgID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji =='⚔️':
            role = discord.utils.get(guild.roles, name="Chevalier")
        elif emoji =='🛡️':
            role = discord.utils.get(guild.roles, name="Paladin")
        elif emoji =='🎯':
            role = discord.utils.get(guild.roles, name="Archer")
        elif emoji =='🗡️':
            role = discord.utils.get(guild.roles, name="Assassin")
        await payload.member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    msgID = 853775690112565270

    if msgID == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji =='⚔️':
            role = discord.utils.get(guild.roles, name="Chevalier")
        elif emoji =='🛡️':
            role = discord.utils.get(guild.roles, name="Paladin")
        elif emoji =='🎯':
            role = discord.utils.get(guild.roles, name="Archer")
        elif emoji =='🗡️':
            role = discord.utils.get(guild.roles, name="Assassin")
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)

# Commandes utilisées sur le serveur et interprétées par le bot

@bot.command(name='ping', help='| Envoie un ping au bot')
async def ping(ctx):
    await ctx.send(f'Pong ! {round (bot.latency * 1000)}ms')

determine_flip = [1, 0]
@bot.command(name='coin', help='| Simule un lancer de pièce et affiche le résultat.')
async def coin(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(
            title=":coin: Pile ou face ", 
            description=f"{ctx.author.mention} a lancé une pièce et a obtenu **Pile** !")
        await ctx.send(embed=embed)
    
    else:
        embed = discord.Embed(
            title=":coin: Pile ou face ", 
            description=f"{ctx.author.mention} a lancé une pièce et a obtenu **Face** !")
        await ctx.send(embed=embed)

@bot.command(name='dice', help='| Simule un ou plusieurs lancers de dés')
async def dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    embed = discord.Embed(
        title=":game_die: Lancer de dés", 
        description=f"{ctx.author.mention} a lancé les dés et a obtenu :\n**{dice}**")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def role(ctx):
    embed = discord.Embed(
        title = "Réagissez avec un emoji pour ajouter un rôle.",
        description = f":crossed_swords: Chevalier \n :shield: Paladin \n :dart: Archer \n :dagger: Assassin"
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('⚔️') #Chevalier
    await msg.add_reaction('🛡️') #Paladin
    await msg.add_reaction('🎯') #Archer
    await msg.add_reaction('🗡️') #Assassin

@bot.command(name='encrypt', help='| Encrypte et décrypte un message ou un mot de passe')

async def encrypt(ctx):
    tableauSaisie=[]
    tableauLettre=[]
    tableauCrypto=[]
    toto=[]
    titi=[]
    tata=[]
    tab=[]

    def saisieTableauLettre(tab):
        """initialisation tableau lettre"""
        for i in range (65,91):
            z=chr(i)
            tab.append(z)
        return tab

    #Creation du tableau de reference
    saisieTableauLettre(tableauLettre)

    def saisieTableauCrypto(tableauCrypto):
        """initialisation tableau lettre crypto"""
        for i in range (66,91):
            c=chr(i)
            tableauCrypto.append(c)
        tableauCrypto.insert(25,"A") 
        return tableauCrypto 

    #Creation du tableau crypte
    saisieTableauCrypto(tableauCrypto)

    def saisieTableauSaisie(tab):
        """saisie du tableau de depart """
        for i in range (taille):
            x=str(input("Saisir la lettre à ajouter dans le tableau : "))
            tab.append(x)
        return tab

    def Crypt(tab):
        """changement de lettre Cryptage"""
        for i in range(0, taille):
            for j in range(0, 26):
                if tableauSaisie[i] == tableauLettre[j]:
                    l=tableauCrypto[j]
                    tab.append(l)
                    j = 26
        return tab
        
    def Decrypt(tab):
        """changement de lettre Decryptage """
        for i in range(0, taille):
            for j in range(0, 26):
                if toto[i] == tableauCrypto[j]:
                    m=tableauLettre[j]
                    tab.append(m)
                    j = 26
        return tab
        
    def Decrypt2(tab):
        """changement de lettre Decryptage """
        for i in range(0, taille):
            for j in range(0, 26):
                if tableauSaisie[i]  == tableauCrypto[j]:
                    m=tableauLettre[j]
                    tab.append(m)
                    j = 26
        return tab
    #affichage final

    #programme principal

    #nombre de lettre du mot à saisir
    await ctx.send(f'Entrez le nombre de lettres à saisir')
    taille = await bot.wait_for('message')
    #Mise en memoire du tableau saisie
    tableauSaisie = saisieTableauSaisie(tableauSaisie)

    Crypt=Crypt(toto)

    rep=str(input("veuillez saisir votre choix \n C pour Crypter \n D pour decrypter la saisie crypter \n DD pour decrypter seulement \n"))

    if (rep=='C'):
        print("le message ",tableauSaisie, "saisie devient crypté en ",Crypt)
    elif (rep=='D'):
        print("le message encrypté de ", Crypt, "donne ",Decrypt(titi))
    else :
        print("le message ",tableauSaisie, "saisie devient décrypté en ",Decrypt2(tata))


bot.run(TOKEN)