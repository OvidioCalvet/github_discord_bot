import creds 
import discord
from discord import Color
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())



@bot.event
async def welcome():
    channel = bot.get_channel(creds.WELCOME_CHANNEL_ID)
    await channel.send("Welcome to the server!")


@bot.event
async def on_ready():
    channel = bot.get_channel(creds.WELCOME_CHANNEL_ID)
    print(f"Bot is ready in {channel}")
    await channel.send("Bot INITIALIZED!")

@bot.command()
async def disconnect(ctx):
    await ctx.send("Disconnecting...")
    await ctx.send("Bot DISCONNECTED!")
    await bot.close()

bot.run(creds.BOT_TOKEN)
