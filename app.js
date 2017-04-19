console.log("Starting Discord Bot!");

/* Depends */
const     request             = require('request');
const     Config              = require(__dirname + '/libs/config.js');
const     Entities            = require('html-entities').XmlEntities;
const     Discord             = require('discord.js');
const     client              = new Discord.Client();

/* Bot */
client.on('ready', () => {
    console.log('Bot has successfully started');
    client.user.setGame('TypeRacer')

    /* All strings below are community entered */
    var Games = [
        "piss and shit",
        "shaz's arthiritis simulator",
        "300ms start simulator",
        "nonquit",
        "i dont select races",
        "ctrl+s",
        "rip kenny 2017",
        "TRData Championship",
        "House of Typing"
    ];
    setInterval(function() {
        var random = Math.floor(Math.random()*(Games.length-0+1)+0);
        client.user.setGame(Games[random]);
    }, 2 * 1000);
});

client.on("guildMemberAdd", (member) => {
    if (!member.bot) {
        const guild = member.guild;
        guild.channels.get(guild.id).sendMessage(`Welcome to the Discord, ` + member + `! `);
    }
});

client.on('message',  message => {

    // Debug
    console.log(`(${message.guild.name} / #${message.channel.name}) ${message.author.username}: ${message.content}`);

    // Commands
    require(__dirname + '/commands/help.js')(Discord,Config,message);
    require(__dirname + '/commands/changelog.js')(Discord,Config,message);
    require(__dirname + '/commands/stats.js')(Discord,request,Config,message);
    require(__dirname + '/commands/wpm.js')(Config,message);
    require(__dirname + '/commands/import.js')(Config,message,request);

    // Ping
    if (message.content === '!ping') {
        message.reply('pong i guess');
    }
});

client.on('error', error => { 
    console.log(error);
});

client.login(Config.Discord);

/* Log */
console.log("Discord bot has started!");

/* https://discordapp.com/api/oauth2/authorize?client_id=278647619780083712&scope=bot&permissions=0 */