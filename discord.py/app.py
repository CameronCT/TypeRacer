""" TypeRacer Bot """
import sys
import urllib.request
import json
import discord

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
    args = message.content.split(' ', 1)
    if args[1]:
        cmd = args[1]

    """ When user sends a message """
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    if message.content.startswith('!stats') or message.content.startswith('!s'):
        if cmd is None:
            await client.send_message(message.channel, '!stats <username')

        response = urllib.request.urlopen('http://typeracerdata.com/api?username=' + cmd)
        data = data = json.load(response)

        if data is None:
            await client.send_message(message.channel, 'The username you have entered does not exist, please try again!') # pylint: disable=C0301

        elif data:
            embed = discord.Embed(title='Statistics for ' + cmd, colour=0xDEADBF)
            embed.add_field(name='\u200b', value='__**General Statistics**__', inline=False)
            embed.add_field(name='Races:', value=data['account']['races'] + ' (' + data['account']['wins'] + ' won)') # pylint: disable=C0301
            embed.add_field(name='Texts:', value=data['account']['texts_raced'])
            embed.add_field(name='Marathon:', value=data['account']['marathon_total'] + ' on ' + str(data['account']['marathon_start'])) # pylint: disable=C0301
            embed.add_field(name='\u200b', value='__**WPM Statistics**__', inline=False)
            embed.add_field(name='Career Avg:', value='%.2f' % float(data['account']['wpm_life']) + ' WPM') # pylint: disable=C0301
            embed.add_field(name='Highest:', value='%.2f' % float(data['account']['wpm_highest']) + ' WPM') # pylint: disable=C0301
            embed.add_field(name='Text Bests:', value='%.2f' % float(data['account']['wpm_textbests']) + ' WPM') # pylint: disable=C0301
            embed.add_field(name='Last 10:', value='%.2f' % float(data['account']['wpm_last10']) + ' WPM ' + '(' + '%.2f' % float(data['account']['wpm_bestlast10']) + ' peak)') # pylint: disable=C0301
            embed.set_footer(text='Last Imported: ' + str(data['account']['last_import']))

            await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!exit'):
        await client.send_message(message.channel, 'Closing')
        sys.exit()

client.run(CONFIG['Discord'])
