import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("p!"), intents=intents, slash_command_guilds=[922247223088123924])

@bot.event
async def on_ready():
  print("Ready To Help!")
  
@bot.event
async def on_member_join(member):
  channel = client.get_channel(901099381665718303)
  embed = discord.Embed(
    title = "Welcome to the server",
    description = f"How are you doing? Before hoping into the fun, make sure to read the rules in <#962096867783626812> and join the team by opening a ticket in <#962096867783626812> then follow along.",
    color = 0xFF6500
  )
  embed.set_author(name=mention)
  await channel.send('hello')

bot.run(os.environ['DISCORD_TOKEN'])
