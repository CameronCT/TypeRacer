module.exports = {

    isCommand: function(message, string) {
        if (message.content.indexOf(string) == 0)
            return true;
        else
            return false;
    },
    isMessage: function(message, string) {
        if (message.content === string)
            return true;
        else
            return false;
    },
    getParams: function(message) {
        return message.content.split(" ");
    }
    
}