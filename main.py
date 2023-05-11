import discord

TOKEN = 'MTA4NjMxODgxOTk1NTQ2MjIxNw.G0PZwF.r-O1Kc8iCfm3rL0P99Zz7lVFnfByFKaAZHCYVQ'
CHAT_HISTORY_FILE = 'chat_history.txt'

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Zapisywanie chat v0.2', client.user.name)
    print('------------------------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    channel = message.channel.name
    with open(CHAT_HISTORY_FILE, 'a', encoding='utf-8') as file:
        file.write(f'[{channel}] {message.author.name}: {message.content}\n')

    if message.content.startswith('!savechat'):
        await message.channel.send(file=discord.File(CHAT_HISTORY_FILE))

@client.event
async def on_message_edit(before, after):
    if before.author == client.user:
        return

    channel = before.channel.name
    with open(CHAT_HISTORY_FILE, 'a', encoding='utf-8') as file:
        file.write(f'[{channel}] Wiadomosc "{before.content}" napisana przez uzytkownika "{before.author.name}" edytowana przez "{before.author.name}" na "{after.content}"\n')

client.run(TOKEN)
