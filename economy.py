import server
from replit import db
import discord
import urllib.request, json 
import random
import json
from threading import Timer
from replit import db
from datetime import datetime
from datetime import timedelta
from pytz import timezone

async def ecoCheck(message, command, args, client, p, defaultColor, fullArgs, cooldowns):

    if command == 'daily':
      #if message.author.id != 123: return await message.channel.send("Even though this command has been developed it will not get released until a day or more, this is because of the unstable server and the cooldowns.")
      if f"daily_{message.guild.id}_{message.author.id}" in cooldowns:
          est = timezone('EST')
          now = datetime.now(est)
          coolDownOver = now + timedelta(minutes = 720)
          ranTime = cooldowns[f"daily_{message.guild.id}_{message.author.id}"]
          difference = coolDownOver-ranTime
          totalSecs = difference.total_seconds() - 43200
          timeLeft = 43200-totalSecs
          e = discord.Embed(color=defaultColor, title="You're on Cooldown!", description=f"{message.author.name}, you're on cooldown, please try this command again in `{round(timeLeft/3600, 2)}` hours.")
          await message.channel.send(embed=e)
      else:
        try: 
            currency = db[f"currency_{message.guild.id}"]
        except:
            currency = 'coins'
        try:
                bal = db[f"eco_{message.guild.id}_{message.author.id}"]
        except:
                bal = 0

        db[f"eco_{message.guild.id}_{message.author.id}"] = bal+5000
        e = discord.Embed(color=defaultColor, title='Daily Reward', description=f"""
        {message.author.name}, you have claimed your daily reward and 5,000 {currency} were added to your cash balance, you can use this command again in 12 hours.
        """)
        await message.channel.send(embed=e)
        est = timezone('EST')
        now = datetime.now(est)
        cooldowns[f"daily_{message.guild.id}_{message.author.id}"] = now
        def removeCooldown():
          del cooldowns[f"daily_{message.guild.id}_{message.author.id}"]
        t = Timer(43200.0, removeCooldown)
        t.start()


    if command == 'rob':
      if f"rob_{message.guild.id}_{message.author.id}" in cooldowns:
          est = timezone('EST')
          now = datetime.now(est)
          coolDownOver = now + timedelta(minutes = 5)
          ranTime = cooldowns[f"rob_{message.guild.id}_{message.author.id}"]
          difference = coolDownOver-ranTime
          totalSecs = difference.total_seconds() - 300
          timeLeft = 300-totalSecs
          e = discord.Embed(color=defaultColor, title="You're on Cooldown!", description=f"{message.author.name}, you're on cooldown, please try this command again in `{round(timeLeft/60, 2)}` minutes.")
          await message.channel.send(embed=e)
      else:
        #if(str(message.author.id) != '549268263289487431'): return await message.channel.send('❌ Since this command is still being developed only the owner can access it and use it (kemosaf) ❌')
        try: 
            currency = db[f"currency_{message.guild.id}"]
        except:
            currency = 'coins'
		
        if(len(message.mentions) < 1): return await message.channel.send("Please provide a user to rob after the command.")
        member = message.mentions[0]
        try:
                bal = db[f"eco_{message.guild.id}_{member.id}"]
        except:
                bal = 0

        try:
                bank = db[f"bank_{message.guild.id}_{member.id}"]
        except:
                bank = 0

        cash = bal - bank

        try:
            robberBal = db[f"eco_{message.guild.id}_{message.author.id}"]
        except:
            robberBal = 0
        if cash < 1: return await message.channel.send(f"**{member.name}** doesn't have any cash on them! They either deposited at the bank or just don't have money.")
        success = random.randint(1,101)
        if success < 30:
            lost = random.randint(700,1500)
            newBal = robberBal - lost
            db[f"eco_{message.guild.id}_{message.author.id}"] = newBal
            e = discord.Embed(color=defaultColor, title='You Were Caught! ❌', description=f"You got caught trying to rob **{member.name}**, you paid fine of `{lost}` {currency} for your attempted robbery.")
            await message.channel.send(embed=e)
        else:
            amount = int(cash * 0.80)
            robberNewBal = robberBal + amount
            robbedNewBal = bal - amount
            db[f"eco_{message.guild.id}_{message.author.id}"] = robberNewBal
            db[f"eco_{message.guild.id}_{member.id}"] = robbedNewBal
            e = discord.Embed(color=defaultColor, title='Robbery Successful! ✅', description=f"You have successfully robbed **{member.name}** and was able to get 80% of their cash which is `{amount}` {currency}!")
            await message.channel.send(embed=e)

        est = timezone('EST')
        now = datetime.now(est)
        cooldowns[f"rob_{message.guild.id}_{message.author.id}"] = now
        def removeCooldown():
          del cooldowns[f"rob_{message.guild.id}_{message.author.id}"]
        t = Timer(300.0, removeCooldown)
        t.start()

        
        

    if command =='currency':
            try: 
                currency = db[f"currency_{message.guild.id}"]
            except:
                currency = 'coins'
            if message.author.guild_permissions.administrator == False:
                    await message.channel.send('You need to have the `administrator` permission to be able to change the currency for this server.')
            else:
                    if len(args) < 1:
                            await message.channel.send('Please provide the currency you would like to have for the economy system in this server after the command.')
                    else:
                            db[f"currency_{message.guild.id}"] = fullArgs
                            await message.channel.send(f'Successfully set the new currency to: {fullArgs}')
    if command == 'setbalance':
            try: 
                currency = db[f"currency_{message.guild.id}"]
            except:
                currency = 'coins'
            if message.author.guild_permissions.administrator == False: 
                        await message.channel.send('You need to have the `administrator` permission to be able to set the balance for other users.')
            else:
                        if len(message.mentions) < 1:
                                await message.channel.send('Who\'s balance would you like to change? Please mention someone after the command!')
                        else:
                                if len(args) < 2:
                                        await message.channel.send('Please provide the amount you would like to give the user after the command!')
                                else:
                                        try:
                                                bal = db[f"eco_{message.guild.id}_{message.mentions[0].id}"]
                                        except:
                                                bal = 0
        
                                        if str(args[1]).isdigit() == False:
                                                await message.channel.send('Please provide a valid number after the command!')
                                        else:
                                                db[f"eco_{message.guild.id}_{message.mentions[0].id}"] = int(args[1])
                                                db[f"bank_{message.guild.id}_{message.mentions[0].id}"] = 0

                                                e = discord.Embed(title=f'Successfully Changed {message.mentions[0].name}\'s Balance!', color=defaultColor)
                                                e.add_field(name='New Balance:', value=db[f"eco_{message.guild.id}_{message.mentions[0].id}"])
                                                e.add_field(name='Old Balance', value=bal)
                                                e.add_field(name='Amount Added/Removed', value=db[f"eco_{message.guild.id}_{message.mentions[0].id}"]-bal)
                                                await message.channel.send(embed=e)
		      


    if command == 'work':
        try: 
                currency = db[f"currency_{message.guild.id}"]
        except:
                currency = 'coins'
        try:
                bal = db[f"eco_{message.guild.id}_{message.author.id}"]


        except:
                bal = 'not-started'
                

        if bal == 'not-started': 
                await message.channel.send(f'You do not have an economy account! Try starting one with {p}start')
        else:
                
                if f"eco_{message.guild.id}_{message.author.id}" in cooldowns:
                        est = timezone('EST')
                        now = datetime.now(est)
                        coolDownOver = now + timedelta(minutes = 1)
                        ranTime = cooldowns[f"eco_{message.guild.id}_{message.author.id}"]
                        difference = coolDownOver-ranTime
                        totalSecs = difference.total_seconds() - 60
                        timeLeft = 60-totalSecs
                        e = discord.Embed(color=defaultColor, title="You're on Cooldown!", description=f"{message.author.name}, you're on cooldown, please try this command again in `{round(timeLeft, 2)}` seconds.")
                        await message.channel.send(embed=e)
                else:
                        gained = random.randint(0,500)
                        newBal = gained + bal
                        db[f"eco_{message.guild.id}_{message.author.id}"] = newBal
                        newBal = db[f"eco_{message.guild.id}_{message.author.id}"]
                        work_replies = [f'For some reason you decided to eat a tide pod for content, your video goes viral and get 5 billion views, your success leads you to getting a {gained} {currency} reward.', f'You went on Omegle and a random person decided to share their credit card info with you, you go on their account and find {gained} {currency}, you transfered it to your account and skipped them.', f'You sneaked into area 51 for some views, you found a lot of secrets in there, the government paid you {gained} {currency} to not tell anyone about anything you saw inside.', f'You helped the CDC find a cure for COVID-19 and got paid {gained} {currency} for your hard work.', f'You saw an old man and helped them cross the street, they liked your kindness and kindly gave you {gained} {currency}', f'You got bullied at school for posting a dance video on tiktok, the new kid felt bad and gave you {gained} {currency}', f'On your way back home from the movies you find a big bag with {gained} {currency} laying on the ground, you take it without telling a soul.', f'You helped a random lady fix her flat tire, she was so thankful that she gave you {gained} {currency} ']
                        
                        e = discord.Embed(color=defaultColor, description=f'{random.choice(work_replies)}')
                        e.set_author(name=message.author, icon_url=message.author.avatar_url)
                        await message.channel.send(embed=e)
                        est = timezone('EST')
                        now = datetime.now(est)
                        cooldowns[f"eco_{message.guild.id}_{message.author.id}"] = now
                        def removeCooldown():
                                del cooldowns[f"eco_{message.guild.id}_{message.author.id}"]

                        t = Timer(60.0, removeCooldown)
                        t.start()

    elif command == 'start':
        try: 
                currency = db[f"currency_{message.guild.id}"]
        except:
                currency = 'coins'

        try:
                bal = db[f"eco_{message.guild.id}_{message.author.id}"]

        except:
                bal = 'not-started'
                

        if bal == 'not-started': 
                db[f"eco_{message.guild.id}_{message.author.id}"] = 1000
                e = discord.Embed(title='Economy Account!', color=defaultColor, description=f'You have successfully started your economy account and you will start off at 1k {currency}!!')
                await message.channel.send(embed=e)
        else:
                await message.channel.send('You have already started your economy account!')



    elif command == 'balance' or command == 'bal':
        try: 
                currency = db[f"currency_{message.guild.id}"]
        except:
                currency = 'coins'

        if ( len(fullArgs) < 1 ):
                member  = message.author  
        else:
                member = message.mentions[0]
                
  
        try:
                bal = db[f"eco_{message.guild.id}_{member.id}"]

        except:
                bal = 0

        try:
                bank = db[f"bank_{message.guild.id}_{member.id}"]
        except:
                bank = 0
        cash = bal - bank
        e = discord.Embed(color=defaultColor)
        e.set_author(name=member, icon_url=member.avatar_url)
        e.add_field(name='Bank 🏦', value=bank, inline=True)
        e.add_field(name='Cash 💵', value=cash, inline=True)
        e.add_field(name='Total 💰', value=bal, inline=True)
        await message.channel.send(embed=e)





    elif command == 'with' or command == 'withdraw':
        try: 
                currency = db[f"currency_{message.guild.id}"]
        except:
                currency = 'coins'
        member  = message.author  
        try:
                bal = db[f"eco_{message.guild.id}_{member.id}"]

        except:
                bal = 0

        try:
                bank = db[f"bank_{message.guild.id}_{member.id}"]
        except:
                bank = 0
        cash = bal - bank
        if(len(fullArgs) < 1): return await message.channel.send(f'❌Please provide an amount you would like to withdraw from the bank. You currently have `{bank}` {currency} IN❌')
        if str(args[0]).isdigit() == False: return await message.channel.send(f"❌Please provide a valid amount after the command! Make sure to not include any commas or spaces!❌")
        if(int(args[0]) < 1): return await message.channel.send(f'❌You cannot withdraw less than `1` {currency}❌')
        if(int(args[0]) > bank): return await message.channel.send(f"❌You cannot withdraw more than `{bank}` since you only have `{bank}` {currency} in your bank account.❌")
        db[f"bank_{message.guild.id}_{member.id}"] = bank - int(args[0])
        await message.channel.send(f'Success! ✅\n You successfully withdrew `{args[0]}` {currency} at the bank!')



    elif command == 'dep' or command == 'deposit':
        try: 
                currency = db[f"currency_{message.guild.id}"]
        except:
                currency = 'coins'
        member  = message.author  
        try:
                bal = db[f"eco_{message.guild.id}_{member.id}"]

        except:
                bal = 0

        try:
                bank = db[f"bank_{message.guild.id}_{member.id}"]
        except:
                bank = 0
        cash = bal - bank
        if(len(fullArgs) < 1): return await message.channel.send(f'❌Please provide an amount you would like to deposit at the bank. You currently have `{cash}` {currency} with you as cash.❌')

        if(args[0].lower() != 'all'):
            if str(args[0]).isdigit() == False: return await message.channel.send(f"❌Please provide a valid amount after the command! Make sure to not include any commas or spaces!❌")
            if(int(args[0]) < 1): return await message.channel.send(f'❌You cannot deposit less than `1` {currency}❌')
            if(int(args[0]) > cash): return await message.channel.send(f"❌You cannot deposit more than `{cash}` since you only have `{cash}` {currency} with you as cash.❌")
            amount = int(args[0])
            db[f"bank_{message.guild.id}_{member.id}"] = int(args[0]) + bank
        else:
            amount = cash
            db[f"bank_{message.guild.id}_{member.id}"] = cash + bank
        e = discord.Embed(color=defaultColor, title='Success!', description=f"""You have successfully deposited `{amount}` {currency} at the bank! Try `{p}bal` to see more balance.""")
        await message.channel.send(embed=e)

    elif command == 'lb' or command == 'leaderboard':
        try: 
                currency = db[f"currency_{message.guild.id}"]
        except:
                currency = 'coins'
        users =  db.prefix(f"eco_{message.guild.id}_")
        userArray = []
        leaderboard = ''
        i = 0
        if len(users) > 0:
                for element in users:
                        userBal = db[element]
                        userID = element.replace(f"eco_{message.guild.id}_", "")
                        userArray.append({"user": f'{userID}', "balance": userBal})
                def get_my_key(obj):
                        return obj['balance']
                userArray.sort(key=get_my_key)
                userArray.reverse()
                for element in userArray:
                        i += 1
                        
                        try:
                                bank = db[f"bank_{message.guild.id}_{element['user']}"]
                        except:
                                bank = 0
                        cash = element["balance"] - bank
                        leaderboard += f' {i}) **{client.get_user(int(element["user"]))}** - Total: {element["balance"]} {currency} (Bank: {bank} | Cash: {cash})\n'
                e = discord.Embed(title=f'{message.guild.name}\'s Leaderboard', color=defaultColor, description=f'{leaderboard}')
                await message.channel.send(embed=e)
        else:
                await message.channel.send('No one in this server seems to have an economy account!')
