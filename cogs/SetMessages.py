import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

import json


class SetMessage(commands.Cog):
	def __init__(self, bot):
		self.bot = bot    

	@commands.command()
	@has_permissions(administrator=True)
	async def setally(self, ctx, *, message):
		with open(r"C:\Users\Autopilot\Desktop\1ARC-Recruitment-Bot\config.json", 'r') as f:
			config = json.load(f)

		config["allyMsg"] = message

		with open(r"C:\Users\Autopilot\Desktop\1ARC-Recruitment-Bot\config.json", 'w') as f:
			json.dump(config, f, indent=4)




	@commands.command()
	@has_permissions(administrator=True)
	async def setjoin(self, ctx, *, message):
		with open(r"C:\Users\Autopilot\Desktop\1ARC-Recruitment-Bot\config.json", 'r') as f:
			config = json.load(f)

		config["joinMsg"] = message

		with open(r"C:\Users\Autopilot\Desktop\1ARC-Recruitment-Bot\config.json", 'w') as f:
			json.dump(config, f, indent=4)


def setup(bot):
	bot.add_cog(SetMessage(bot))
