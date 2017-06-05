"""
    File: stats.py
    Description: Executes the command !s or !stats
    Last Modified: 6/4/2017
"""
# pylint: disable=C0301

import time
import datetime
import discord
from methods import send_reply

async def execute(client, message, config):
    """ Executes the command !stats """
    args = message.content.split(' ')

    reportstamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + ' UTC'

    if len(args) <= 2:
        await send_reply(client, message.channel, message.author.id, 'Please use the correct syntax. !report <username> <log>', True)
    else:
        embed = discord.Embed(colour=0xFF0000)
        embed.add_field(name='User', value=args[1], inline=False)
        embed.add_field(name='Message', value=args[2], inline=False)
        embed.set_footer(text='Reported by ' + message.author.nick + ' on ' + reportstamp + '.')

        await client.send_message(client.get_channel(config['Channels']['report']), embed=embed)
