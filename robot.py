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
  embed.set_author(name=member, icon_url=member.display_avatar)
  embed.set_footer(text="Happy to see you!")
  await channel.send(embed=embed)

@bot.command()
async def info():
  embed = discord.Embed(
    title = "Information About Me",
    description = 'I am called Pacemaker, made by **"×¤-|☆ŁÄVÌÈ§†È§☆|-¤/×"#8692**, my prefix is `p!` and here is my commands list.',
    color = 0xFF6500
  )
  embed.add_field(
    name = "**__Moderation__**",
    value = "Working on it"
  )
  embed.add_field(
    name = "**__Information__**",
    value = "Working on it"
  )

bot.run(os.environ['DISCORD_TOKEN'])
