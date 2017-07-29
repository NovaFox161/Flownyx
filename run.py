import discord

from bin.file import FileReader

client = discord.Client()


@client.event
async def on_ready():
	print("Logged in as:")
	print(client.user.name)
	print(client.user.id)


@client.event
async def on_message(message):
	print("Received message: " + message.content)
	if message.content == "~test":
		await client.send_message(message.channel, "Hello World!")


client.run(FileReader.get_bot_settings()[0])
