@bot.event
async def on_message_reaction(member, reaction):
    ChID = 853602556281225236
    if reaction.emoji == ":crossed_swords:":
        WarriorRole = discord.utils.get(member.guid.roles, id=853606250653679638)
        await member.add_roles(WarriorRole)

@bot.command(name='dice', help='| Simule un ou plusieurs lancers de dés')
async def dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    embed = discord.Embed(
        title=":game_die: Lancer de dés", 
        description=f"{ctx.author.mention} a lancé les dés et a obtenu :\n{dice}")
    await ctx.send(embed=embed)


@bot.event
async def on_raw_reaction_add(payload):
    ChID = 853602556281225236
    if reaction.emoji == ":crossed_swords:":
        WarriorRole = discord.utils.get(member.guid.roles, id=853606250653679638)
        await member.add_roles(WarriorRole)