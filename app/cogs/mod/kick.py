import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        '''Kicks a member from the server'''
        await member.kick(reason=reason)


def setup(client):
    client.add_cog(Kick(client))
