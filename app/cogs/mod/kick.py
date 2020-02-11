import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, *, reason: str=None) -> None:
        if member is None:
            await ctx.send('Missing `<@user>` argument.')
            return

        await member.kick(reason=reason)


def help():
    return {
        'name': 'Kick',
        'usage': 'kick <@user> [reason]',
        'description': 'Kicks a user from the server'
    }


def setup(client):
    client.add_cog(Kick(client))
