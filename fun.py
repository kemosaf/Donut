import server
import discord
import urllib.request, json 
import requests
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

async def funCheck(message, command, args, client, p, defaultColor, fullArgs, snipes):


    #snipe command
    if command == 'snipe':
        if str(message.channel.id) in snipes:
            e=discord.Embed(color=defaultColor)
            e.set_author(name=snipes[str(message.channel.id)]['author'], icon_url=snipes[str(message.channel.id)]['avatar'])
            e.set_footer(text=f"{snipes[str(message.channel.id)]['type']} on {snipes[str(message.channel.id)]['date']}")
            if snipes[str(message.channel.id)]['type'] == 'Deleted':
                e.description = snipes[str(message.channel.id)]['message']
            elif snipes[str(message.channel.id)]['type'] == 'Edited':
                e.add_field(name='Old Message', value=snipes[str(message.channel.id)]['old'], inline=True)
                e.add_field(name='New Message', value=snipes[str(message.channel.id)]['new'], inline=True)
           # if snipes[str(message.channel.id)]['image'] != None:
            #    e.set_image(url=snipes[str(message.channel.id)]['image'])
            await message.channel.send(embed=e)
        else:
            await message.channel.send('There are no edited/deleted recent messages in this channel.')

    #meme command
    if command == 'meme':
            with urllib.request.urlopen("https://meme-api.herokuapp.com/gimme/dankmemes") as url:
                data = json.loads(url.read().decode())
                image = data['url'] 
                post = data['postLink']
                title = data['title']
                e = discord.Embed(title=title, url=post, color=defaultColor)
                e.set_image(url=image)
                await message.channel.send(embed=e)

    #cleanmemememe command
    elif command == 'cleanmeme':
            with urllib.request.urlopen("https://meme-api.herokuapp.com/gimme/cleanmemes") as url:
                data = json.loads(url.read().decode())
                image = data['url'] 
                post = data['postLink']
                title = data['title']
                e = discord.Embed(title=title, url=post, color=defaultColor)
                e.set_image(url=image)
                await message.channel.send(embed=e)

        #cleanmemememe command
    elif command == 'apple':
            with urllib.request.urlopen("https://meme-api.herokuapp.com/gimme/apples") as url:
                data = json.loads(url.read().decode())
                image = data['url'] 
                post = data['postLink']
                title = data['title']
                e = discord.Embed(title='An Apple! 🍎', color=defaultColor)
                e.set_image(url=image)
                await message.channel.send(embed=e)


    #joke command
    #API: https://official-joke-api.appspot.com/random_joke
    elif command == 'joke':
                        with urllib.request.urlopen("https://official-joke-api.appspot.com/random_joke") as url:
                                data = json.loads(url.read().decode())
                                setup = data['setup']
                                punchline = data['punchline']
                                e = discord.Embed(title=setup, color=defaultColor, description=f'||{punchline}||\n ^ Click above to see the answer')
                                await message.channel.send(embed=e)




    #dog command
    elif command == 'dog':
                                res = requests.get(f"""https://no-api-key.com/api/v1/animals/dog""")
                                data = res.json()
                                image = data['image'] 
                                fact = data['fact']
                                e = discord.Embed(title='Random Dog! 🐶', description=f'Fact: {fact}', color=defaultColor)
                                e.set_image(url=image)
                                await message.channel.send(embed=e)
    #cat command
    elif command == 'cat':
                                res = requests.get(f"""https://no-api-key.com/api/v1/animals/cat""")
                                data = res.json()
                                image = data['image'] 
                                fact = data['fact']
                                e = discord.Embed(title='Random Cat! 🐈', description=f'Fact: {fact}', color=defaultColor)
                                e.set_image(url=image)
                                await message.channel.send(embed=e)
    #8ball command
    elif command == '8ball':

                        if ( len(fullArgs) < 1 ):
                                await message.channel.send("What's your question?")
                        else:
                                 possible_responses = ['Of Course Not!','Maybe...','I cannot tell...','Probably.','Yes! 100%!',]
                                 e = discord.Embed(title='8-Ball!', description=f'You Asked: **{fullArgs}**\n\nAnswer: **{random.choice(possible_responses)}**', color=defaultColor)
                                 e.set_thumbnail(url='https://www.clker.com/cliparts/b/o/j/B/l/Z/8-ball.svg.med.png')
                                 await message.channel.send(embed=e)

    #reddit command
    elif command == 'reddit':

                        if ( len(fullArgs) < 1 ):
                                await message.channel.send("Please give a subreddit after the command!")
                        else:
                                progress = await message.channel.send(f'Fetching reddit post from `r/{args[0]}`...')
                                with urllib.request.urlopen(f"https://meme-api.herokuapp.com/gimme/{args[0]}") as url:
                                        data = json.loads(url.read().decode())
                                        image = data['url'] 
                                        post = data['postLink']
                                        title = data['title']
                                        nsfw = data['nsfw']
                                        if(nsfw == True):
                                            return await message.channel.send('⚠ This reddit post contains nsfw content! ⚠\n I cannot show this content or send it!')
                                        e = discord.Embed(title=title, url=post, color=defaultColor)
                                        e.set_image(url=image)
                                        await message.channel.send(embed=e)

    elif command == 'img':
            picture = Image.open("images/6f19683bdac263efd51e3cd4d61b9f82.png")
            done = ImageDraw.Draw(picture)
            done.text((90, 182), 'hi', (255, 255, 255))
            print(picture)
            await message.channel.send(file=discord.File(picture))

