var Func        = require('../libs/functions.js');

module.exports = function(Config,message) {
    if (Func.isCommand(message, '!help') || Func.isCommand(message, '!h')) {
        message.channel.sendMessage(`
Welcome to ` + Config.name + ` created by ` + Config.author + `!

**General**
!h(elp) - *The command you are currently viewing*
!s(tats) - *Find statistics of a TypeRacer User*
!i(mport) - *Import user to TypeRacerData*
!wpm - *Check details statistics on a given quote*

**Updates**
*2/25/2017:*
    - Made Bot reconnect itself when no activity in server.
    - Updated !stats command and made it say "Last Best 10"
    - Made !import check the TypeRacer API before adding to TypeRacerData's Queue

If you want to contribute, you may check out the repository on GitHub at https://github.com/CameronCT/TypeRacer/

This bot is powered by http://typeracerdata.com/
        `);
    }
}

/*
**PUG (experimental)**
!a(dd) - *Adds you to PUG Queue*
!r(emove) - *Removes you from PUG Queue*
!w(ho) - *Returns a list of Added racers*
*/