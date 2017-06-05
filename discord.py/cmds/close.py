"""
    File: set.py
    Description: Executes the command !set
    Last Modified: 6/4/2017

    if args[1] is None or config['Commands'][args[1]] is None:
"""
# pylint: disable=C0301

import sys
from methods import send_reply

async def execute_status(client, message, config):
    """ Executes the command !close """
    if message.channel.permissions_for(message.author).ban_members or message.author.id == config['Owner']:
        await send_reply(client, message.channel, message.author.id, 'I\'m a bot, beep, beep, beep. Error: Bot not found, piss and shit.')
        sys.exit()
    else:
        await send_reply(client, message.channel, message.author.id, 'you are not authorized to perform this command!')
