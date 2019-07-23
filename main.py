import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

import json

import ztoken

bot = commands.Bot(command_prefix = "!")
extensions = ["cogs.SetMessages"] # list of cogs to call

@bot.event
async def on_ready():
	print(f"{bot.user.name} - {bot.user.id}")
	print(discord.__version__)
	print("Ready...")

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(588438854738903122) 
	await channel.send(f"{member.mention}, are you a high ranked member of an allied clan and want to be an ally? Or would you like to join the clan.\n *Enter ally or join*")


async def response(message):
	if message.author.id != 603027473151819786 and message.channel.id == 588438854738903122:
		with open(r"C:\Users\wilso\Desktop\1ARC-Recruitment-Bot\config.json", 'r') as f:
			config = json.load(f)

		allyMsg = config["allyMsg"]

		joinMsg = config["joinMsg"]

		channel = message.channel
		author = message.author
		#####
		if message.content.lower() == "join":
			role = discord.utils.get(message.guild.roles, name = "Potential Recruit")
			await author.add_roles(role)
			await channel.send(f"{author.mention}, {joinMsg}")

		elif message.content.lower() == "ally":
			#await self.msg.delete()
			role = discord.utils.get(message.guild.roles, name = "Unverified Allies")
			await author.add_roles(role)
			channel = bot.get_channel(603036173622837279) 
			await channel.send(f"{author.mention}, {allyMsg}")

	#if message.channel.id == 603037936161652746


#bot.add_listener(new_person, 'on_member_join')
bot.add_listener(response, 'on_message')



if __name__ == '__main__':
	for extension in extensions:
		try:
			bot.load_extension(extension)
			print(f"Loaded cog: {extension}")
		except Exception as error:
			print(f"{extension} could not be loaded. [{error}]")
	# bot.loop.create_task(background_loop())
	bot.run(ztoken.token)