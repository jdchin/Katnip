import discord
from discord.ext import commands

class Arena(commands.Cog):
    # All Arena commands go here
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Arena(client))
