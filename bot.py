import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Katnip is online!")

# client.load_extension('cogs.Test')
client.remove_command('help')
for cog in os.listdir('./cogs'):
    if cog.endswith('.py'):
        client.load_extension(f'cogs.{cog[:-3]}')


client.run(token)
