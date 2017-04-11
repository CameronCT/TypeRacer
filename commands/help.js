var Func        = require('../libs/functions.js');

module.exports = function(Discord,Config,message) {
    if (Func.isCommand(message, '!help') || Func.isCommand(message, '!h')) {
        const helpEmbed = new Discord.RichEmbed()
            .setColor('#00FF00')
            .setDescription(`
                Welcome to **` + Config.name + `** created by **` + Config.author + `**!

                **General**
                !h(elp) - *The command you are currently viewing*
                !s(tats) - *Find statistics of a TypeRacer User*
                !i(mport) - *Import user to TypeRacerData*
                !wpm - *Check details statistics on a given quote*
                !c(hangelog) - *Update logs of the Discord bot*

                **Tournaments**
                TypeRacerData Championship - http://typeracerdata.com/championship
                House of Typing - https://houseoftyping.com
                Typing Zone - http://typingzone.com

                If you want to contribute, you may check out the repository on GitHub at https://github.com/CameronCT/TypeRacer/
                This bot is powered by http://typeracerdata.com/
            `)
        ;

        try { 
            message.channel.sendEmbed(helpEmbed);
        } catch (err) {
            message.reply('There was a problem, please try again!');
        }
    }
}