import server
import discord
import urllib.request, json 
import requests
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



async def imageCheck(message, command, args, client, p, defaultColor, fullArgs):



    #changemymind command
    if command == 'changemymind':
        if len(fullArgs) < 1:
            await message.channel.send('Please provide some text after the command.')
        else:
            progress = await message.channel.send('Obtaining Image...')
            plus = '+'
            msg = plus.join(args)
            e = discord.Embed(color=defaultColor)
            e.set_image(url=f'https://vacefron.nl/api/changemymind?text={msg}')
            await message.channel.send(embed=e)
            await progress.delete()



    #simp command
    if command == 'simp':
        if len(message.mentions) < 1:
            member = message.author
        else:
            member = message.mentions[0]
        progress = await message.channel.send('Obtaining Image...')
        plus = '+'
        msg = plus.join(args)
        e = discord.Embed(color=defaultColor)
        e.set_image(url=f'https://api.no-api-key.com/api/v2/simpcard?image={str(member.avatar_url).replace(".webp", "").replace("?size=1024", "")}')
        await message.channel.send(embed=e)
        await progress.delete()


    #shoot command
    if command == 'shoot':
        if len(message.mentions) < 1:
            return await message.channel.send('Who do you want to shoot?')
        progress = await message.channel.send('Obtaining Image...')
        plus = '+'
        member = message.mentions[0]
        msg = plus.join(args)
        e = discord.Embed(color=defaultColor)
        e.set_image(url=f'https://api.no-api-key.com/api/v2/shoot?image={str(member.avatar_url).replace(".webp", "").replace("?size=1024", "")}')
        await message.channel.send(embed=e)
        await progress.delete()


    #trash command
    if command == 'trash':
        if len(message.mentions) < 1:
            member = message.author
        else:
            member = message.mentions[0]
        progress = await message.channel.send('Obtaining Image...')
        plus = '+'
        msg = plus.join(args)
        e = discord.Embed(color=defaultColor)
        e.set_image(url=f'https://api.no-api-key.com/api/v2/trash?image={str(member.avatar_url).replace(".webp", "").replace("?size=1024", "")}')
        await message.channel.send(embed=e)
        await progress.delete()


    #invert command
    if command == 'invert':
        if len(message.mentions) < 1:
            member = message.author
        else:
            member = message.mentions[0]
        progress = await message.channel.send('Obtaining Image...')
        plus = '+'
        msg = plus.join(args)
        e = discord.Embed(color=defaultColor)
        e.set_image(url=f'https://api.no-api-key.com/api/v2/invert?image={str(member.avatar_url).replace(".webp", "").replace("?size=1024", "")}')
        await message.channel.send(embed=e)
        await progress.delete()

    #colorify command
    if command == 'colorify':
        if(len(fullArgs) < 1):
            return await message.channel.send(f'Error! ❌\n Please provide a hex code after the command. Example usage: `{p}colorify #ff4085`, `{p}colorify @Donut #ff4085`.')
        if len(message.mentions) < 1:
            member = message.author
            hex = args[0]
        else:
            member = message.mentions[0]
            hex = args[1]
        progress = await message.channel.send('Obtaining Image...')
        if(hex.startswith('#') == False):
            return await message.channel.send('Error! ❌\n Please provide a valid hex code after the command.')
        plus = '+'
        msg = plus.join(args)
        e = discord.Embed(color=defaultColor)
        e.set_image(url=f'https://api.no-api-key.com/api/v2/customify?image={str(member.avatar_url).replace(".webp", "").replace("?size=1024", "")}&color={hex.replace("#", "")}')
        await message.channel.send(embed=e)
        await progress.delete()


    #wide command
    if command == 'wide':
        if len(message.mentions) < 1:
            member = message.author
        else:
            member = message.mentions[0]
        progress = await message.channel.send('Obtaining Image...')
        plus = '+'
        msg = plus.join(args)
        e = discord.Embed(color=defaultColor)
        e.set_image(url=f'https://vacefron.nl/api/wide?image={member.avatar_url}')
        await message.channel.send(embed=e)
        await progress.delete()


    #deepfry command
    if command == 'deepfry':
        if len(message.mentions) < 1:
            member = message.author
        else:
            member = message.mentions[0]
        progress = await message.channel.send('Obtaining Image...')
        res = requests.get(f"""https://nekobot.xyz/api/imagegen?type=deepfry&image={member.avatar_url}""")
        data = res.json()
        e = discord.Embed(color=defaultColor)
        e.set_image(url=data['message'])
        await message.channel.send(embed=e)
        await progress.delete()


    #deepfry command
    if command == 'slap':
        if(len(args) > 1):
            msgArgs = args
            del msgArgs[:1]
            space = '+'
            msg = space.join(msgArgs)
        else:
            msg = message.author.name
        if len(message.mentions) < 1:
            return await message.channel.send('Please provide a user to slap after the command!')
        progress = await message.channel.send('Obtaining Image...')
        e = discord.Embed(color=defaultColor)
        e.set_image(url=f"https://vacefron.nl/api/batmanslap?text1={message.mentions[0].name.replace(' ', '-')}&text2={msg}&batman={message.author.avatar_url}&robin={message.mentions[0].avatar_url}")
        await message.channel.send(embed=e)
        await progress.delete()

    #clyde command
    if command == 'clyde':
        if len(fullArgs) < 1:
            await message.channel.send('Please provide a message after the command.')
        else:
            progress = await message.channel.send('Obtaining Image...')
            res = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={fullArgs}")
            data = res.json()
            e = discord.Embed(color=defaultColor)
            e.set_image(url=data['message'])
            await message.channel.send(embed=e)
            await progress.delete()

    #threats command
    if command == 'threats':
        if len(message.mentions) < 1:
            member = message.author
        else:
            member = message.mentions[0]
        #userAv = f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png?size=1024"
        progress = await message.channel.send('Obtaining Image...')
        res = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={member.avatar_url}")
        data = res.json()
        e = discord.Embed(color=defaultColor)
        e.set_image(url=data['message'])
        await message.channel.send(embed=e)
        await progress.delete()
	#captcha command
    if command == 'captcha':
            if len(message.mentions) < 1:
                member  = message.author
            else:
                member = message.mentions[0]
            #userAv = f'https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png?size=4096'
            progress = await message.channel.send('Obtaining Image...')
            res = requests.get(f"""https://nekobot.xyz/api/imagegen?type=captcha&url={member.avatar_url}&username={member.name}""") 
            data = res.json()
            e = discord.Embed(color=defaultColor)
            e.set_image(url=data['message'])
            await message.channel.send(embed=e)
            await progress.delete()

    #trumptweet command
    if command == 'trumptweet':
            plus = '+'
            msg = plus.join(args)
            progress = await message.channel.send('Obtaining Image...')
            res = requests.get(f"""https://nekobot.xyz/api/imagegen?type=trumptweet&text={msg}""") 
            data = res.json()
            e = discord.Embed(color=defaultColor)
            e.set_image(url=data['message'])
            await message.channel.send(embed=e)
            await progress.delete()

	#tweet command
    if command == 'tweet':
            plus = '+'
            msg = plus.join(args)
            userAv = f'https://cdn.discordapp.com/avatars/{message.author.id}/{message.author.avatar}.png?size=4096'
            progress = await message.channel.send('Obtaining Image...')
            with urllib.request.urlopen(f"""http://tweet-api.kemosaf5.repl.co/tweet?author={message.author.name.replace(' ', '-')}&avatar={userAv}&message={msg}&type=f""") as url:
                data = json.loads(url.read().decode())
                e = discord.Embed(color=defaultColor)
                e.set_image(url=data['link'])
                await message.channel.send(embed=e)
                await progress.delete()