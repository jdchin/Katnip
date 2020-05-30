import discord
from discord.ext import commands

class Item(commands.Cog):
    # All Item commands go here
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Item(client))
