import discord
import random

TOKEN = 'OTI5NzIwNDI4NTkzODE1NTcy.Ydrbnw.DK_hswlFkPQzijV0NYiOUAJRAzc'

client = discord.Client()

@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
   username = str(message.author).split('#')[0]
   user_message = str(message.content)
   channel = str(message.channel.name)
   print(f'{username}: {user_message} ({channel})')

   if message.author == client.user:
      return
   if message.channel.name == 'general':
      if user_message.lower() == 'hello':
         await message.channel.send(f'Hello {username} !')
         return
      elif user_message.lower() == 'bye':
         await message.channel.send(f'Bye {username}, was really nice to meet you !')
      elif user_message.lower() == '!random':
         response = f'This is your random number: {random.randrange(1000000)}'
         await message.channel.send(response)
      elif user_message.lower() == '!help':
         await message.channel.send('Here are the following commands that you can use during this discord channel : \n 1.hello \n 2.bye \n 3. !random \n 4. !anywhere (Activate globally)')
         return

   if user_message.lower() == '!anywhere':
      await message.channel.send('This can be anywhere!')
      return

client.run(TOKEN)




