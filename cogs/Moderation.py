import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def removeChannel(self, ctx):
        await ctx.channel.delete()
    @commands.command()
    async def stop(self, ctx):
        await ctx.message.channel.send("Survivor Bot shutting down.")
        await self.client.close()

def setup(client):
    client.add_cog(Moderation(client))
