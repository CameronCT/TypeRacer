"""
    File: stats.py
    Description: Executes the command !s or !stats
    Last Modified: 6/4/2017
"""
# pylint: disable=C0301

import datetime
import json
import urllib.request
import discord
from methods import send_reply

async def execute(client, message, config):
    """ Executes the command !stats """

    if config['Commands']['stats'] is True or message.channel.permissions_for(message.author).kick_members or message.author.id == config['Owner']:
        args = message.content.split(' ')

        if len(args) is 1:
            await send_reply(client, message.channel, message.author.id, 'Please use the correct syntax. !stats <username>', True)
        else:
            try:
                response = urllib.request.urlopen('http://typeracerdata.com/api?username=' + args[1])
                data = json.load(response)
            except ValueError:
                await send_reply(client, message.channel, message.author.id, 'the username you have entered does not exist, please try again!')

            if data:
                timezone = 'UTC'
                marathon = datetime.datetime.fromtimestamp(float(data['account']['marathon_start'])).strftime('%Y-%m-%d %H:%M:%S') + ' ' + timezone
                lastimport = datetime.datetime.fromtimestamp(float(data['account']['last_import'])).strftime('%Y-%m-%d %H:%M:%S') + ' ' + timezone

                embed = discord.Embed(colour=0x00e5ee)
                embed.set_author(name='Statistics for ' + args[1], icon_url='http://data.typeracer.com/misc/pic?uid=tr:' + args[1] + '&size=large&bpc=1')
                embed.set_thumbnail(url='http://data.typeracer.com/misc/pic?uid=tr:' + args[1] + '&size=large&bpc=1')
                embed.add_field(name='\u200b', value='__**General Statistics**__', inline=False)
                embed.add_field(name='Races:', value=data['account']['races'] + ' (' + data['account']['wins'] + ' won)')
                embed.add_field(name='Texts:', value=data['account']['texts_raced'])
                embed.add_field(name='Marathon:', value=data['account']['marathon_total'] + ' races on ' + marathon)
                embed.add_field(name='\u200b', value='__**WPM Statistics**__', inline=False)
                embed.add_field(name='Career Avg:', value='%.2f' % float(data['account']['wpm_life']) + ' WPM')
                embed.add_field(name='Highest:', value='%.2f' % float(data['account']['wpm_highest']) + ' WPM')
                embed.add_field(name='Text Bests:', value='%.2f' % float(data['account']['wpm_textbests']) + ' WPM')
                embed.add_field(name='Last 10:', value='%.2f' % float(data['account']['wpm_last10']) + ' WPM ' + '(' + '%.2f' % float(data['account']['wpm_bestlast10']) + ' peak)')
                embed.set_footer(text='Updated on ' + lastimport)

                await client.send_typing(message.channel)
                await client.send_message(message.channel, embed=embed)
    else:
        await client.send_typing(message.channel)
        await send_reply(client, message.channel, message.author.id, 'this command has been temporarily disabled!')
