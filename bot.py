import server
import discord
import urllib.request, json 
import time
from datetime import datetime
from pytz import timezone
import random
import json
from replit import db
from threading import Timer

async def botCheck(message, command, args, client, p, defaultColor, fullArgs, cooldowns):
        if command == 'suggest':
                if f"suggest_{message.author.id}" in cooldowns:
                        await message.channel.send('The cooldown for this command is one minute, please try again later.')
                else:
                        if len(args) < 1:
                                await message.channel.send('Please provide your suggestion after the command!')
                        else:
                                e = discord.Embed(color=defaultColor, description=fullArgs)
                                e.set_author(name=f"Suggestion by {message.author}", icon_url=message.author.avatar_url)
                                await message.channel.send(f"Your suggestion has been filed and saved and will be reviewd, it was also sent to the user-suggestions channel of the support server! Your suggestion will be reviewed by a staff member or a developer. \n\n **Your Suggestion:** `{fullArgs}`")
                                await client.get_channel(int('781990123741904907')).send(embed=e)
                                suggestions = db['suggestions']
                                est = timezone('EST')
                                date = datetime.now(est).strftime('%l:%M%p %Z on %b %d, %Y')
                                suggestion = f"""
    <div class="card">
	      <br><p style='margin-top:5px;font-size:20px'><b><u>User: {message.author}</u></b></p><p> 
    <p><b>Suggestion Content:  </b>{fullArgs}</p>
    <p><b>Suggested On:  </b>{date}</p>
    <p><b>User ID:  </b>{message.author.id}</p>
    <br>
	    </div>  
<br><br>
                                """
                                db['suggestions'] = suggestion + suggestions
                                cooldowns.append(f"suggest_{message.author.id}")
                                def removeCooldown():
                                        cooldowns.remove(f"suggest_{message.author.id}")

                                t = Timer(60.0, removeCooldown)
                                t.start()








        if command == 'issue' or command == 'bug':
                if f"issue_{message.author.id}" in cooldowns:
                        await message.channel.send('The cooldown for this command is one minute, please try again later.')
                else:
                        if len(args) < 1:
                                await message.channel.send('Please provide the issue you found after the command!')
                        else:
                                e = discord.Embed(color=defaultColor, description=fullArgs)
                                e.set_author(name=f"Issue Reported by {message.author}", icon_url=message.author.avatar_url)
                                await message.channel.send(f"Your issue has been filed and saved and will be reviewd, it was also sent to the reported-bugs channel of the support server! Your issue will be reviewed by a staff member or a developer. \n\n **Your Reported Issue/Bug:** `{fullArgs}`")
                                await client.get_channel(int('781990143677431828')).send(embed=e)
                                issues = db['issues']
                                est = timezone('EST')
                                date = datetime.now(est).strftime('%l:%M%p %Z on %b %d, %Y')
                                issue = f"""
    <div class="card">
	      <br><p style='margin-top:5px;font-size:20px'><b><u>User: {message.author}</u></b></p><p> 
    <p><b>Bug Report Content:  </b>{fullArgs}</p>
    <p><b>Reported On:  </b>{date}</p>
    <p><b>User ID:  </b>{message.author.id}</p>
    <br>
	    </div>  
<br><br>
                                """
                                db['issues'] = issue + issues
                                cooldowns.append(f"issue_{message.author.id}")
                                def removeCooldown():
                                        cooldowns.remove(f"issue_{message.author.id}")

                                t = Timer(60.0, removeCooldown)
                                t.start()
