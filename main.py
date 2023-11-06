import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

server_embed = None  

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}!')

@bot.command()
async def pserver(ctx, name, password):
    global server_embed

    # Get the role by name (@PrivServerPings)
    role = discord.utils.get(ctx.guild.roles, name='PrivServerPings')

    # Create the embed
    embed = discord.Embed(title='Pung.io Private Server Manager', color=discord.Color.green())
    embed.add_field(name='Name', value=name, inline=False)
    embed.add_field(name='Password', value=password, inline=False)

    if role:
        # Mention the role in the embed field value
        embed.add_field(name='Ping', value=role.mention, inline=False)

    # Add your avatar URL to the embed's thumbnail
    embed.set_thumbnail(url=ctx.author.avatar.url)

    # Send the embed and save it for future reference
    server_embed = await ctx.send(embed=embed)

@bot.command()
async def close(ctx):
    global server_embed

    if server_embed:
        # Create a new embed with the lock image and "This server has been closed"
        embed = discord.Embed(title='Server Closed', description='This server has been closed', color=discord.Color.red())

      #put a url here whenever u find out how to do it >:V
        embed.set_image(url='')  # Add the lock image

        # Add your avatar URL to the embed's thumbnail
        embed.set_thumbnail(url=ctx.author.avatar.url)

        # Edit the previous embed with the new one
        await server_embed.edit(embed=embed)

        # Reset the server_embed variable
        server_embed = None
    else:
        await ctx.send("You need to use .pserver command first.")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from the Discord Developer Portal
bot.run('MTEzMjUxNDYyNzEyMTU5MDM2Mw.GQhdCQ.P5SDxtavUrVUJy4dUljmC8hd8PYRS8LCUxkd9I')