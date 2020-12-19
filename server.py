
from flask import Flask
from threading import Thread
from flask import send_file, send_from_directory, safe_join, abort, g, session, redirect, request, url_for, jsonify, render_template
import os
import random
import requests
import json
import string

app = Flask('')
import discord
from replit import db


import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

client = None
def setClient(bot):
	global client
	client = bot
def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

@app.route('/')
def main():
        style = render_template('style.css')
        homePage = render_template('home.html')
        return homePage.format(style=style, bs='{', bl='}')



@app.route('/invite')
def invite():
    #https://discord.com/oauth2/authorize?client_id=734526487994171392&permissions=8&scope=bot
        return """<meta http-equiv="Refresh" content="0; url='https://discord.com/oauth2/authorize?client_id=734526487994171392&permissions=8&scope=bot'" />"""


@app.route('/loadstaff')
def loadStaff():
	javascript = render_template('loadStaff.js')
	style = render_template('style.css')
	homePage = render_template('load.html')
	return homePage.format(style=style, javascript=javascript)
@app.route('/fetchuser')
def fetchuser():
	user = request.args.get('id')
	if user == None: return 'null'
	person = client.get_user(int(user))
	userDict = {"tag": str(person), "pfp": str(person.avatar_url)}
	from flask import jsonify
	return str(userDict)
@app.route('/staff')
def staffPage():
	staff = ["368071242189897728", "373863238816759819", "549268263289487431", "703282236279226408", "741554642063982692"]
    #^ coolo2, holy cat, kemosaf, chopstix, and UpbeatErmine493
	token = request.args.get('token')
	key = request.args.get('key')
	value = request.args.get('value')
	if token == None or token == 'null':
		return """<meta http-equiv="Refresh" content="0; url='https://discord.com/api/oauth2/authorize?client_id=776729260647907379&redirect_uri=https%3A%2F%2Fdonut.js.org%2Floadstaff&response_type=token&scope=identify%20guilds&prompt=none'" />"""
	else:
		person = requests.get('https://discord.com/api/users/@me', headers={"Authorization" : f"Bearer {token}"})
		if person.status_code == 401:
			return """<meta http-equiv="Refresh" content="0; url='https://discord.com/api/oauth2/authorize?client_id=776729260647907379&redirect_uri=https%3A%2F%2Fdonut.js.org%2Floadstaff&response_type=token&scope=identify%20guilds'" />"""
		person = json.loads(person.text)
		id = person['id']
		if id in staff:
			##^the firewall^##

			if(key != None and value != None):
				if(key == 'blacklists'):
					blacklists = db['blacklists']
					if value in blacklists:
						blacklists.remove(value)
					else:	
						blacklists.append(value)
					db[f'blacklists'] = blacklists
					return 'data entered the database successfully and firewall allowed access'
				else:
					db[f'{key}'] = value
			if person['avatar'] == None:
				userAv = 'https://www.attornify.com/assets/builds/images/no_avatar.jpg'
			else:
				userAv = f"https://cdn.discordapp.com/avatars/{person['id']}/{person['avatar']}.webp?size=4096"

			allServers = ''
			for element in client.guilds:
				if element.icon_url == None:
					serverAv = 'https://intersections.humanities.ufl.edu/wp-content/uploads/2020/07/112815904-stock-vector-no-image-available-icon-flat-vector-illustration-1.jpg'
				else:
					serverAv = element.icon_url
				server = client.get_guild(int(element.id))
				code = get_random_string(6)
				db[f"dashboard_{element.id}_{person['id']}"] = code
				allServers += f"""
    <div class="item">
    <div class="float">
	    
	    <img width=100%; src='{serverAv}'><br>
	       <p style='font-size:15px'><b>{element.name}</b></p><p style='font-size:10px'>ID: {element.id}</p><a href='/render#server={element.id}&user={person['id']}&tag={person['username']}%23{person['discriminator']}&code={code}&token={token}&type=staff'><p><button style='cursor: pointer; background-color:#ff4085'>View Dashboard</button></p></a>
	    </div>  
</div>
				"""
			style = render_template('style.css')
			staffWeb = render_template('staff.html')
			return staffWeb.format(style=style, userAv=userAv, userusername=person['username'], userdiscriminator=person['discriminator'], allServers=allServers, bs='{', bl='}', suggestions=db['suggestions'], issues=db['issues'], token=token, blacklists=db['blacklists'])
	
		else:
			page = render_template('notStaff.html')
			style = render_template('style.css')
			return page.format(style=style)
			return "You aren't part of the staff team! "




@app.route('/dashboard')
def dashboard():
            return """<meta http-equiv="Refresh" content="0; url='https://discord.com/oauth2/authorize?client_id=776729260647907379&redirect_uri=https%3A%2F%2Fdonut.js.org%2Fload&response_type=token&scope=identify%20guilds&prompt=none'" />"""

@app.route('/levels')
def levels():
        users =  db.prefix(f"level_")
        userArray = []
        levels = ''
        i = 0
        if len(users) > 0:
                for element in users:
                        userLvl = db[element]
                        userID = element.replace(f"level_", "")
                        userArray.append({"user": f'{userID}', "lvl": userLvl})
                def get_my_key(obj):
                        return obj['lvl']
                userArray.sort(key=get_my_key)
                userArray.reverse()
                for element in userArray:
                        person = client.get_user(int(element["user"]))
                        i += 1
                        xp = element['lvl']
                        nextInt = int(xp/1000+1) * 1000
                        leftNext = nextInt - xp 
                        thisLevelXp  = 1000 - leftNext
                        if(client.get_user(int(element['user'])) != None):
                            
                            person = client.get_user(int(element['user'])).name + '%23____'
                            member = client.get_user(int(element['user']))
                            try:
                                xpcolor = db[f'cardXp_{element["user"]}']
                            except:
                                xpcolor = 'ff4085'

                            try:
                                bgcolor = db[f'cardBg_{element["user"]}']
                            except:
                                bgcolor = None
                            levels += f'''
                    
                        <center>
                        <img width=800 src='https://vacefron.nl/api/rankcard?username={person}&avatar={client.get_user(int(element['user'])).avatar_url}&level={int(xp/1000)}+++++++++++++Rank+{i}&rank=&currentxp={thisLevelXp}&nextlevelxp=1000&previouslevelxp=0&custombg={bgcolor}&xpcolor={xpcolor}&isboosting=false'>
                        </center>
                        
<br><br><br><br>

                        '''
        page = render_template('levels.html')
        style = render_template('style.css')
        return page.format(style=style, levels=levels)
@app.route('/server')
def dashboardPage():
	req = request.args.get('type')
	user = request.args.get('user')
	server = request.args.get('server')
	code = request.args.get('code')
	token = request.args.get('token')
	key = request.args.get('key')
	value = request.args.get('value')
	try:
		dbCode = db[f"dashboard_{server}_{user}"]
	except:
		dbCode = os.getenv("PASSWORD")
	
	try:
		prefix = db[f"prefix_{server}"]
	except:
		prefix = '?'

	try: 
                currency = db[f"currency_{server}"]
	except:
                currency = 'coins'

	try:
                defaultColor = str(db[f"color_{server}"].replace('0x', '#'))
	except:
                defaultColor = '#ff4085'

	try:
		deleteID = db[f"deleteChannel_{server}"]
		deleteChannel = client.get_channel(int(deleteID));
		check = 'checked'
	except:
		deleteChannel = 'None'
		deleteID = 'None'
		check = ''	

	try:
		editID = db[f"editChannel_{server}"]
		editChannel = client.get_channel(int(editID));
		check = 'checked'
	except:
		editChannel = 'None'
		editID = 'None'
		check = ''	



	try:
		leaveID = db[f"leaveChannel_{server}"]
		leaveChannel = client.get_channel(int(leaveID));
		check = 'checked'
	except:
		leaveChannel = 'None'
		leaveID = 'None'
		check = ''
	try:
		leaveMessage = db[f"leaveMessage_{server}"]
	except:
		leaveMessage = 'None'
	


	try:
		joinID = db[f"joinChannel_{server}"]
		joinChannel = client.get_channel(int(joinID));
		check = 'checked'
	except:
		joinChannel = 'None'
		joinID = 'None'
		check = ''
	try:
		joinMessage = db[f"joinMessage_{server}"]
	except:
		joinMessage = 'None'


	if str(code) == str(dbCode):
		if key != None and value != None:	
			db[f"{key}_{server}"] = str(value)
		
		bs = '{'
		bl = '}'
		guildObj = client.get_guild(int(server))
		if guildObj.icon == None:
			serverAv = 'https://intersections.humanities.ufl.edu/wp-content/uploads/2020/07/112815904-stock-vector-no-image-available-icon-flat-vector-illustration-1.jpg'
		else:
			serverAv = f'https://cdn.discordapp.com/icons/{server}/{guildObj.icon}.webp?size=4096'

		channels = ''
		for element in guildObj.channels:
			if str(element.type) == 'text' or str(element.type) == 'news':
				channels += f'<option value="{element.id}">#{element.name}</option>\n'
		
		if req == 'staff':
			nav = """
     <a href="/">Home</a>
     <a href="/dashboard">Dashboard</a>
     <a href="/levels">Levels</a>
     <a href="/commands">Commands</a>
     <a style='background-color:white;' href="/staff">Staff</a>
     <a href="/about">About</a>
 
			"""
			redirect = 'loadstaff'
		else:
			nav = """
     <a href="/">Home</a>
     <a style='background-color:white;'  href="/dashboard">Dashboard</a>
     <a href="/levels">Levels</a>
     <a href="/commands">Commands</a>
     <a href="/staff">Staff</a>
     <a href="/about">About</a>
 
			"""
			redirect = 'load'
		style = render_template('style.css')
		html = render_template('server.html')
		return html.format(style=style, defaultColor=defaultColor, channels=channels, bs='{', bl='}', serverAv=serverAv, joinChannel=joinChannel, joinID=joinID, joinMessage=joinMessage, leaveChannel=leaveChannel, leaveID=leaveID, leaveMessage=leaveMessage, editChannel=editChannel, editID=editID, deleteChannel=deleteChannel, deleteID=deleteID, prefix=prefix, token=token, guildObj=guildObj, lenguildObjmembers=len(guildObj.members), guildBirthday=guildObj.created_at.strftime('%a, %#d, %B, %Y, %I :%M %p UTC'), server=server, user=user, code=code, nav=nav, redirect=redirect, currency=currency)

	else:
		return "fail"

	
@app.route('/test')
def test():
	token = request.args.get('token')
	user = requests.get('https://discord.com/api/users/@me', headers={"Authorization" : f"Bearer {token}"})
	return str(user.status_code)
@app.route('/profile')
def profile():


	guildList = ''
	noDonut = ''
	noPerms = ''
	name = request.args.get('name')
	value = request.args.get('value')
	token = request.args.get('token')
	user = requests.get('https://discord.com/api/users/@me', headers={"Authorization" : f"Bearer {token}"})
	if user.status_code == 401:
		return """<meta http-equiv="Refresh" content="0; url='https://discord.com/api/oauth2/authorize?client_id=776729260647907379&redirect_uri=https%3A%2F%2Fdonut.js.org%2Fload&response_type=token&scope=identify%20guilds'" />"""
	user = json.loads(user.text)
	guilds = requests.get('https://discord.com/api/users/@me/guilds', headers={"Authorization" : f"Bearer {token}"})
	guilds = guilds.json()
	try:
		xp = db[f"level_{user['id']}"]
	except:
		xp = 0

	nextInt = int(xp/1000+1) * 1000; leftNext = nextInt - xp; thisLevelXp  = 1000 - leftNext

	if token == None or token == 'null':
		return """<meta http-equiv="Refresh" content="0; url='https://discord.com/api/oauth2/authorize?client_id=776729260647907379&redirect_uri=https%3A%2F%2Fdonut.js.org%2Fload&response_type=token&scope=identify%20guilds'" />"""

	if name != None and value != None:
		db[f'{name}_{user["id"]}'] = value
		return "Set!"

	try:
		xpcolor = db[f'cardXp_{user["id"]}']
	except:
		xpcolor = 'ff4085'

	try:
		bgcolor = db[f'cardBg_{user["id"]}']
	except:
		bgcolor = None
	for element in guilds:
		try:
			guildObj = client.get_guild(int(element['id']))
		except:
			guildObj = None
		perms = str(element['permissions'])
		perms = [char for char in perms]

		if len(perms) > 9:
			perms = perms[9]
		else:
			perms = None
		if guildObj != None and perms == '7':
			#7 indicated that the user has admin in that server sikk
			#if guildObj is basically checking that the bot is in the guild and it rtuerned something not None
			code = get_random_string(6)
			db[f"dashboard_{element['id']}_{user['id']}"] = code
			
			if element['icon'] == None:
				serverAv = 'https://intersections.humanities.ufl.edu/wp-content/uploads/2020/07/112815904-stock-vector-no-image-available-icon-flat-vector-illustration-1.jpg'
			else:
				serverAv = f'https://cdn.discordapp.com/icons/{element["id"]}/{element["icon"]}.webp?size=4096'
				
			guildList = guildList + f"""


    <div class="item">
    <div class="float">
	    
	    <img width=100%; src='{serverAv}'><br>
	       <p style='font-size:15px'><b>{element['name']}</b></p><a href='/render#server={element['id']}&user={user['id']}&tag={user['username']}%23{user['discriminator']}&code={code}&token={token}&type=user'><p><button style='cursor: pointer; background-color:#ff4085'>View Dashboard</button></p></a>
	    </div>  
</div>
		"""	
		if guildObj == None and perms == '7':
						
			if element['icon'] == None:
				serverAv = 'https://intersections.humanities.ufl.edu/wp-content/uploads/2020/07/112815904-stock-vector-no-image-available-icon-flat-vector-illustration-1.jpg'
			else:
				serverAv = f'https://cdn.discordapp.com/icons/{element["id"]}/{element["icon"]}.webp?size=4096'
				
			noDonut = noDonut + f"""

		
    <div class="item">
    <div class="float">
	    
	    <img width=100%; src='{serverAv}'><br>
	       <p style='font-size:15px'><b>{element['name']}</b></p><a href='https://discord.com/api/oauth2/authorize?client_id=734526487994171392&permissions=8&scope=bot&guild_id={element['id']}'><p><button style='background-color:gray; cursor: pointer;'>Invite Me</button></p></a>
	    </div>  
</div>
		"""	
		
		if guildObj != None and perms != '7':
									
			if element['icon'] == None:
				serverAv = 'https://intersections.humanities.ufl.edu/wp-content/uploads/2020/07/112815904-stock-vector-no-image-available-icon-flat-vector-illustration-1.jpg'
			else:
				serverAv = f'https://cdn.discordapp.com/icons/{element["id"]}/{element["icon"]}.webp?size=4096'
				
			noPerms = noPerms + f"""

		
    <div class="item">
    <div class="float">
	    
	    <img width=100%; src='{serverAv}'><br>
	       <p style='font-size:15px'><b>{element['name']}</b></p><a><p><button style='background-color:red; cursor: no-drop;'>No Permissions</button></p></a>
	    </div>  
</div>
		"""	
		if user['avatar'] == None:
			userAv = 'https://www.attornify.com/assets/builds/images/no_avatar.jpg'
		else:
			userAv = f"https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.webp?size=4096"

	style = render_template('style.css')
	profilePage = render_template('profile.html')

    #f"https://vacefron.nl/api/rankcard?username={str(member).replace('#', '%23')}&avatar={member.avatar_url}&level={int(xp/100)}&rank=&currentxp={thisLevelXp}&nextlevelxp=1000&previouslevelxp=0&custombg=none&xpcolor=ff4085&isboosting=false"

	return profilePage.format(style=style, userAv=userAv, userusername=user['username'], userdiscriminator=user['discriminator'], userlocale=user['locale'], userid=user['id'], guildList=guildList, noPerms=noPerms, noDonut=noDonut, bs='{', bl='}', levelTag=f"{user['username']}%23{user['discriminator']}", level=int(xp/1000), thisLevelXp=thisLevelXp, token=token, xpcolor=xpcolor, bgcolor=bgcolor)

@app.route('/render')
def render():
	javascript = render_template('guildrender.js')
	style = render_template('style.css')
	page = render_template('load.html')
	return page.format(style=style, javascript=javascript)
@app.route('/load')
def load():
        javascript = render_template('render.js')
        style = render_template('style.css')
        homePage = render_template('load.html')
        return homePage.format(style=style, javascript=javascript)

@app.route('/about')
def about():
        style = render_template('style.css')
        page = render_template('about.html')
        return page.format(style=style)



@app.route('/commands')
def commands():
        style = render_template('style.css')
        page = render_template('commands.html')
        return page.format(style=style)



@app.errorhandler(404)
def page_not_found(e):
        notFound = render_template('notFound.html')
        style = render_template('style.css')
        return notFound.format(style=style)


def run():
    app.run(host="0.0.0.0", port=8080)

def online(client):
    server = Thread(target=run)
    server.start()

#oauth2 link: https://discord.com/api/oauth2/authorize?client_id=776729260647907379&redirect_uri=https%3A%2F%2Fdonut.js.org%2Fload&response_type=token&scope=identify%20guilds