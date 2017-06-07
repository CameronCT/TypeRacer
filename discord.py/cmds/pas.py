"""
    File: pas.py
    Description: Executes the command !pissandshit
    Last Modified: 6/4/2017

    This command was a community demanded command, one of the
    users like's saying "piss and shit" and is now a command.
"""
# pylint: disable=C0301

from methods import send_reply

async def execute(client, message, config):
    """ Executes the command !pissandshit """
    if config['Commands']['pas'] is True or message.channel.permissions_for(message.author).kick_members or message.author.id == config['Owner']:
        await client.send_typing(message.channel)
        await client.send_message(message.channel, '🐸')
    else:
        await client.send_typing(message.channel)
        await send_reply(client, message.channel, message.author.id, 'this command has been temporarily disabled!')
