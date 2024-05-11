from func import *
import discord
from discord.ext import commands
from time import sleep

intents = discord.Intents.default()
intents.message_content = True

command_info = [
    '1. .eco_facts - экологические советы',
    '2. .info - все команды',
]

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def eco_facts(ctx):
    await ctx.send(random_facts())

@bot.command()
async def info(ctx):
    for i in command_info:
        await ctx.send(i)

bot.run('')


