import discord

from bin.cmds import CommandHandler
from bin.file import FileReader

client = discord.Client()


@client.event
async def on_ready():
	print("Successfully logged in!")
	print(client.user.name)


@client.event
async def on_message(message):
	print("Received message: " + message.content)
	CommandHandler.handle_command(message, client)


client.run(FileReader.get_bot_settings()[0])
