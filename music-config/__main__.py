from discord.ext import commands
import os
from threading import Thread
import time
import re
import lavalink
import discord

class Bot:
	def __init__(self, **kwargs):
		self.intents = discord.Intents.default()
		self.intents.members = True
		if "prefix" not in kwargs:
			raise "You must provide a prefix"
		else:
			self.bot = commands.Bot(command_prefix = kwargs["prefix"], intents = self.intents)
			self.bot.lavalinkpass = kwargs["lavalinkpass"]
			self.bot.lavalinkport = kwargs["lavalinkport"]

	def connect(self, token):
		def lavarun():
			os.system("java -jar Lavalink.jar")
		
		print("Starting processes!")
		time.sleep(5)
		print("Running Lavalink.")
		Thread(target = lavarun).start()
		time.sleep(30) #did this on purpose lavalink takes a while to boot up
