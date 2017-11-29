import asyncio

import discord


def run_command(message, client):
    em = discord.Embed(color=discord.Color.magenta())
    em.set_author(name="Flownyx Help")
    em.add_field(name="flow", value="Shows bot info", inline=False)
    em.add_field(name="bots", value="List of bots I highly recommend", inline=False)
    em.add_field(name="help", value="Displays commands obviously", inline=False)

    asyncio.ensure_future(client.send_message(message.channel, embed=em))
