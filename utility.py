import discord
import time
from replit import db
from datetime import datetime
from pytz import timezone

async def utilityCheck(message, command, args, client, p, defaultColor, fullArgs):

	if(command == 'unmute'):
		if(message.author.guild_permissions.manage_roles == False): return await message.channel.send("You need the `MANAGE_ROLES` permission in order to unmute other users in this guild.")
		if(len(message.mentions) < 1): return await message.channel.send('Please mention someone to unmute them.')
		role = discord.utils.get(message.guild.roles, name="muted-donut")
		person = message.mentions[0]
		if role == None: return await message.channel.send(f"The muted role does not exist in the server and **{person.name}** is not Muted.")
		if role not in person.roles: return await message.channel.send(f"**{person.name}** is not Muted.")
		await person.remove_roles(role)
		await message.channel.send(f"You have unmuted **{person.name}**.")
	if(command == 'mute'):
		if(message.author.guild_permissions.manage_roles == False): return await message.channel.send("You need the `MANAGE_ROLES` permission in order to mute other users in this guild.")
		if(len(message.mentions) < 1): return await message.channel.send('Please mention someone to mute them.')
		toMute = message.mentions[0]
		toMuteMember = message.guild.get_member(toMute.id)
		if(toMuteMember.guild_permissions.administrator == True): return await message.channel.send("This person has the `ADMINISTRATOR` permission meaning they cannot be muted.")
		role = discord.utils.get(message.guild.roles, name="muted-donut")
		if(role == None):
			await message.channel.send("The `muted-donut` role wasn't found. Generating a new one...")
			role = await message.guild.create_role(name='muted-donut')
			for channel in message.guild.channels:
				await channel.set_permissions(role, speak=False, send_messages=False)

		await toMute.add_roles(role)
		await message.channel.send(f"You have muted **{toMute.name}**.")

	if(command == 'clear'):
                if message.author.guild_permissions.manage_messages == False: return await message.channel.send(f"You need the `MANAGE_MESSAGES` permission in order to clear messages.")
                if len(fullArgs) < 1:
                        await message.channel.send('Please provide a number of messages to delete after the command!')
                else:   
                        amount = str(args[0])
                        digit = amount.isdigit()
                        print(fullArgs)
		 
                        if(digit == True):
                                if int(amount) < 100 and int(amount) > 0:
                                        deleted = await message.channel.purge(limit = int(amount) + 1)
                                        done = await message.channel.send(f'Sucessfully deleted **{len(deleted)}** messages in {message.channel}!')
                                        time.sleep(1)
                                        await done.delete()
                                else: 
                                        await message.channel.send('Please provide a number between 1 and 100!')
                        else:
                                await message.channel.send('Please provide a valid number!')
	if command == 'poll' or command == 'vote':
		if(len(fullArgs) < 1): return await message.channel.send(f'Please either provide a yes or no poll or a multiple choice poll. Examples: \n Yes or No: `{p}poll How are you?`\n Multiple Choice: `{p}poll How are you?: Good - Excited - Bored`')
		subDash = ''
		subColon = ':'
		if(subDash in fullArgs and subColon in fullArgs):
			question = fullArgs.split(':')[0]
			msgArgs = fullArgs.split(':')
			del msgArgs[:1]
			strOptions = ' '.join(msgArgs)
			options = strOptions.split('-')
			optionsDesc = ""
			i = -1
			if(len(options) > 20): return await message.channel.send('The max amount of reactions on a Discord message is 20! I cannot put more than that. Please provide 20 options max.')
			if(len(options) < 2): return await message.channel.send('Please provide at least 2 options.')
			reactions = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿']
			for element in options: i+=1;optionsDesc += f"{reactions[i]} = {element}\n\n"
			e = discord.Embed(color=defaultColor, title=question, description=optionsDesc)
			e.set_author(name=message.author, icon_url=message.author.avatar_url)
			msg = await message.channel.send(embed=e)
			i = -1
			for element in options: i+=1;await msg.add_reaction(f"{reactions[i]}")
		else:
			question = fullArgs
			e = discord.Embed(color=defaultColor, title=question)
			e.set_author(name=message.author, icon_url=message.author.avatar_url)
			msg = await message.channel.send(embed=e)
			await msg.add_reaction('✅')
			await msg.add_reaction('❌')

	if command == 'clear-warns':
		if(message.author.guild_permissions.manage_roles == False): return await message.channel.send("You need the `MANAGE_ROLES` permission in order to manage people's warns.")
		if(len(message.mentions) < 1): return await message.channel.send("Please provide a user to remove their warns.")
		person = message.mentions[0]
		db[f"warns_{message.guild.id}_{person.id}"] = []
		await message.channel.send(f"You have cleared **{person.name}**'s warns.")
	if command == 'warn':
		if(message.author.guild_permissions.manage_roles == False): return await message.channel.send("You need the `MANAGE_ROLES` permission in order to warn people.")
		if(len(message.mentions) < 1): return await message.channel.send("Please provide a user to warn after the command.")
		person = message.mentions[0]
		if(len(args) < 2):
			warnReason = 'No Reason'
		else:
			msgArgs = args
			del msgArgs[:1]
			warnReason = " ".join(msgArgs)
		try:
			warns = db[f"warns_{message.guild.id}_{person.id}"]
		except:
			warns = []
		est = timezone('EST')
		date = datetime.now(est).strftime('%l:%M%p %Z on %b %d, %Y')
		finalDate = f"{date}"
		warns.append({"date": date, "mod": str(message.author), "reason": warnReason})
		db[f"warns_{message.guild.id}_{person.id}"] = warns
		await message.channel.send(f"You have warned **{person.name}** for **{warnReason}** on **{date}**.")
	if command == 'warns':
		if(len(message.mentions) < 1): 
			person = message.author
		else:
			person = message.mentions[0]

		try:
			warns = db[f"warns_{message.guild.id}_{person.id}"]
		except:
			warns = []
		e = discord.Embed(color=defaultColor, title=f'__{person.name}\'s Warns in {message.guild.name}__')
		for element in warns:
			e.add_field(name=f"{element['date']}", value=f"Warned By: {element['mod']}\nReason for Warn: {element['reason']}", inline=False)
		if(len(warns) < 1): e.add_field(name='None', value=f"{person.name} has no warns in {message.guild.name}!")
		await message.channel.send(embed=e)
	if command == 'kick':
                if message.author.guild_permissions.kick_members == False: 
                        await message.channel.send('You do not have the kick members permission!')
                else:
                        if len(message.mentions) < 1:
                                await message.channel.send('Who do you want to kick?')
                        else:
                                user = message.mentions[0]
                                member = message.guild.get_member(user.id)
                                if len(args) < 2:
                                        kickReason = 'None'
                                else:
                                        msgArgs = args
                                        del msgArgs[:1]
                                        space = ' '
                                        kickReason = space.join(msgArgs)
                                try:
                                        await member.kick(reason=f'{message.author}: {kickReason}')
                                        embed=discord.Embed(title=f'Action: Kicked {member}', color=defaultColor)
                                        embed.add_field(name='Kicked User ID:', value=member.id)
                                        embed.add_field(name='Reason:', value=kickReason)
                                        embed.add_field(name='Kicked By:', value=message.author)
                                        await message.channel.send(embed=embed)
                                except:
                                        await message.channel.send("I don't have enough permissions to do that!")

	if command == 'ban':
                if message.author.guild_permissions.ban_members == False: 
                        await message.channel.send('You do not have the ban members permission!')
                else:
                        if len(message.mentions) < 1:
                                await message.channel.send('Who do you want to ban?')
                        else:
                                user = message.mentions[0]
                                member = message.guild.get_member(user.id)
                                if len(args) < 2:
                                        banReason = 'None'
                                else:
                                        msgArgs = args
                                        del msgArgs[:1]
                                        space = ' '
                                        banReason = space.join(msgArgs)
                                try:
                                        await member.ban(reason=f'{message.author}: {banReason}')
                                        embed=discord.Embed(title=f'Action: Banned {member}', color=defaultColor)
                                        embed.add_field(name='Banned User ID:', value=member.id)
                                        embed.add_field(name='Reason:', value=banReason)
                                        embed.add_field(name='Banned By:', value=message.author)
                                        await message.channel.send(embed=embed)
                                except:
                                        await message.channel.send("I don't have enough permissions to do that!")