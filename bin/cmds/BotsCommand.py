import asyncio

import discord


def run_command(message, client):
	em = discord.Embed(color=discord.Color.magenta())
	em.set_author(name="Flownyx")
	em.description = "Bots I suggest you check out!"
	em.add_field(name="DisCal", value="Advanced GoogleCalendar bot: https://www.cloudcraftgaming.com/discal",
	             inline=False)
	em.add_field(name="Apparatus", value="Advanced multi-purpose bot: http://www.xaanit.me/Products/", inline=False)

	asyncio.ensure_future(client.send_message(message.channel, embed=em))
