const Func        = require('../libs/functions.js');

module.exports = function(Discord,Config,message) {
    if (Func.isCommand(message, '!changelog') || Func.isCommand(message, '!c')) {
        if (!Func.getParams(message)) return message.reply("**SYNTAX:** !changelog");

        const changeLogEmbed = new Discord.RichEmbed()
            .setColor('#FF0000')
            .setDescription(`
                **CHANGELOG FOR 3/26/2017**
                - Added command !c(hangelog)
                - Changed style of !s(tats)
                - Corrected bug on !wpm
                - Corrected bug on !s(tats) with Last Best 10
                - Removed PUG system
                - Changed style of !h(elp)

                **CHANGELOG FOR 2/24/2017**
                - Made Bot reconnect itself when no activity in server.
                - Updated !stats command and made it say "Last Best 10"
                - Made !import check the TypeRacer API before adding to TypeRacerData's Queue
            `)
        ;

        try { 
            message.channel.sendEmbed(changeLogEmbed);
        } catch (err) {
            message.channel.reply('There was a problem, please try again!');
        }
    }
}