import creds
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = discord.ext.commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def welcome():
    print('Github Bot has landed!!!')

bot.run(creds.BOT_TOKEN)