""" TypeRacer Bot """
import sys
import urllib.request
import json
import discord
import datetime
import time

client = discord.Client() # pylint: disable=C0103
timer = time.time

""" Grab Config.json and make it a global variable """
with open('config.json') as data_file:
    CONFIG = json.load(data_file)

@client.event
async def on_ready():
    """ Debugging for when Bot is launched """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    """ When user sends a message """
    # pylint: disable=C0301
    print("{}(#{}) / {}: {}".format(message.server, message.channel, message.author, message.content))

    if message.content.startswith('!help') or message.content.startswith('!h'):
        await client.send_message(message.channel, 'Welcome! Type !stats to check a user\'s statistics!')

    elif message.content.startswith('!stats') or message.content.startswith('!s'):
        args = message.content.split(' ')
        diff = timer - time.time

        if diff < CONFIG['Delay']:
            await client.send_message(message.channel, 'Please wait a few seconds before using this command again!')

        if args[1] is None:
            await client.send_message(message.channel, '!stats <username')

        try:
            response = urllib.request.urlopen('http://typeracerdata.com/api?username=' + args[1])
            data = data = json.load(response)
        except ValueError:
            await client.send_message(message.channel, 'The username you have entered does not exist, please try again!')

        timezone = 'UTC'
        marathon = datetime.datetime.fromtimestamp(float(data['account']['marathon_start'])).strftime('%Y-%m-%d %H:%M:%S') + ' ' + timezone
        lastimport = datetime.datetime.fromtimestamp(float(data['account']['last_import'])).strftime('%Y-%m-%d %H:%M:%S') + ' ' + timezone

        if data:
            embed = discord.Embed(title='Statistics for ' + args[1], colour=0x00e5ee)
            embed.add_field(name='\u200b', value='__**General Statistics**__', inline=False)
            embed.add_field(name='Races:', value=data['account']['races'] + ' (' + data['account']['wins'] + ' won)')
            embed.add_field(name='Texts:', value=data['account']['texts_raced'])
            embed.add_field(name='Marathon:', value=data['account']['marathon_total'] + ' races on ' + marathon)
            embed.add_field(name='\u200b', value='__**WPM Statistics**__', inline=False)
            embed.add_field(name='Career Avg:', value='%.2f' % float(data['account']['wpm_life']) + ' WPM')
            embed.add_field(name='Highest:', value='%.2f' % float(data['account']['wpm_highest']) + ' WPM')
            embed.add_field(name='Text Bests:', value='%.2f' % float(data['account']['wpm_textbests']) + ' WPM')
            embed.add_field(name='Last 10:', value='%.2f' % float(data['account']['wpm_last10']) + ' WPM ' + '(' + '%.2f' % float(data['account']['wpm_bestlast10']) + ' peak)')
            embed.set_footer(text='Last Imported: ' + lastimport)

            await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('!exit'):
        if message.author.roles.permissions.kick_members:
            await client.send_message(message.channel, 'Closing')
            sys.exit()
        else:
            await client.send_message(message.channel, 'You are not authorized to perform this command!')

client.run(CONFIG['Discord'])
