import discord
from discord.ext import commands

class Inventory(commands.Cog):
    # All Inventory commands go here
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Inventory(client))
