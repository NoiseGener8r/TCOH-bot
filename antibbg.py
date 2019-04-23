
import discord, random, re

TOKEN = 'NTcwMDYxNjQyOTQzOTU0OTQ0.XL8W1w.F6ivzzgr-PWVJ3dftsvFccmpZ5s'

client = discord.Client()
botprefix = '!'

command_list = ['help', 'shows this dialogue', 'yeet', 'prints yeet']

@client.event
async def on_message(message):
    message.content = re.sub('[^A-Za-z0-9]+!', ' ', message.content).lower().split(' ')
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.id == 544581480144175104 or message.author.id == 259493263679946774:
        chance_to_get_pissed = random.randint(0,10)
        if chance_to_get_pissed == 1:
            await message.channel.send('Oh. This guy.')
        else:
            return

    if message.content[0].startswith(str(botprefix)) and message.content[0] != str(botprefix):
        if message.content[0] == '!help' and len(message.content) <= 1:
            for i in command_list:
                if command_list.index(i) % 2 == 0:
                    await message.channel.send(i + ': ' +command_list[command_list.index(i) + 1])
                else:
                    await message.channel.send(' ')
                
                
        elif message.content[0] == '!help' and len(message.content) > 1:
            if message.content[1] in command_list:
                await message.channel.send(str(command_list[command_list.index(message.content[1])]) + ': ' + str(command_list[command_list.index(message.content[1])+1]))
            
            
        # await message.channel.send('No commands yet.')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
    
    