"""
    File: set.py
    Description: Executes the command !set
    Last Modified: 6/4/2017

    if args[1] is None or config['Commands'][args[1]] is None:
"""
# pylint: disable=C0301

async def execute(config, client, message):
    """ Executes the command !set """
    err = ''
    args = message.content.split(' ')

    if len(args) <= 2:
        err = 'SYNTAX: !set <cmd> <true/false>'

    if args[1] not in config['Commands']:
        err = 'The command you have entered could not be found, please try again!'

    if args[2] is not True and args[2] is not False:
        err = 'You can only set the command to true or false, please try again!'

    if err is None:
        await client.send_message(message.channel, 'You have set !' + cmd + ' to ' + str(val))
    else:
        await client.send_message(message.channel, err)
