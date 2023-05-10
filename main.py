import discord
import os

TOKEN = ''
CHANNEL_ID = 888043542033862669
OUTPUT_FILE = 'output.txt' 
COMMAND_PREFIX = '!savechat'
OUTPUT_DIRECTORY = ''


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    print('------')

#------------------------------------------------Zapisywanie Historii chat---------------------------------------------------------

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID:
        with open(OUTPUT_FILE, 'a', encoding='utf-8') as file:
            file.write(f'{message.author.name}: {message.content}\n')

    if message.content.startswith(COMMAND_PREFIX):
        if message.author == client.user:
            return

        await message.channel.send(file=discord.File(OUTPUT_FILE))

#------------------------------------------------Zapisywanie zdjęć z chat---------------------------------------------------------

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID:
        if len(message.attachments) > 0:
            for attachment in message.attachments:
                await attachment.save(os.path.join(OUTPUT_DIRECTORY, attachment.filename))

client.run(TOKEN)