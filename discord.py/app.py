""" TypeRacer Bot """
import sys
import urllib.request
import json
import discord
import datetime

datetime.datetime.fromtimestamp(int("1284101485")
    ).strftime('%Y-%m-%d %H:%M:%S')

client = discord.Client() # pylint: disable=C0103

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

    args = message.content.split(' ')
    if args:
        cmd = args[1]

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!stats') or message.content.startswith('!s'):
        if cmd is None:
            await client.send_message(message.channel, '!stats <username')

        response = urllib.request.urlopen('http://typeracerdata.com/api?username=' + cmd)
        data = data = json.load(response)

        timezone = 'UTC'
        marathon = datetime.datetime.fromtimestamp(float(data['account']['marathon_start'])).strftime('%Y-%m-%d %H:%M:%S') + ' ' + timezone
        lastimport = datetime.datetime.fromtimestamp(float(data['account']['last_import'])).strftime('%Y-%m-%d %H:%M:%S') + ' ' + timezone

        if data:
            embed = discord.Embed(title='Statistics for ' + cmd, colour=0xDEADBF)
            embed.add_field(name='\u200b', value='__**General Statistics**__', inline=False)
            embed.add_field(name='Races:', value=data['account']['races'] + ' (' + data['account']['wins'] + ' won)')
            embed.add_field(name='Texts:', value=data['account']['texts_raced'])
            embed.add_field(name='Marathon:', value=data['account']['marathon_total'] + ' on ' + marathon)
            embed.add_field(name='\u200b', value='__**WPM Statistics**__', inline=False)
            embed.add_field(name='Career Avg:', value='%.2f' % float(data['account']['wpm_life']) + ' WPM')
            embed.add_field(name='Highest:', value='%.2f' % float(data['account']['wpm_highest']) + ' WPM')
            embed.add_field(name='Text Bests:', value='%.2f' % float(data['account']['wpm_textbests']) + ' WPM')
            embed.add_field(name='Last 10:', value='%.2f' % float(data['account']['wpm_last10']) + ' WPM ' + '(' + '%.2f' % float(data['account']['wpm_bestlast10']) + ' peak)')
            embed.set_footer(text='Last Imported: ' + lastimport)

            await client.send_message(message.channel, embed=embed)
        elif data is None or False:
            await client.send_message(message.channel, 'The username you have entered does not exist, please try again!')

    elif message.content.startswith('!exit'):
        sys.exit()
        await client.send_message(message.channel, 'Closing')

client.run(CONFIG['Discord'])
