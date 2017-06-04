"""
    File: set.py
    Description: Executes the command !set
    Last Modified: 6/4/2017

    if args[1] is None or config['Commands'][args[1]] is None:
"""
# pylint: disable=C0301

from methods import send_reply

async def execute(config, client, message):
    """ Executes the command !set """
    err = ''
    args = message.content.split(' ')

    if len(args) <= 2:
        await send_reply(client, message.channel, message.author.id, 'Please use the correct syntax. !set <cmd> <true/false>', True)
    else:
        if args[1] not in config['Commands']:
            err = send_reply(client, message.channel, message.author.id, 'the command you have entered could not be found, please try again!')

        if args[2] not in ('true', 'false'):
            err = send_reply(client, message.channel, message.author.id, 'you can only set the command to true or false, please try again!')

        if not err:
            await send_reply(client, message.channel, message.author.id, 'you have set !' + args[1] + ' to ' + args[2])
        else:
            await client.send_message(message.channel, err)
