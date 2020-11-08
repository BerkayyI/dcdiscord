import discord 
from discord.ext import commands
import random
import asyncio
import time
import os
client = commands.Bot(command_prefix='!')

Token = os.getenv("DISCORD_TOKEN")
client.remove_command("help")

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}({client.user.id}")
    await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name = "Making discordbot", url="https://www.twitch.tv/elraenn"))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        
        await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name = "======", url="https://www.twitch.tv/elraenn"))
        await asyncio.sleep(3)
        await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name = "-------", url="https://www.twitch.tv/elraenn"))
        await asyncio.sleep(3)
        await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name = "xxxxxxxx", url="https://www.twitch.tv/elraenn"))
        await asyncio.sleep(3)
        await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name = "#########", url="https://www.twitch.tv/elraenn"))
        await asyncio.sleep(3)
        await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name = "$$$$$$$$$", url="https://www.twitch.tv/elraenn"))
        await asyncio.sleep(3)


client.run(Token)