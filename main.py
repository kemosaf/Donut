import os

token = os.getenv("TOKEN")
from datetime import datetime
from pytz import timezone
from threading import Thread

#os.system("npm i discord.js")
#os.system("node index.js")
#READ LICENSE.md
from discord.ext import commands
from replit import db
import server
import economy
from termcolor import colored
import time
import utility
import custom
import fun
import info
import bot
import image
import discord
import os


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '?', intents = intents)
prefix = '?'
#while True:
    #print('f')
keys = db.keys()

cooldowns = ['start']
ecoCooldowns = {}
snipes = {}
#db['blacklists'] = []
@client.event
async def on_ready():
    import pathlib 
    est = timezone('EST')
    client.uptime = datetime.now(est)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name=f"?Help | Donut.js.org"))
    #await client.granitepy.create_node(
 #       host="node-ip",
  #      port=12345,
  #      password="node-password",
     #   identifier="node-name"
   # )

    def connect():
        def lavarun():
            os.system("java -jar Lavalink.jar")
		
        print("Starting processes!")
        time.sleep(5)
        print("Running Lavalink.")
        Thread(target = lavarun).start()
        time.sleep(30) 
    #connect()
    print('Logged In!')
    time.sleep(5)
    #client.load_extension('music')  

@client.event
async def on_guild_join(guild):
        channel = client.get_channel(789355680258719784)
        e = discord.Embed(color=0x00FF00, title="__New Server__")
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name='Name', value=guild.name)
        e.add_field(name='Members', value=len(guild.members))
        e.add_field(name='Now in', value=f"{len(client.guilds)} Servers")
        await channel.send(embed=e)

@client.event
async def on_guild_remove(guild):
        channel = client.get_channel(789355680258719784)
        e = discord.Embed(color=0xff0000, title="__Removed Server__")
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name='Name', value=guild.name)
        e.add_field(name='Members', value=len(guild.members))
        e.add_field(name='Now in', value=f"{len(client.guilds)} Servers")
        await channel.send(embed=e)
@client.event
async def on_message_delete(message):
	if message.author.bot:return
	try:
                defaultColor = int(db[f"color_{message.guild.id}"], 0)
	except:
                defaultColor = 0xff4085
	est = timezone('EST')
	date = datetime.now(est).strftime('%l:%M%p %Z on %b %d, %Y')
	channel = str(message.channel.id)
	if message.attachments:
		image = message.attachments[0].url
	else:
		image = None
	snipes[channel] = {
		"message": f"{message.content}",
		"author": f"{message.author}",
		"avatar": f"{message.author.avatar_url}",
		"image": image,
		"date": f"{date}",
        "type": "Deleted"
	}
	try:
		id = db[f"deleteChannel_{message.guild.id}"]
	except:
		id = None
	
	if id != None:
		print(id)
		channel = client.get_channel(int(id))
		print(channel)
		embed=discord.Embed(description=message.content, footer=f'Message Deleted', color=defaultColor)
		embed.set_author(name=message.author, icon_url=message.author.avatar_url)
		embed.add_field(name='** **', value=f"Sent in <#{message.channel.id}>")
		embed.set_footer(text=f"Deleted on {date}")

		await channel.send(embed=embed)



@client.event
async def on_message_edit(old, new):
        if old.author.bot or new.author.bot:return
        if old.content == new.content:return

        try:
                defaultColor = int(db[f"color_{new.guild.id}"], 0)
        except:
                defaultColor = 0xff4085

        est = timezone('EST')
        date = datetime.now(est).strftime('%l:%M%p %Z on %b %d, %Y')
        channel = str(old.channel.id)
        snipes[channel] = {
		"old": f"{old.content}",
        "new": f"{new.content}",
		"author": f"{new.author}",
		"avatar": f"{new.author.avatar_url}",
		"date": f"{date}",
        "type": "Edited"
	        }
        try:
                id = db[f"editChannel_{new.guild.id}"]
        except:
                id = None
	
        if id != None:
	        channel = client.get_channel(int(id))
	        e=discord.Embed(color=defaultColor)
	        e.set_author(name=new.author, icon_url=new.author.avatar_url)
	        e.add_field(name='Old Message', value=old.content, inline=True)
	        e.add_field(name='New Message', value=new.content, inline=True)
	        e.add_field(name='** **', value=f"Sent in <#{old.channel.id}>", inline=False)
	        e.set_footer(text=f"Edited on {date}")
	        await channel.send(embed=e)


@client.event
async def on_member_join(member):

    try:
        id, message = db[f"joinChannel_{member.guild.id}"], db[
            f"joinMessage_{member.guild.id}"]
    except:
        id, message = None, None

    if id != None and message != None:
        channel = client.get_channel(int(id))
        await channel.send(message.replace('{user}', f"<@!{str(member.id)}>"))


@client.event
async def on_member_remove(member):

    try:
        id, message = db[f"leaveChannel_{member.guild.id}"], db[
            f"leaveMessage_{member.guild.id}"]
    except:
        id, message = None, None

    if id != None and message != None:
        channel = client.get_channel(int(id))
        await channel.send(message.replace('{user}', str(member)))

import linecache
import sys

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))


@client.event
async def on_message(message):
    if message.author.bot:return
    
    try:
        defaultColor = int(db[f"color_{message.guild.id}"], 0)
    except:
        defaultColor = 0xff4085
    try:
        value = db[f"prefix_{message.guild.id}"]
        p = value
    except:
        p = prefix

    if (message.content.startswith(f'<@!734526487994171392> ')):
        message.content = message.content.replace('<@!734526487994171392> ', p,
                                                  1)
    elif (message.content.startswith(f'<@734526487994171392> ')):
        message.content = message.content.replace('<@734526487994171392> ', p,
                                                  1)

    if (message.content.startswith(p)):



        fullMessage = message.content.lower()
        splitMessage = fullMessage.split(' ')
        args = splitMessage[1:]
        space = ' '
        fullArgs = space.join(args)
        firstArg = splitMessage[0]
        command = firstArg[len(p):]

        cmds = ['invite', 'rob', 'daily', 'wikipedia', 'wiki', 'mute', 'unmute', 'warn', 'warns', 'clear-warns', 'uptime', 'vote', 'poll', 'about', 'shoot', 'colorify', 'trash', 'icon', 'simp', 'invert', 'meme', 'slap', 'cleanmeme', '8ball', 'cat', 'dog', 'reddit', 'joke', 'snipe', 'tweet', 'trumptweet', 'captcha', 'threats', 'clyde', 'deepfry', 'wide', 'changemymind', 'help', 'latency', 'ping', 'avatar', 'av', 'pfp', 'userinfo', 'serverinfo', 'corona', 'covid', 'coronacount', 'fact', 'clear', 'kick', 'ban', 'prefix', 'greetings', 'greeting', 'leaves', 'leave', 'messages', 'work', 'start', 'bal', 'balance', 'leaderboard', 'lb', 'setbalance', 'dep', 'deposit', 'withdraw', 'with', 'currency', 'level']
        if command in cmds:
            blacklists = db['blacklists']
            e = discord.Embed(color=0xff0000, title='You are Blacklisted!', description='You have been blacklisted by a staff member and can no longer use the bot. If you think this was a mistake or you have any concerns join the support server and let us know at [discord.gg/spX282SDPQ](https://discord.gg/spX282SDPQ).')
            if str(message.author.id) in blacklists: return await message.channel.send(embed=e)
            try:
                xp = db[f"level_{message.author.id}"]
            except:
                xp = 0
            xp += 20
            db[f"level_{message.author.id}"] = xp

        try:
            level = db[f"level_{message.author.id}"]
        except:
            level = 0
        try:
                await fun.funCheck(message, command, args, client, p, defaultColor,
                           fullArgs, snipes)
                await image.imageCheck(message, command, args, client, p, defaultColor,
                           fullArgs)
                await info.infoCheck(message, command, args, client, p, defaultColor,
                             fullArgs)
                await utility.utilityCheck(message, command, args, client, p,
                                 defaultColor, fullArgs)
              
                await custom.customCheck(message, command, args, client, p,
                                 defaultColor, fullArgs)
                await economy.ecoCheck(message, command, args, client, p, defaultColor,
                               fullArgs, ecoCooldowns)
                await bot.botCheck(message, command, args, client, p, defaultColor,
                               fullArgs, cooldowns)
                
        except Exception as e:
                embed = discord.Embed(title=f'An Unkown Error Has Occured!', description=f'```{PrintException()}```', color=0xff002b)
                await message.channel.send(embed=embed)
                est = timezone('EST')
                date = datetime.now(est).strftime('%l:%M%p %Z on %b %d, %Y')
                print(colored(f"""\nError! Info: User:{message.author}, Command:{command}, Time:{date} \n CODE ERROR: \n {e}
                \n""", 'red'))

server.online(client)
server.setClient(client)
client.run(os.getenv("TOKEN"))