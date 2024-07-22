import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)



bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('---------------')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f'Message from  {message.author}: {message.content}')

    if message.content.startswith('Hellow'):
        await message.channel.send('Heey')

    if 'commands' in message.content.lower():
        await mostrar_comandos(message)

    if message.content.lower() == 'creator': 
        await mostrar_creador_info(message)

    await bot.process_commands(message)


async def mostrar_comandos(message):
    embed = discord.Embed(title="Available commands ", color=discord.Color.random())

    for command in bot.commands:
        embed.add_field(name=f"{bot.command_prefix}{command.name}", value=command.help, inline=False)

    await message.channel.send(f"{message.author.mention}, Here is the list of commands: ", embed=embed)

async def mostrar_creador_info(message): 
    
    app_info = await bot.application_info()

    embed = discord.Embed(tittle = "Creator's information",
                          description= f"Information of the account that created this Discord bot",
                          color = discord.color.random())
    
    embed.add_field(name="Application name :", value=app_info.name, inline=False)
    embed.add_field(name="Application ID:", value=app_info.id, inline=False)
    embed.add_field(name="Application Owner:", value=f"{app_info.owner.name}#{app_info.owner.discriminator}", inline=False)

    await message.channel.send(embed=embed)

@bot.command()
async def perfil(ctx):
    """Displays the user's profile. """
    user = ctx.author
    guild = ctx.guild

    embed = discord.Embed(title="User profile", color=discord.Color.random())

    
    embed.add_field(name="User's name:", value=user.name, inline=False)
    embed.add_field(name="Aliases on the server:", value=user.display_name, inline=False)
    embed.add_field(name="Date account created:", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)

  
    if guild:
        member = guild.get_member(user.id)
        if member:
            if member.joined_at:
                embed.add_field(name="Date of joining the server :", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            else:
                embed.add_field(name="Date of joining the server :", value="ERROR", inline=False)
        else:
            embed.add_field(name="Date of joining the server :", value="ERROR", inline=False)

    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    
    guild = member.guild

  
    embed = discord.Embed(title="New member",
                          description=f"¡Welcome {member.mention} to the server!",
                          color=discord.Color.green())
    
    embed.add_field(name="User's name:", value=member.name, inline=False)
    embed.add_field(name="Aliases on the server:", value=member.display_name, inline=False)
    embed.add_field(name="Date account created:", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)

    
    channel = guild.get_channel(1028743688161071104)  
    if channel:
        await channel.send(embed=embed)
    else:
        print(f"ERROR!! Welcome channel not found on server{guild.name}")


TOKEN = 'BOT TOKEN'


bot.run(TOKEN)