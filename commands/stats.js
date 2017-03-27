var Func        = require('../libs/functions.js');

var options = {
    weekday: "long", year: "numeric", month: "short",
    day: "numeric", hour: "2-digit", minute: "2-digit"
};

module.exports = function(Discord,request,Config,message) {
    if (Func.isCommand(message, '!stats') || Func.isCommand(message, '!s')) {
        var params = Func.getParams(message);
        if (!params[1]) return message.reply("**SYNTAX:** !stats <username>");

        request.get('http://typeracerdata.com/api?username=' + params[1], function(error, response, body) {    
            if (error || !body|| response.statusCode != 200) return message.reply("The username you have entered could not be found, please try again!");
            data = JSON.parse(body);
            
            var last = new Date(data.account.last_import * 1000);
            var marathon = new Date(data.account.marathon_start * 1000);

            var blank = ' ';

            const startEmbed = new Discord.RichEmbed()
                .setColor('#00B2EE')
                .setThumbnail(`http://data.typeracer.com/misc/pic?uid=tr:` + data.account.username + `&size=large&bpc=1`)
                .setAuthor(`Statistics for ` + data.account.username)
                .setDescription(`
                    The data supplied by this bot is from TypeRacerData's API which was created by Noah. Make sure to check out the TypeRacer Championship at http://typeracerdata.com/championship/
                `)
                .addField('\u200b', '__**General Statistics**__', true)
                .addField('Races:', data.account.races + ` (` + data.account.wins + ` won)`)
                .addField('Texts:', data.account.texts_raced)
                .addField('Marathon:', data.account.marathon_total + ` on ` + marathon.toLocaleTimeString("en-us", options))
                .addField('\u200b', '__**WPM Statistics**__', true)
                .addField('Career Avg:', parseFloat(data.account.wpm_life).toFixed(2) + ` WPM`)
                .addField('Highest:', parseFloat(data.account.wpm_highest).toFixed(2) + ` WPM`)
                .addField('Text Bests:', parseFloat(data.account.wpm_textbests).toFixed(2) + ` WPM`)
                .addField('Last Best 10:', parseFloat(data.account.wpm_bestlast10).toFixed(2) + ` WPM ` + `(` + parseFloat(data.account.wpm_bestlast10).toFixed(2) + ` peak)`)
                .setFooter(`Last Imported: ` + last.toLocaleTimeString("en-us", options))
            ;

            try { 
                message.channel.sendEmbed(startEmbed);
            } catch (err) {
                message.channel.reply('There was a problem, please try again!');
            }
        });
    }
}