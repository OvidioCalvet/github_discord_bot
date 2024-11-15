import creds
import discord
from discord import Color
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def welcome():
    channel = bot.get_channel(creds.WELCOME_CHANNEL_ID)
    await channel.send("test test test")

bot.run(creds.BOT_TOKEN)