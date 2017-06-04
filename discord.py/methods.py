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
