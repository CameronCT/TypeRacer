"""
    File: import.py
    Description: Executes the command !import
    Last Modified: 6/4/2017
"""
# pylint: disable=C0301

import datetime
import json
import urllib.request
import discord
from methods import send_reply

async def execute(client, message, config):
    """ Executes the command !import """

    if config['Commands']['import'] is True or message.channel.permissions_for(message.author).kick_members or message.author.id == config['Owner']:
        args = message.content.split(' ')

        if len(args) is 1:
            await send_reply(client, message.channel, message.author.id, 'Please use the correct syntax. !import <username>', True)
        else:
            try:
                response = urllib.request.urlopen('http://www.typeracerdata.com/import?username=' + args[1])
            except ValueError:
                await send_reply(client, message.channel, message.author.id, 'the username you have entered does not exist, please try again!')

            if response:
                await client.send_typing(message.channel)
                await send_reply(client, message.channel, message.author.id, 'you have successfully added **' + args[1] + '** to the import.')
    else:
        await client.send_typing(message.channel)
        await send_reply(client, message.channel, message.author.id, 'this command has been temporarily disabled!')
