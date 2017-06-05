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

    if config['Commands']['report'] is True or message.channel.permissions_for(message.author).kick_members or message.author.id == config['Owner']:
        args = message.content.split(' ')

        reportstamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + ' UTC'

        if len(args) <= 2:
            await send_reply(client, message.channel, message.author.id, 'Please use the correct syntax. !report <username> <log>', True)
        else:
            embed = discord.Embed(colour=0x00e5ee, )
            embed.set_author(name='Reported by ' + message.author.nick)
            embed.set_thumbnail(url='https://d30y9cdsu7xlg0.cloudfront.net/png/1306-200.png')
            embed.add_field(name='User:', value=args[1], inline=False)
            embed.add_field(name='Message:', value=args[2], inline=False)
            embed.set_footer(text='Last commit on ' + reportstamp + '.')

            await client.send_message(config['Channels']['report'], embed=embed)
    else:
        await send_reply(client, message.channel, message.author.id, 'this command has been temporarily disabled!')
