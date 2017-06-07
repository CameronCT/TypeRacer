"""
    File: pas.py
    Description: Executes the command !pissandshit
    Last Modified: 6/4/2017

    This command was a community demanded command, one of the
    users like's saying "piss and shit" and is now a command.
"""
# pylint: disable=C0301

import time
import datetime
import discord
from methods import send_reply

async def execute(client, message, config):
    """ Executes the command !pissandshit """
    await client.send_typing(message.channel)
    await client.send_message(message.channel, '🐸')
