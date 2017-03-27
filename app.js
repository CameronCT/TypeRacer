console.log("Starting Discord Bot!");

/* Depends */
var     request             = require('request');
var     Config              = require(__dirname + '/libs/config.js');
var     Entities            = require('html-entities').XmlEntities;
const   Discord             = require('discord.js');
const   client              = new Discord.Client({autoReconnect:true});

/* Bot */
client.on('ready', () => {
    console.log('Bot has successfully started');

    /* All strings below are community entered */
    var Games = [
        "piss and shit",
        "shaz's arthiritis simulator",
        "300ms start simulator",
        "nonquits",
        "with fuccbois"
    ];
    setInterval(function() {
        var random = Math.floor(Math.random()*(Games.length-0+1)+0);
        client.user.setGame(Games[random]);
    }, 5 * 1000);
});

client.on('message', message => {

    // General
    require(__dirname + '/commands/help.js')(Config,message);
    require(__dirname + '/commands/stats.js')(Discord,request,Config,message);
    require(__dirname + '/commands/wpm.js')(Config,message);
    require(__dirname + '/commands/import.js')(Config,message,request);

    // PUG
    //require(__dirname + '/commands/pug.js')(Config,message);

});
client.login(Config.Discord);

/* Log */
console.log("Discord bot has started!");

/* https://discordapp.com/api/oauth2/authorize?client_id=278647619780083712&scope=bot&permissions=0 */