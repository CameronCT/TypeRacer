""" TypeRacer Bot """
# pylint: disable=C0103,C0301

import sys
import json
import discord
from cmds import info, stats

client = discord.Client()

""" Grab Config.json and make it a global variable """
with open('config.json') as data_file:
    CONFIG = json.load(data_file)

@client.event
async def on_ready():
    """ Debugging for when Bot is launched """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    """ When user sends a message """
    print("{}(#{}) / {}: {}".format(message.server, message.channel, message.author, message.content))

    if message.content.startswith('!help') or message.content.startswith('!h'):
        await info.execute(client, message)

    elif message.content.startswith('!stats') or message.content.startswith('!s'):
        await stats.execute(client, message)

    elif message.content.startswith('!exit'):
        if message.channel.permissions_for(message.author).kick_members:
            await client.send_message(message.channel, 'Closing')
            sys.exit()
        else:
            await client.send_message(message.channel, 'You are not authorized to perform this command!')

client.run(CONFIG['Discord'])
