import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

@client.event
async def on_ready():
    print('Music bot ready to play')

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTI5NzI5ODc5NzQ5MDY2ODIy.YdrkbA.At_4L8n6k1kiL5Y3ljHFi_cafFg")