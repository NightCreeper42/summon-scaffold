# Discord Summon Bot

Hello, and thank you for choosing to have a Summon Bot! I am delighted this little thing can be of service.

## Installing Python
First, you are going to need to install [python3](https://www.python.org/downloads/) (the latest will do) and make sure you have 'Add Python x.z.y to PATH' checked at the bottom of the installer when you first open it.

## Creating a Discord Application
Now that you have python installed, you'll need to create a discord Application for it. There are plenty of tutorials online to do this. In fact, [here's one](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)! You only need to go as far as inviting your bot to the server.

## It's alive, *it's aliiive!*
Cool, so you've got your hollow shell of a discord bot invited to your server. Now, let's stuff it with usefulness!

But first, you may need to install some libraries. You'l need to install the libraries `discord`, `gtts` and `playsound`. Do this by going into your command line and typing `pip install <library>`.
At the top of the code, you should see this:
```
#-------------------#
# INITIAL VARIABLES #
#-------------------#
global name,guild_id,channel_id,your_id,other_id,TOKEN
name = "Your Name"
guild_id = 123456789
channel_id = 123456789
your_id = 123456789
other_id = 123456789
TOKEN = "abc"
command_prefix = "Davus " # the space after is important. 
other_bot_name = "Dave"
```

Ignore the global bit and fill up these variables. Here's a list of what the hell they do:

| Variable | Type | Description |
| ----------- | ----------- | ----------- |
| name | string | Here, you put your name (i.e. the 'Dom' in Summon Dom). |
| guild_id | integer | The id of your guild. To get this, [make sure you have Developer Mode enabled](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-). |
| channel_id | integer | Same as guild_id but for your channel. |
| your_id | integer | To get this, right click yourself in the users list. |
| other_id | integer | This is the id of a potential friend who also has a summon bot. |
| TOKEN | string | Get this by going to the Bot tab and pressing "Copy". |
| command_prefix | string | The prefix of your command (i.e. the 'Dommus ' in Dommus summonus). The space is important. |
| other_bot_name | string | Like the `name` variable but for another bot that your friend may have. |


Having filled those in, you now need to add greetings. Near the bottom of the file, there's the function `on_ready()`. In there, you should see a comment that says `# here, put a list of things you want the bot to maybe say when it's first turned on to let others know that it's on. It's recommended you use @here`.  
An example from the Great Summon Dom is, `"@here I'm online if you want to boogie"`. Truely inspiring stuff.  
  
Now, run your code and watch it work! You can even try the summoning command you put in. It truely is wonderful, isn't it?  
The way *I* typically get the bot to run is by doing `Win+R` and having the command `python summon.py` to run it. I have the file in my User folder and the file is named `summon.py`. This was the point of adding python to path before.  
If you have any queries, feel free to ask them in the Issues tab and I'll try to respond asap.  
### Happy summoning!
