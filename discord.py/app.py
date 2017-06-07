""" 
    TypeRacer Bot
"""
# pylint: disable=C0103,C0301

import json
import discord
from cmds import info, stats, dev, status, close, report, pas

client = discord.Client()

""" Grab config.json and make it a global variable """
with open('config.json') as data_file:
    config = json.load(data_file)

@client.event
async def on_ready():
    """ Debugging for when Bot is launched """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    getMembers = sum(1 for x in client.get_all_members() if x.status.value != 'offline' and x.status.value != 'invisible')
    await client.change_presence(game=discord.Game(name='!help | ' + str(getMembers) + ' Online!'))

@client.event
async def on_message(message):

    """ When user sends a message """
    print("{}(#{}) / {}: {}".format(message.server, message.channel, message.author, message.content))

    if message.content.startswith('!help'):
        await info.execute(client, message, config)

    elif message.content.startswith('!stats'):
        await stats.execute(client, message, config)

    elif message.content.startswith('!report'):
        await report.execute(client, message, config)

    elif message.content.startswith('!pissandshit'):
        await pas.execute(client, message, config)

    elif message.content.startswith('!dev'):
        await dev.execute(client, message, config)

    elif message.content.startswith('!set'):
        await status.execute(client, message, config)

    elif message.content.startswith('!status'):
        await status.execute_status(client, message, config)

    elif message.content.startswith('!close'):
        await close.execute_status(client, message, config)

client.run(config['Discord'])

