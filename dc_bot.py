import os
import discord
from dotenv import load_dotenv
import message_process as mc
from multiprocessing import Process

def getIntents():
    intents = discord.Intents()
    intents.messages = True
    intents.message_content = True
    intents.guilds = True
    intents.typing = True
    intents.reactions = True
    intents.auto_moderation = True
    return intents

def getTOKEN():
    if os.path.isfile(".env"):
        load_dotenv()
        token = os.getenv('DISCORD_TOKEN')
    else:
        print('Cannot find environment file\n')
        token = input('Please enter your bot token!\n')
        saveToken = input('Do you want to save this token?\n [Y/N] \n')
        if saveToken.upper() == 'Y':
            f = open(".env", "w")
            f.write(f'DISCORD_TOKEN={token}')
            f.close()
    return token

client = discord.Client(intents=getIntents())

@client.event
async def on_ready():
    for guild in client.guilds:
        print(f'{client.user.name} has connected to {guild.name}!')


@client.event
async def on_message(message):
    if not message.author.bot:
        reply = mc.Msg(message)
        if reply.type:
            await message.edit(suppress=True)
            reply.getVideo()
            if reply.replyVideo:
                rMsg = await message.channel.send(content=reply.replyVideo, reference=message)
                await rMsg.edit(suppress=False)


try:
    client.run(getTOKEN())
except:
    print('Error: The connection to the server cannot be established, please check your Token!')