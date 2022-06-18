import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('pks '),intents=intents)
bot.help_command = None

@bot.event
async def on_ready():
  print("Ready To Help!")
  
@bot.event
async def on_member_join(member):
  channel = bot.get_channel(901099381665718303)
  embed = discord.Embed(
    title = "Welcome to the server",
    description = f"How are you doing? Before hoping into the fun, make sure to read the rules in <#962096867783626812> and join the team by opening a ticket in <#962096867783626812> then follow along.",
    color = 0xFF6500
  )
  embed.set_author(name=member, icon_url=member.display_avatar)
  embed.set_footer(text="Happy to see you!")
  await channel.send(embed=embed)

@bot.command()
async def help(ctx):
  embed = discord.Embed(
    title = "Information About Me",
    description = 'I am called Pacemaker, made by **"×¤-|☆ŁÄVÌÈ§†È§☆|-¤/×"#8692**, my prefix is `p!` or you can mention me. Here is my commands list.',
    color = 0xFF6500
  )
  embed.add_field(
    name = "**__Moderation__**",
    value = "`accept`, `abort`",
    inline = False
  )
  embed.add_field(
    name = "**__Utility__**",
    value = "`st`, `abtusr`, `tc`, `server`",
    inline = False
  )
  embed.set_footer(text="<> - Required | [] - Optional")
  
  await ctx.send(embed=embed)
  
@bot.command()
async def server(ctx):
  embed = discord.Embed(
    title = f"About {ctx.guild.name}",
    color = 0xFF6500
  )
  embed.add_field(
    name = "Server Created At",
    value = ctx.guild.created_at
  )
  embed.add_field(
    name = "Server Owner",
    value = ctx.guild.owner
  )
  embed.add_field(
    name = "Server's Owner ID",
    value = ctx.guild.owner_id
  )
  embed.set_thumbnail(url = ctx.guild.icon)
  
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

@bot.command()
async def st(ctx, *, suggestion):
  channel = bot.get_channel(955093721093910578)
  embed = discord.Embed(
    title = "Tactic Suggestion Submitted!",
    description = "Your suggestion will be sent staff and they will respond to you ASAP.",
    color = 0x47ff69
  )
  submission = discord.Embed(
    title = "New Tactic Suggestion!",
    url = ctx.message.jump_url,
    description = f"By **{ctx.author.display_name}**",
    color = 0xFF6500
  )
  submission.add_field(
    name = "Suggestion",
    value = suggestion.capitalize(),
    inline = False
  )
  submission.add_field(
    name = "User ID",
    value = ctx.author.id,
    inline = False
  )
  submission.set_footer(text = "`accept <user_id>` to accept or `abort <user_id>` to abort")
  
  await channel.send(embed=submission)
  await ctx.reply(embed=embed)

@bot.command()
async def accept(ctx, user_id):
  embed = discord.Embed(
    title = "Good News!",
    description = "Your tactics were approved!",
    color = 0x47ff69
  )
  
  user_id = int(user_id)
  target = bot.get_user(user_id)
  
  await target.send(embed=embed)
  await ctx.send("Done.")
  
@bot.command()
async def abort(ctx, user_id):
  embed = discord.Embed(
    title = "Bad News.",
    description = "Your tactics were declined.",
    color = 0xff4747
  )
  
  user_id = int(user_id)
  target = bot.get_user(user_id)
  
  await target.send(embed=embed)
  await ctx.send("Done.")
  
bot.run(os.environ['DISCORD_TOKEN'])
