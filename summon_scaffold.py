from discord.ext import commands
from discord import Status
import time,discord,random,playsound,gtts,os
from discord.ext.commands.core import Command # *yawn* boring import stuff

intents = discord.Intents.default()
intents.members = True
intents.presences = True

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
command_prefix = "foo " # the space after is important. 
other_bot_name = "Dave"

bot = commands.Bot(command_prefix=command_prefix, help_command=None, intents=intents) # important stuff that needs to be defined or the whole code falls down the kermit

class botCommands(commands.Cog): # ah yes, O R G A N I S A T I O N

    @commands.command()
    async def summon(self,ctx): # the beast of the bot, the summon command. Now defined! You will have to change this in the help command also.
        try:
            commandGuts = ctx.message.content.split(' ') # splitting open the command
            x = commandGuts[2] # this is just a test to catch an index error if there isn't an additional message
            del commandGuts[0]
            del commandGuts[0] # when 0 is deleted, the next one goes to the position 0
            
            additional = ''
            for x in commandGuts:
                additional = additional + x + ' ' # reassembles the additional message
            tts = gtts.gTTS(f"You have been summoned by {str(ctx.author).split('#')[0]}. Additional: {additional}",lang="en")
            print(f"You were summoned by {ctx.author} @ {time.strftime('%H:%M')}; Additional: {additional}")
        except IndexError: # from the test earlier
            tts = gtts.gTTS(f"You have been summoned by {str(ctx.author).split('#')[0]}",lang="en")
            print(f"You were summoned by {ctx.author} @ {time.strftime('%H:%M')}")
        
        await ctx.message.channel.send("Dom has been notified of your summoning. He shall arrive shortly.") # in the other one, I did it for both the additional and not because S P A G H E T

        filename = 'tmp.mp3'
        tts.save(filename)
        playsound.playsound(filename)   # plays the summmnnn
        os.remove(filename)

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(
            title = f"**Summon {name}**",
            colour = discord.Colour.blurple(),
            ) # embeds look SO MUCH BETTER OH MY GOD
        embed.add_field(name="**Command**",value="summon\nhelp\nping\nupdates\nLED",inline=True)
        embed.add_field(name="**Description**",value="Summons Dom\nShows this message\nPings the bot to see if it is responding\nLists all of the updates from v2.2 onwards\nLights up LEDs in an ordered squence",inline=True) # sets the fields for the inline table of commands. Thank god for the inline parameter or my OCD would drive me up the wall
        apr = random.randint(1000,999999999)
        embed.set_footer(text=f"Summon {name} - Part of the Summon Bot collection by Dom Massive\n{apr}% APR, Ts&Cs Apply") # Ts&Cs listed here: https://bit.ly/39mTazI
        await ctx.channel.send(embed=embed) # sends the embed, duh

    @commands.command()
    async def ping(self,ctx):
        await ctx.channel.send("Pong! :ping_pong:") # does what it says on the tin, really
        

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{command_prefix}help"))
    print("Ready to go!") # tells you when it's ready AND does the cool thing with the listening to status thing

    guild = bot.get_guild(guild_id)
    summonDave = guild.get_member_named("lorem_ipsum#0000") # another summon bot in case anyone else's may be on. Dave is not real, btw
    channel = bot.get_channel(channel_id)

    if str(summonDave.status) == "online":
        await channel.send(f"<@!{your_id}> Summon Dave is already on you twonk")
    else:
        await channel.send(random.choice([
            "@here greeting 1", # here, put a list of things you want the bot to maybe say when it's first turned on to let others know that it's on. It's recommended you use @here
            "@here greeting 2"
        ]))

@bot.event
async def on_member_update(before, after):
    if str(after.name) == f"Summon {other_bot_name}" and after.status == Status.online:
        channel = bot.get_channel(channel_id)
        await channel.send(f"<@!{other_id}> I'm already online you twonk")

bot.add_cog(botCommands())
bot.run(TOKEN) # boring discord backend stuff
