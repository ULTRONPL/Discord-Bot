import discord
TOKEN, CHAT_HISTORY_FILE = '', 'chat_history.txt'
intents = discord.Intents.all()
client = discord.Client(intents=intents)
@client.event
async def on_message(message):
    if message.author==client.user: return
    with open(CHAT_HISTORY_FILE, 'a', encoding='utf-8') as file:
        file.write(f'[{message.channel.name}] {message.author.name}: {message.content}\n')
    if message.content.startswith('!savechat'): await message.channel.send(file=discord.File(CHAT_HISTORY_FILE))
@client.event
async def on_message_edit(before, after):
    if before.author==client.user: return
    with open(CHAT_HISTORY_FILE, 'a', encoding='utf-8') as f: f.write(f'[{before.channel.name}] Edited: "{before.content}" to "{after.content}"\n')
client.run(TOKEN)