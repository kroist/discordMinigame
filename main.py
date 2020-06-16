from discord.ext import commands

client = commands.Bot(command_prefix='!')

guessed_word = 'LOL_KEK'
word_ptr = 0
channel_id = 0

@client.event
async def on_ready():
    guild_list = client.guilds
    print('Logged in as {0.user} on '.format(client))
    for guild in guild_list:
        print(guild.name)

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    global channel_id, word_ptr, guessed_word
    print(message.channel.id, channel_id)
    if message.channel.id != channel_id:
        return
    print(message.channel.id)
    print('Message from {0.author}: {0.content}'.format(message))
    print(message.content)
    print(guessed_word[word_ptr])
    if message.content == guessed_word[word_ptr]:
        word_ptr = (word_ptr + 1) % len(guessed_word)
        if word_ptr == 0:
            await message.channel.send('GOOD')
    else:
        await message.delete()
        await message.author.send('ууу сука')


@client.command()
@commands.has_permissions(administrator=True)
async def setBot(ctx, channelId, word):
    channelId = channelId[2:-1]
    print(channelId)
    global channel_id, guessed_word, word_ptr
    channel_id = int(channelId)
    print(word)
    guessed_word = word
    word_ptr = 0


f = open('botToken.txt', 'r')
botToken = f.read()
print(botToken)
client.run(botToken)
