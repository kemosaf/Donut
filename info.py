from replit import db
import server
import discord
import urllib.request, json 
import random
import json
import time
import requests
import wikipedia
from datetime import datetime
from pytz import timezone
async def infoCheck(message, command, args, client, p, defaultColor, fullArgs):

    if command == 'invite':
            embed=discord.Embed(color=defaultColor, description=f"You can get my direct invite at [donut.js.org/invite](https://donut.js.org/invite), and you can see my website at [donut.js.org](https://donut.js.org).")
            await message.channel.send(embed=embed)
    #help command
    if command == 'help' or command == 'commands':
                        embed=discord.Embed(color=defaultColor, description=f"This list of commands is also avaliable online at [Donut.js.org/commands](https://donut.js.org/commands)")
                        embed.set_author(name='Donut - Help', icon_url='https://media.discordapp.net/attachments/758726391495000104/779145290347184148/97d72f9647dbe3ed61c585d7ce9947bf.png')
                        embed.add_field(name='__😂 - Fun__' , value=f'`{p}meme`, `{p}cleanmeme`, `{p}8ball`, `{p}cat`, `{p}dog`, `{p}reddit`, `{p}joke`, `{p}snipe`', inline=False)
                        embed.add_field(name='__📸 - Image Manipulation__' , value=f'`{p}tweet`, `{p}trumptweet`, `{p}captcha`, `{p}threats`, `{p}clyde`, `{p}deepfry`, `{p}wide`, `{p}slap`, `{p}changemymind`, `{p}simp`, `{p}invert`, `{p}colorify`, `{p}trash`, `{p}shoot`', inline=False)
                        embed.add_field(name='__📃 - Info__' , value=f'`{p}help`, `{p}latency/{p}ping`, `{p}avatar/{p}av/{p}pfp`, `{p}icon`, `{p}userinfo`, `{p}serverinfo`, `{p}corona`, `{p}fact`, `{p}level`, `{p}wikipedia/{p}wiki`, `{p}invite`', inline=False)
                        embed.add_field(name='__🚔 - Moderation/Utility__', value=f'`{p}clear`, `{p}kick`, `{p}ban`, `{p}mute`, `{p}unmute`, `{p}warn`, `{p}warns`, `{p}clear-warns`, `{p}poll\{p}vote`')
                        embed.add_field(name='__⚙ - Customization/Logging__' , value=f'`{p}prefix`, `{p}greetings`, `{p}leaves`, `{p}messages`', inline=False)  
                        embed.add_field(name='__💰 - Economy__', value=f'`{p}work`, `{p}daily`, `{p}start`, `{p}balance/{p}bal`, `{p}leaderboard/{p}lb`, `{p}setbalance`, `{p}deposit/{p}dep`, `{p}withdraw/{p}with`, `{p}rob`, `{p}currency`')
                        embed.add_field(name='__🤖 - Bot__', value=f"`{p}suggest`, `{p}issue`,  `{p}uptime`, `{p}about` ", inline=False)                     
                        await message.channel.send(embed=embed)

    if command == 'translate':
        lang = args[0]
        msgArgs = args
        del msgArgs[:1]
        msg = " ".join(msgArgs)
        translator = GoogleTrans()
        translated = translator.translate(fullArgs)
        await message.channel.send(translated)

    if command == 'wikipedia' or command == 'wiki':
        if len(fullArgs) < 1:  await message.channel.send("Please provide a term to search wikipedia for.")
        summary = wikipedia.summary(fullArgs, sentences=5)
        e = discord.Embed(color=defaultColor, title=f'A Wikipedia Summary on `{fullArgs}`', description=summary)
        await message.channel.send(embed=e)
    if command == 'uptime':
        def getUptime(bot):
            est = timezone('EST')
            now = datetime.now(est)
            delta = now - bot.uptime
            hours, remainder = divmod(int(delta.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)
            if days:
                fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
            else:
                fmt = '{h} hours, {m} minutes, and {s} seconds'
            return fmt.format(d=days, h=hours, m=minutes, s=seconds)
        e = discord.Embed(color=defaultColor)
        e.add_field(name='Uptime', value=f'{getUptime(client)}', inline=False)
        e.add_field(name='Online Since', value=client.uptime.strftime('%l:%M%p %Z on %b %d, %Y'), inline=False)
        e.add_field(name='More Uptime Info', value='[Click Here](https://stats.uptimerobot.com/1Vklgip78O)')
        e.set_author(name='Donut - Uptime', icon_url='https://media.discordapp.net/attachments/758726391495000104/779145290347184148/97d72f9647dbe3ed61c585d7ce9947bf.png')

        await message.channel.send(embed=e)
    if command == 'about':
        e = discord.Embed(color=defaultColor)
        e.set_author(name='Donut - About', icon_url='https://media.discordapp.net/attachments/758726391495000104/779145290347184148/97d72f9647dbe3ed61c585d7ce9947bf.png')
        e.add_field(name='Written With', value='Python 🐍\n and \nJavaScript ☕', inline=False)
        e.add_field(name='Developed By', value='kemosaf#7268', inline=False)
        e.add_field(name='Developed On', value='Sunday 19, July 2020', inline=False)
        e.add_field(name='Servers', value=len(client.guilds), inline=False)
        e.add_field(name='Linked Users', value=len(client.users), inline=False)
        e.add_field(name='Support Server', value='[discord.gg/spX282SDPQ](https://discord.gg/spX282SDPQ)')
        await message.channel.send(embed=e)

    if command == 'level':
        if len(message.mentions) < 1:
                member  = message.author
        else:
                member = message.mentions[0]
                
        try:
            xp = db[f"level_{member.id}"]
        except:
            xp = 0

        try:
            xpcolor = db[f'cardXp_{member.id}']
        except:
            xpcolor = 'ff4085'

        try:
            bgcolor = db[f'cardBg_{member.id}']
        except:
            bgcolor = None
        nextInt = int(xp/1000+1) * 1000
        leftNext = nextInt - xp 
        thisLevelXp  = 1000 - leftNext
        print(f"https://vacefron.nl/api/rankcard?username={str(member).replace('#', '%23').replace('✞', '').replace(' ', '+')}&avatar={member.avatar_url}&level={int(xp/1000)}&rank=&currentxp={thisLevelXp}&nextlevelxp=1000&previouslevelxp=0&custombg={bgcolor}&xpcolor={xpcolor}&isboosting=false")
        e = discord.Embed(title=f'{member.name}\'s Level', color=defaultColor, description=f'This level is based of how much {member.name} uses the bot. To view a leaderboard of all levels go to [Donut.js.org/levels](https://donut.js.org/levels). You can customize your own level card at [Donut.js.org/dashboard](https://donut.js.org/dashboard).')
        e.add_field(name='Level:', value=int(xp/1000))
        e.add_field(name='Total XP:', value=xp)
        e.add_field(name='XP This Level:', value=f'{thisLevelXp}/1000')
        e.set_image(url=f"https://vacefron.nl/api/rankcard?username={str(member).replace('#', '%23').replace('✞', '').replace(' ', '+')}&avatar={member.avatar_url}&level={int(xp/1000)}&rank=&currentxp={thisLevelXp}&nextlevelxp=1000&previouslevelxp=0&custombg={bgcolor}&xpcolor={xpcolor}&isboosting=false")
        await message.channel.send(embed=e)
    #fact command
    #API: https://uselessfacts.jsph.pl/random.json?language=en
    if command == 'fact':
                        with urllib.request.urlopen("https://uselessfacts.jsph.pl/random.json?language=en") as url:
                                data = json.loads(url.read().decode())
                                fact = data['text']
                                e = discord.Embed(title='A Cool Fact!', color=defaultColor, description=fact)
                                await message.channel.send(embed=e)

    
    #avatar command
    elif command == 'avatar' or command == 'pfp' or command == 'av':
        if len(message.mentions) < 1:
                member  = message.author
        else:
                member = message.mentions[0]
                
                
                
        av = discord.Embed(title=f'{member.name}\'s Avatar', footer=f'Requested by {message.author.name}', colour=defaultColor)
        av.set_image(url='{}'.format(member.avatar_url))                        
        await message.channel.send(embed=av)

	#icon command
    elif command == 'icon':
        e = discord.Embed(title=f"{message.guild.name}'s Icon", color=defaultColor)
        e.set_image(url=message.guild.icon_url)
        await message.channel.send(embed=e)

    #userinfo command
    elif command == 'userinfo':
        if ( len(fullArgs) < 1 ):
                member  = message.author  
        else:
                member = message.mentions[0]


        if member.bot:
                accType = 'Bot'
        else:
                accType = 'Human'
        userEmbed = discord.Embed(title=f'About {member}', footer=f'Requested by {message.author}', color=defaultColor)
        userEmbed.set_thumbnail(url=member.avatar_url)

        userEmbed.add_field(name='User\'s ID', value=member.id, inline=False)
        userEmbed.add_field(name='User\'s Nickname', value=member.display_name, inline=False)
        userEmbed.add_field(name='Discord Birthday', value=member.created_at.strftime('%a, %#d, %B, %Y, %I :%M %p UTC'),inline=False)
        userEmbed.add_field(name='Joined Guild Date', value=member.joined_at.strftime("%a, %d %B %Y, %I : %M %p UTC"), inline=False)
        userEmbed.add_field(name='Account Type', value=accType, inline=False)
        userEmbed.add_field(name='Top Role', value=member.top_role.mention, inline=False)
        userEmbed.set_footer()
        await message.channel.send(embed=userEmbed)

    elif command == 'serverinfo':
        serverEmbed = discord.Embed(title=f'Server Info - {message.guild.name}', footer=f'Requested by {message.author}', color=defaultColor)
        serverEmbed.set_thumbnail(url=message.guild.icon_url)
        serverEmbed.set_thumbnail(url=f"{message.guild.icon_url}")
        serverEmbed.add_field(name='Server ID', value=message.guild.id, inline=False)
        serverEmbed.add_field(name='Owner', value=message.guild.owner, inline=False)
        serverEmbed.add_field(name='Created At', value=message.guild.created_at.strftime("%d/%m/%Y"),inline=False)
        serverEmbed.add_field(name='Bots', value=len(list(filter(lambda m: m.bot, message.guild.members))), inline=False)
        serverEmbed.add_field(name='Humans', value=len(list(filter(lambda m: not m.bot, message.guild.members))), inline=False)
        serverEmbed.add_field(name='Total Members', value=len(message.guild.members), inline=False)
        serverEmbed.add_field(name='Text Channels', value=len(message.guild.text_channels), inline=False)
        serverEmbed.add_field(name='Voice Channels', value=len(message.guild.voice_channels), inline=False)
        serverEmbed.set_footer()
        await message.channel.send(embed=serverEmbed)
    elif command == 'ping' or command == 'latency':
            before = time.monotonic()
            message = await message.channel.send("Pinging...")
            ping = (time.monotonic() - before) * 1000
            e = discord.Embed(title=f'Pong! 🏓', color=defaultColor)
            e.add_field(name='Bot Latency', value=f'`{ping}ms`', inline=False)
            e.add_field(name='Socket Latency', value=f'`{client.latency*1000 }ms`', inline=False)
            await message.edit(embed=e)


    elif command == 'corona' or command =='covid' or command =='coronavirus' or command == 'coronacount':
            if len(fullArgs) < 1:
                response = requests.get("https://disease.sh/v2/all")
                response.raise_for_status()
                data = response.json()
                e = discord.Embed(title=f'Global Coronavirus Statistics', description='These statistics are provided from the internet and may not be the most accurate, try putting a country after the command to get the statistics for that country!', color=defaultColor)
                e.add_field(name='Total Cases', value=f'{data["cases"]}')
                e.add_field(name='Total Deaths', value=f'{data["deaths"]}')
                e.add_field(name="Today's Cases", value=f'{data["todayCases"]}')
                e.add_field(name="Today's Deaths", value=f'{data["todayDeaths"]}')
                e.add_field(name="Recovered", value=f'{data["recovered"]}')
                e.add_field(name="Recovered Today", value=data["todayRecovered"])
                e.add_field(name='Critical', value=data['critical'])
                e.add_field(name='Affected Countries', value=data["affectedCountries"])
                e.add_field(name='Tests', value=data["tests"])
                e.add_field(name="Cases Per 1 Million", value=data["casesPerOneMillion"])
                e.add_field(name="Deaths Per 1 Million", value=data["deathsPerOneMillion"])
                e.add_field(name='Recovered Per 1 Million', value=data["recoveredPerOneMillion"])
                await message.channel.send(embed=e)
            else:
                response = requests.get(f"https://disease.sh/v2/countries/{fullArgs}")
                response.raise_for_status()
                data = response.json()
                e = discord.Embed(title=f'{data["country"]}\'s Coronavirus Statistics', description='These statistics are provided from the internet and may not be the most accurate, a number "0" means that the info wasn\'t found.', color=defaultColor)
                e.set_thumbnail(url=data["countryInfo"]["flag"])
                e.add_field(name='Total Cases', value=f'{data["cases"]}')
                e.add_field(name='Total Deaths', value=f'{data["deaths"]}')
                e.add_field(name="Today's Cases", value=f'{data["todayCases"]}')
                e.add_field(name="Today's Deaths", value=f'{data["todayDeaths"]}')
                e.add_field(name="Recovered", value=f'{data["recovered"]}')
                e.add_field(name="Recovered Today", value=data["todayRecovered"])
                e.add_field(name='Critical', value=data['critical'])
                e.add_field(name='One Case Per People', value=data["oneCasePerPeople"])
                e.add_field(name='Tests', value=data["tests"])
                e.add_field(name="Cases Per 1 Million", value=data["casesPerOneMillion"])
                e.add_field(name="Deaths Per 1 Million", value=data["deathsPerOneMillion"])
                e.add_field(name='Recovered Per 1 Million', value=data["recoveredPerOneMillion"])
                await message.channel.send(embed=e)
