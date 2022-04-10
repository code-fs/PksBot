import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('p!'),intents=intents)

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
async def info(ctx):
  embed = discord.Embed(
    title = "Information About Me",
    description = 'I am called Pacemaker, made by **"×¤-|☆ŁÄVÌÈ§†È§☆|-¤/×"#8692**, my prefix is `p!` and here is my commands list.',
    color = 0xFF6500
  )
  embed.add_field(
    name = "**__Moderation__**",
    value = "Working on it",
    inline = False
  )
  embed.add_field(
    name = "**__Information__**",
    value = "`abtusr`,`tc`",
    inline = False
  )
  embed.set_footer(text="<> - Required | [] - Optional")
  
  await ctx.send(embed=embed)
  
@bot.command()
async def abtusr(ctx, user:discord.Member=None):
  if user:
    roles = []
    for role in user.roles:
      roles.append(role.mention)
      
    embed = discord.Embed(
      title = f"About {user}: {user.status}",
      color = 0xFF6500
    )
    embed.add_field(
      name = "**__ID__**",
      value = user.id
    )
    embed.add_field(
      name = "**__Name__**",
      value = user.name
    )
    embed.add_field(
      name = "**__Account Created At__**",
      value = user.created_at
    )
    embed.add_field(
      name = "**__Joined At__**",
      value = user.joined_at
    )
    embed.add_field(
      name = "**__Roles__**",
      value = ', '.join(roles)
    )
    embed.add_field(
      name = "**__Is Bot?__**",
      value = user.bot
    )
    embed.set_thumbnail(url = user.display_avatar)
  else:
    roles = []
    for role in user.roles:
      roles.append(role.mention)
      
    embed = discord.Embed(
      title = f"About You: {ctx.author.status}",
      color = 0xFF6500
    )
    embed.add_field(
      name = "**__ID__**",
      value = ctx.author.id
    )
    embed.add_field(
      name = "**__Name__**",
      value = ctx.author.name
    )
    embed.add_field(
      name = "**__Account Created At__**",
      value = ctx.author.created_at
    )
    embed.add_field(
      name = "**__Joined At__**",
      value = ctx.author.joined_at
    )
    embed.add_field(
      name = "**__Roles__**",
      value = ', '.join(roles)
    )
    embed.add_field(
      name = "**__Is Bot?__**",
      value = ctx.author.bot
    )
    
    embed.set_thumbnail(url = ctx.author.display_avatar)

  await ctx.send(embed=embed)

@bot.command()
async def tc(ctx):
  embed = discord.Embed(
    title = "Tactics",
    description = 'For a team tactic it is simple, stable defense and full pressurer and a golie. A team should adapt to what they are up against, if the enemy goalkeeper is a dangerous kicker and can serve offensive shots from his place, the pressure player will stop looking for angles and instead be close to the enemy keeper. If the enemy keeper Can not go good shots and resorts to passing immediatly, the pressure player should keep pressuring but also look for empty spaces to recieve the ball from his goalkeeper and score, an empty angle may be far from the enemy goalkeeper by he will not be a threat anyways. Defender stays stable.',
    color = 0xFF6500
  )
  
  await ctx.send(embed=embed)
  
bot.run(os.environ['DISCORD_TOKEN'])
