import asyncio

import discord


def run_command(message, client):
	em = discord.Embed(color=discord.Color.magenta())
	em.set_author(name="Flownyx =^.^=")
	em.add_field(name="Version", value="1.0.0", inline=True)
	em.add_field(name="Library", value="Discord.py", inline=True)
	em.add_field(name="Author", value="NovaFox", inline=False)
	em.add_field(name="Guilds", value=str(len(client.servers)), inline=True)

	asyncio.ensure_future(client.send_message(message.channel, embed=em))
