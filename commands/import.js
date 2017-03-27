var Func        = require('../libs/functions.js');

module.exports = function(Config,message,request) {
    if (Func.isCommand(message, '!import') || Func.isCommand(message, '!i')) {
        var params = Func.getParams(message);
        if (!params[1]) return message.reply("**SYNTAX:** !import <username>");
        request.get('http://typeracerdata.appspot.com/users?id=tr:' + params[1], function(error, response, body) {    
            if (error || !body || response.statusCode != 200) return message.reply("The username you have entered could not be found, please try again!");
            request
                .get('http://www.typeracerdata.com/import?username=' + params[1])
                .on('response', function(response) {
                    if (response.statusCode == 200) message.reply("You have successfully added **" + params[1] + "** to the queue!");
                });
        });
    }
}