import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.',intents=discord.Intents.all())

@client.event
async def on_ready():
   print('Bot started')
   await client.change_presence(activity=discord.Game(name="Slovní fotbal"))

@client.event
async def on_message(message):
    c_channel = client.get_channel(id kanalu kde bot bude fungovat)
    messages = [message async for message in c_channel.history(limit=2)]
    messageback = messages[1]
    messagenow = messages[0]
    messagebackstr = messageback.content[-1]
    messagenowstr = messagenow.content[0]

    if(messagebackstr != messagenowstr):
      await message.delete()
    else:
      return
    

client.run('token')