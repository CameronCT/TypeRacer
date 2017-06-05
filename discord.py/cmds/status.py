"""
    File: status.py
    Description: Executes the command !set
    Last Modified: 6/4/2017

    if args[1] is None or config['Commands'][args[1]] is None:
"""
# pylint: disable=C0301

from methods import send_reply

async def execute(client, message, config):
    """ Executes the command !set """
    if message.channel.permissions_for(message.author).kick_members or message.author.id == config['Owner']:
        err = ''
        args = message.content.split(' ')

        if len(args) <= 2:
            await send_reply(client, message.channel, message.author.id, 'Please use the correct syntax. **!set <help/stats/dev/etc> <on/off>**', True)
        else:
            if args[1] not in config['Commands']:
                err = 'the command you have entered could not be found, please try again!'

            if args[2].lower() not in ('on', 'off'):
                err = 'you can only set the command to true or false, please try again!'

            if not err:
                cmd = True
                if args[2].lower() == 'on':
                    cmd = True
                else:
                    cmd = False

                config['Commands'][args[1]] = cmd


                await send_reply(client, message.channel, message.author.id, 'you have set **!' + args[1] + '** to **' + args[2] + '**!')
            else:
                await send_reply(client, message.channel, message.author.id, err)
    else:
        await send_reply(client, message.channel, message.author.id, 'you are not authorized to perform this command!')


async def execute_status(client, message, config):
    """ Executes the command !set """
    err = ''
    args = message.content.split(' ')

    if len(args) <= 1:
        await send_reply(client, message.channel, message.author.id, 'Please use the correct syntax. **!status <help/stats/dev/etc>**', True)
    else:
        if args[1] not in config['Commands']:
            err = 'the command you have entered could not be found, please try again!'

        if not err:
            cmd = 'On'
            if config['Commands'][args[1]] is True:
                cmd = 'On'
            else:
                cmd = 'Off'

            await send_reply(client, message.channel, message.author.id, 'the command **!' + args[1] + '** is set to **' + cmd + '**!')
        else:
            await send_reply(client, message.channel, message.author.id, err)
