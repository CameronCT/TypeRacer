const Func        = require('../libs/functions.js');
const WPM         = require('../libs/wpm.js');

module.exports = function(Config,message) {
    if (Func.isCommand(message, '!wpm')) {
        let params = Func.getParams(message);
        params.splice(0, 1);
        let query = params.join(" ");

        message.channel.sendMessage(WPM.process(query));
    }
}