# Ne pas utiliser
# bot.py

import os
import random
import discord
import aiohttp
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

description = '''Bot Discord réalisé par Alexis.R.'''

bot = commands.Bot(command_prefix='!', description=description)

# Évènements 

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f'Connexion réussie ! \n{bot.user} est connecté sur le serveur {guild.name} (ID : {guild.id})\n')

    channel = bot.get_channel(850484147965394964) # Affiche un message de confirmation dans le salon textuel "générale"
    await channel.send('Connexion au serveur réussie !')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="851796151362387968") # Identifiant du rôle Recrue
    await bot.add_roles(role)

    channel = bot.get_channel(843196170620633140) # Affiche un message de confirmation dans le salon textuel "général" (différent de "générale")
    await channel.send('Rôle Recrue ajouté !')

# Commandes utilisées sur le serveur et interprétées par le bot

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong ! {round (bot.latency * 1000)}ms')

determine_flip = [1, 0]
@bot.command(name='coin', help='Simule un lancer de pièce et affiche le résultat.')
async def coin(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title=":coin: Pile ou face ", description=f"{ctx.author.mention} a lancé une pièce et a obtenu **Pile** !")
        await ctx.send(embed=embed)
    
    else:
        embed = discord.Embed(title=":coin: Pile ou face ", description=f"{ctx.author.mention} a lancé une pièce et a obtenu **Face** !")
        await ctx.send(embed=embed)

@bot.command(name='dice', help='Simule un ou plusieurs lancers de dés')
async def dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    embed = discord.Embed(title=":game_die: Lancer de dés", description=f"{ctx.author.mention} a lancé les dés et a obtenu :\n"+dice(', '.join(dice)))
    await ctx.send(embed=embed)
 
bot.run(TOKEN)