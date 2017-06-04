"""
    File: methods.py
    Description: Full of modules for easy command processing
    Last Modified: 6/4/2017
"""

def user_string(userid):
    """
        Name: user_string()
        Description: Returns the Discord's username in a @mention form. <@01234567890>
    """

    return '<@' + str(userid) + '>'

def send_reply(client, channel, author, message, right=False):
    """
        Name: send_reply()
        Description: Used to easily send a string with the mention of a user before it.
    """
    if right is False:
        return client.send_message(channel, user_string(author) + ', ' + message)
    else:
        return client.send_message(channel, message + ' - ' + user_string(author))
