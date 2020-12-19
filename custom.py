import server
import discord
import urllib.request, json 
import random
import json
from replit import db

async def customCheck(message, command, args, client, p, defaultColor, fullArgs):



        if command == 'prefix':
                if message.author.guild_permissions.administrator == False: 
                        await message.channel.send('You do not have admin so you cannot change the prefix for this server!')
                else:
                        if ( len(fullArgs) < 1 ):
                                await message.channel.send(f'Please provide the prefix you would like after the command! Current Prefix: `{p}`')
                        else:
                                if(len(args) == 1):
                                        db[f"prefix_{message.guild.id}"] = f"{fullArgs}"
                                        await message.channel.send(f'Successfully set the prefix to `{fullArgs}`')
                                else:
                                        await message.channel.send('Your prefix cannot contain spaces!')

			
        if command == 'greetings' or command == 'greeting':
                if message.author.guild_permissions.administrator == False: 
                        await message.channel.send('You do not have admin so you cannot change the greeting settings for this server!')
                else:
                        try:
                                joinID = db[f"joinChannel_{message.guild.id}"]
                                joinChannel = client.get_channel(int(joinID));
                                check = 'checked'
                        except:
                                joinChannel = 'None'
                                joinID = 'None'
                                check = ''
                        try:
                                joinMessage = db[f"joinMessage_{message.guild.id}"]
                        except:
                                joinMessage = 'None'
	
                        if len(args) < 1:
                                embed=discord.Embed(title='User Greeting System', description=f'Use this command in one of its 2 forms, {p}greetings channel #channel and {p}greetings message message. You can also easily edit these settings and many more through the dashboard at [Donut.js.org/dashboard](https://donut.js.org/dashboard).', color=defaultColor)
                                embed.add_field(name=f'{p}greetings channel #channel', value=f'This configures which channel the bot should send a message to everytime a user joins.', inline=False)
                                embed.add_field(name=f'{p}greetings message message', value='This configures what message the bot should send when a new user joins, make sure to replace the user\'s name with {user}.', inline=False)
                                embed.add_field(name='Current Channel:', value=f'{joinChannel}', inline=True)
                                embed.add_field(name='Current Message:', value=f'{joinMessage}', inline=True)
                                await message.channel.send(embed=embed)                                        
                        else: 
                                if args[0] == 'channel':
                                        if len(message.channel_mentions) < 1:
                                                await message.channel.send('Please mention a channel to set as your user greeting channel!')
                                        else:
                                                db[f"joinChannel_{message.guild.id}"] = str(message.channel_mentions[0].id)
                                                await message.channel.send(f'Successfully set the user greeting channel to {message.channel_mentions[0]}')
                                elif args[0] == 'message':
                                        if len(args) > 1:
                                                space = ' '
                                                msgArgs = args
                                                del msgArgs[:1]
                                                db[f"joinMessage_{message.guild.id}"] = space.join(msgArgs)
                                                await message.channel.send(f'Successfully set the user greeting channel to `{space.join(msgArgs)}`')
                                        else:
                                                await message.channel.send('Please place a greeting message after the command!')
                                else:
                                        embed=discord.Embed(title='User Greeting System', description=f'Use this command in one of its 2 forms, {p}greetings channel #channel and {p}greetings message message. You can also easily edit these settings and many more through the dashboard at [Donut.js.org/dashboard](https://donut.js.org/dashboard).', color=defaultColor)
                                        embed.add_field(name=f'{p}greetings channel #channel', value=f'This configures which channel the bot should send a message to everytime a user joins.', inline=False)
                                        embed.add_field(name=f'{p}greetings message message', value='This configures what message the bot should send when a new user joins, make sure to replace the user\'s name with {user}.', inline=False)
                                        embed.add_field(name='Current Channel:', value=f'{joinChannel}', inline=True)
                                        embed.add_field(name='Current Message:', value=f'{joinMessage}', inline=True)
                                        await message.channel.send(embed=embed)                                        

			
        if command == 'leaves' or command == 'leave':
                if message.author.guild_permissions.administrator == False: 
                        await message.channel.send('You do not have admin so you cannot change the user leaves settings for this server!')
                else:
                        try:
                                leaveID = db[f"leaveChannel_{message.guild.id}"]
                                leaveChannel = client.get_channel(int(leaveID));
                                check = 'checked'
                        except:
                                leaveChannel = 'None'
                                leaveChannel = 'None'
                                check = ''
                        try:
                                leaveMessage = db[f"leaveMessage_{message.guild.id}"]
                        except:
                                leaveMessage = 'None'
	
                        if len(args) < 1:
                                embed=discord.Embed(title='User Leaves Logging System', description=f'Use this command in one of its 2 forms, {p}leaves channel #channel and {p}leaves message message. You can also easily edit these settings and many more through the dashboard at [Donut.js.org/dashboard](https://donut.js.org/dashboard).', color=defaultColor)
                                embed.add_field(name=f'{p}leaves channel #channel', value=f'This configures which channel the bot should send a message to everytime a user leaves.', inline=False)
                                embed.add_field(name=f'{p}leaves message message', value='This configures what message the bot should send when a user leaves, make sure to replace the user\'s name with {user}.', inline=False)
                                embed.add_field(name='Current Channel:', value=f'{leaveChannel}', inline=True)
                                embed.add_field(name='Current Message:', value=f'{leaveMessage}', inline=True)
                                await message.channel.send(embed=embed)                                        
                        else: 
                                if args[0] == 'channel':
                                        if len(message.channel_mentions) < 1:
                                                await message.channel.send('Please mention a channel to set as your user leaves logging channel!')
                                        else:
                                                db[f"leaveChannel_{message.guild.id}"] = str(message.channel_mentions[0].id)
                                                await message.channel.send(f'Successfully set the user leaves logging channel to {message.channel_mentions[0]}')
                                elif args[0] == 'message':
                                        if len(args) > 1:
                                                space = ' '
                                                msgArgs = args
                                                del msgArgs[:1]
                                                db[f"leaveMessage_{message.guild.id}"] = space.join(msgArgs)
                                                await message.channel.send(f'Successfully set the user leaves logging channel to `{space.join(msgArgs)}`')
                                        else:
                                                await message.channel.send('Please place a leave message after the command!')
                                else:
                                        embed=discord.Embed(title='User Leaves Logging System', description=f'Use this command in one of its 2 forms, {p}leaves channel #channel and {p}leaves message message. You can also easily edit these settings and many more through the dashboard at [Donut.js.org/dashboard](https://donut.js.org/dashboard).', color=defaultColor)
                                        embed.add_field(name=f'{p}leaves channel #channel', value=f'This configures which channel the bot should send a message to everytime a user leaves.', inline=False)
                                        embed.add_field(name=f'{p}leaves message message', value='This configures what message the bot should send when a user leaves, make sure to replace the user\'s name with {user}.', inline=False)
                                        embed.add_field(name='Current Channel:', value=f'{leaveChannel}', inline=True)
                                        embed.add_field(name='Current Message:', value=f'{leaveMessage}', inline=True)
                                        await message.channel.send(embed=embed)                                        
                

        if command == 'messages':
                try:
                    deleteID = db[f"deleteChannel_{message.guild.id}"]
                    deleteChannel = client.get_channel(int(deleteID));
                except:
                    deleteID = 'None'
                    deleteChannel = 'None'

                try:
                    editID = db[f"editChannel_{message.guild.id}"]
                    editChannel = client.get_channel(int(editID))
                except:
                    editID = 'None'
                    editChannel = 'None'
	
                embed=discord.Embed(title='Messages Logging System', description=f'Use this command in one of its 2 forms, {p}messages deletes #channel and {p}messages edits #channel. You can also easily edit these settings and many more through the dashboard at [Donut.js.org/dashboard](https://donut.js.org/dashboard).', color=defaultColor)
                embed.add_field(name=f'{p}messages deletes #channel', value=f'This configures which channel the bot should send a message to everytime a message is deleted in any channel of the server.', inline=False)
                embed.add_field(name=f'{p}messages edits #channel', value='This configures which channel the bot should send a message to everytime a message is edited in any channel.', inline=False)
                embed.add_field(name='Current Deletes Channel:', value=f'{deleteChannel}', inline=True)
                embed.add_field(name='Current Edits Channel:', value=f'{editChannel}', inline=True)
                if message.author.guild_permissions.administrator == False: 
                        await message.channel.send('You do not have admin so you cannot change the message logging settings for this server!')
                else:

                        if len(args) < 1:
                                await message.channel.send(embed=embed)                                        
                        else: 
                                if args[0] == 'deletes':
                                        if len(message.channel_mentions) < 1:
                                                await message.channel.send('Please mention a channel to set as your deleted messages logging channel!')
                                        else:
                                                db[f"deleteChannel_{message.guild.id}"] = str(message.channel_mentions[0].id)
                                                await message.channel.send(f'Successfully set the deleted messages logging channel to {message.channel_mentions[0]}')
                                elif args[0] == 'edits':
                                        if len(message.channel_mentions) < 1:
                                                await message.channel.send('Please mention a channel to set as your edited messages logging channel!')
                                        else:
                                                db[f"editChannel_{message.guild.id}"] = str(message.channel_mentions[0].id)
                                                await message.channel.send(f'Successfully set the edited messages logging channel to {message.channel_mentions[0]}')
                                else:
                                        await message.channel.send(embed=embed)                                        
                