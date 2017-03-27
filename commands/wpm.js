var Func        = require('../libs/functions.js');
var WPM         = require('../libs/wpm.js');

module.exports = function(Config,message) {
    if (Func.isCommand(message, '!wpm')) {
        var params = Func.getParams(message);
        params.splice(0, 1);
        var query = params.join(" ");

        message.channel.sendMessage(WPM.process(query));
    }
}