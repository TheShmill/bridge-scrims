import discord
from discord.ext import commands, tasks
from random import shuffle
import asyncio
client=commands.Bot(command_prefix="!",intents=discord.Intents.all())

@tasks.loop(seconds=30)
async def member_count():
    count = client.guilds[0].member_count
    output_channel = client.get_channel(779910959006351360)
    await output_channel.edit(name = f'Members: {count}')

@client.event
async def on_ready():
    print('connected to discord')
    member_count.start()

@client.command(aliases=["roll","captains","teams","caps","team","captain","r"])
@commands.cooldown(1,0.5,commands.BucketType.channel)
async def queue(ctx):
    if ctx.message.author.voice is None:
        await ctx.send("Please join a VC before using this command")
        return
    vc=ctx.message.author.voice.channel
    if 'queue' not in vc.category.name.lower():
        return
    if 'queue' not in ctx.message.channel.category.name.lower():
        return
    members=vc.members
    if len(members)<vc.user_limit:
        await ctx.send("This queue is not full yet.")
        return
    stier=[]
    atier=[]
    btier=[]
    ctier=[]
    dtier=[]
    for member in members:
        for role in member.roles:
            if role.id==760148463349661719:
                stier.append(member.display_name)
            elif role.id==760148463458713641:
                atier.append(member.display_name)
            elif role.id==760148463601844236:
                btier.append(member.display_name)
            elif role.id==760148464574136330:
                ctier.append(member.display_name)
            elif role.id==760196093698113566:
                dtier.append(member.display_name)
    shuffle(stier)
    shuffle(atier)
    shuffle(btier)
    shuffle(ctier)
    shuffle(dtier)
    members=[]
    for member in stier:
        members.append(member)
    for member in atier:
        members.append(member)
    for member in btier:
        members.append(member)
    for member in ctier:
        members.append(member)
    for member in dtier:
        members.append(member)
    captain1=members[1]
    captain2=members[0]
    embed=discord.Embed(title="Team Captains:")
    embed.add_field(name="First Captain",value=captain1)
    embed.add_field(name="Second Captain",value=captain2)
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1,0.5,commands.BucketType.channel)
async def random(ctx):
    if ctx.message.author.voice is None:
        await ctx.send("Please join a VC before using this command")
        return
    vc = ctx.message.author.voice.channel
    if "queue" not in ctx.message.channel.category.name.lower():
        return
    if "queue" not in vc.category.name.lower():
        return
    members = vc.members 
    if len(members) < vc.user_limit:
        await ctx.send("This queue is not full yet")
        return
    shuffle(members)
    captain1=members[0].display_name
    captain2=members[1].display_name
    embed = discord.Embed(title="Team Captains:")
    embed.add_field(name="First Captain",value=captain1)
    embed.add_field(name="Second Captain",value=captain2)
    await ctx.send(embed = embed)

client.run("")
