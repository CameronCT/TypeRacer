var Func        = require('../libs/functions.js');
var Max         = 4;
var Comma       = "";
var Foreach     = "";

/* Bad way of doing this, but idc */
var types               = ["main","short","championship"];
var main                = [];
var short               = [];
var championship        = [];

var getList = function(type,array) {
    for (var i = 0; i < array.length; i++) {
        if (type == "User")
            Foreach += Comma + array[i].User;
        else
            Foreach += Comma + "<@" + array[i].Discord + ">";
        Comma = ", ";
    }
    return Foreach;
}

var getUniverse = function(array) {
    for (var i = 0; i < array.length; i++) {
        Foreach += Comma + array[i];
        Comma = ", ";
    }
    return Foreach;
}

module.exports = function(Config,message) {

    if (Func.isCommand(message, '!add') || Func.isCommand(message, '!a')) {
        var params = Func.getParams(message);
        if (!params[1]) return message.reply("**SYNTAX:** !add <main|short|championship>");
        if (!types.includes(params[1])) return message.reply("The universe you have entered doesn't exist!");

        var Data = { Discord: message.author.id, User: message.author.username };

        switch(params[1]) {
            case "main":
                main.push(Data);
                if (main.length < Max) return message.channel.sendMessage("You have successfully been added to the queue for \"main\"!  **(" + main.length + "/" + Max + ")**");
                if (main.length >= Max) { 
                    message.channel.sendMessage("A new pickup game has started! All players report to " + main[0].User + "'s lobby! \n(" + getList("Discord", main) + ")"); 
                    main = [];
                }
                break;
            case "short":
                short.push(Data);
                if (short.length < Max) return message.channel.sendMessage("You have successfully been added to the queue for \"short\"!  **(" + short.length + "/" + Max + ")**");
                if (short.length >= Max) { 
                    message.channel.sendMessage("A new pickup game has started! All players report to " + short[0].User + "'s lobby! \n(" + getList("Discord", short) + ")"); 
                    short = [];
                }
                break;
            case "championship":
                championship.push(Data);
                if (championship.length < Max) return message.channel.sendMessage("You have successfully been added to the queue for \"championship\"!  **(" + championship.length + "/" + Max + ")**");
                if (championship.length >= Max) { 
                    message.channel.sendMessage("A new pickup game has started! All players report to " + championship[0].User + "'s lobby! \n(" + getList("Discord", championship) + ")"); 
                    championship = [];
                }
                break;
        }
    }

    if (Func.isCommand(message, '!who') || Func.isCommand(message, '!w')) {
        var params = Func.getParams(message);
        
        return message.channel.sendMessage(`
**Main:** (` + main.length + `/` + Max + `)
**Short:** (` + short.length + `/` + Max + `)
**Championship:** (` + championship.length + `/` + Max + `) 
        `);
    }
}