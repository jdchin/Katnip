import discord
from discord.ext import commands

class Player(commands.Cog):
    # All Player commands go here
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Player(client))
