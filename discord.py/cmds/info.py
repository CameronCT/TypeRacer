"""
    File: info.py
    Description: Executes the command !h or !help
    Last Modified: 6/4/2017
"""
# pylint: disable=C0301

import discord
from methods import send_reply

async def execute(client, message, config):
    """ Executes the command !help """
    if config['Commands']['help'] is True or message.channel.permissions_for(message.author).kick_members or message.author.id == config['Owner']:
        embed = discord.Embed(colour=0x00e5ee)
        embed.set_author(name='Hello! I\'m a bot, beep beep bloop')
        embed.add_field(name='\u200b', value='__**General**__', inline=False)
        embed.add_field(name='!help', value='The command you are viewing\u200b', inline=True)
        embed.add_field(name='!stats', value='Check the statistics of a TypeRacer user', inline=True)
        embed.add_field(name='!dev', value='Find the latest updates to the bot', inline=True)

        await client.send_typing(message.channel)
        await client.send_message(message.channel, embed=embed)
    else:
        await client.send_typing(message.channel)
        await send_reply(client, message.channel, message.author.id, 'this command has been temporarily disabled!')
