var Func        = require('../libs/functions.js');

var options = {
    weekday: "long", year: "numeric", month: "short",
    day: "numeric", hour: "2-digit", minute: "2-digit"
};

module.exports = function(request,Config,message) {
    if (Func.isCommand(message, '!stats') || Func.isCommand(message, '!s')) {
        var params = Func.getParams(message);
        if (!params[1]) return message.reply("**SYNTAX:** !stats <username>");

        request.get('http://typeracerdata.com/api?username=' + params[1], function(error, response, body) {    
            if (error || !body|| response.statusCode != 200) return message.reply("The username you have entered could not be found, please try again!");
            data = JSON.parse(body);
            
            var last = new Date(data.account.last_import * 1000);
            var marathon = new Date(data.account.marathon_start * 1000);

            message.channel.sendMessage(`
**` + String(data.account.username) + `** - Last Import: ` +  last.toLocaleTimeString("en-us", options) + `

**General Statistics** 
    Races: *` + data.account.races + ` (` + data.account.wins + ` won)*
    Texts: *` + data.account.texts_raced + `*
    Marathon: *` + data.account.marathon_total + ` on ` + marathon.toLocaleTimeString("en-us", options) + `*

**WPM Statistics** 
    Highest: *` + parseFloat(data.account.wpm_highest).toFixed(2) + `*
    Text Bests: *` + parseFloat(data.account.wpm_textbests).toFixed(2) + `*
    Last Best 10: *` + parseFloat(data.account.wpm_last10).toFixed(2) + ` (` + parseFloat(data.account.wpm_bestlast10).toFixed(2) + ` last best)*

This data was pulled from TypeRacerData's API created by Noah.

            `);
        });
    }
}