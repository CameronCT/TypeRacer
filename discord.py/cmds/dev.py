"""
    File: dev.py
    Description: Executes the command !dev
    Last Modified: 6/4/2017
"""
# pylint: disable=C0301

import datetime
import json
import urllib.request
import discord

async def execute(client, message):
    """ Executes the command !stats """

    try:
        response = urllib.request.urlopen('https://api.github.com/repos/CameronCT/TypeRacer/git/refs/heads/master')
        datarepo = json.load(response)
    except ValueError:
        await client.send_message(message.channel, 'Uh oh, an unexpected error has occured with GitHub. Please try again later!')

    if datarepo:
        try:
            response = urllib.request.urlopen(datarepo['object']['url'])
            data = json.load(response)
        except ValueError:
            await client.send_message(message.channel, 'Uh oh, an unexpected error has occured with GitHub. Please try again later!')

        if data:

            embed = discord.Embed(colour=0x00e5ee, url='https://github.com/CameronCT/TypeRacer/commit/' + data['sha'])
            embed.set_author(name='GitHub', icon_url='https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png')
            embed.set_thumbnail(url='https://avatars3.githubusercontent.com/u/11495748')
            embed.add_field(name='Last commit: ' + data['sha'] + ' on ' + data['committer']['date'] + '.', value='\u200b', inline=False)

            await client.send_message(message.channel, embed=embed)
