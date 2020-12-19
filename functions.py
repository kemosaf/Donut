async def getGuild(id, bot):
	print('running')
	return await bot.get_guild(int(id))

