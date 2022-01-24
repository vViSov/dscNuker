from os import getenv
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('The bot is online!')

bot.run(getenv('TOKEN'))
