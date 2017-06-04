"""
    File: info.py
    Description: Executes the command !h or !help
    Last Modified: 6/4/2017
"""
# pylint: disable=C0301

import discord

async def execute(client, message):
    """ Executes the command !help """

    embed = discord.Embed(colour=0x00e5ee)
    embed.set_author(name='Hello! I\'m a bot, beep beep bloop')
    embed.add_field(name='\u200b', value='__**General**__', inline=False)
    embed.add_field(name='!help', value='The command you are viewing\u200b', inline=True)
    embed.add_field(name='!stats', value='Check the statistics of a TypeRacer user', inline=True)


    await client.send_message(message.channel, embed=embed)
