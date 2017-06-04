"""
    File: set.py
    Description: Executes the command !set
    Last Modified: 6/4/2017

    if args[1] is None or config['Commands'][args[1]] is None:
"""
# pylint: disable=C0301

from methods import user_string

async def execute(config, client, message):
    """ Executes the command !set """
    err = ''
    args = message.content.split(' ')

    if len(args) <= 2:
        await client.send_message(message.channel, user_string(message.author.id) + ', SYNTAX: !set <cmd> <true/false>')
    else:
        if args[1] not in config['Commands']:
            err = message.author + ', The command you have entered could not be found, please try again!'

        if args[2] not in ('true', 'false'):
            err = message.author + ', You can only set the command to true or false, please try again!'

        if not err:
            await client.send_message(message.channel, message.author + ', You have set !' + args[1] + ' to ' + args[2])
        else:
            await client.send_message(message.channel, err)
