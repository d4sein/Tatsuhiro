import discord
from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number):
        '''Bulk deletes messages from a channel'''
        try:
            number = int(number)
        except TypeError:
            await ctx.send('You must provide an integer number')
            return

        if number <= 0 or number >= 100:
            await ctx.send('You must provide a number between 1-99')
            return

        msgs = []
        async for x in ctx.channel.history(limit=number+1):
            msgs.append(x)
        await ctx.channel.delete_messages(msgs)
        return


def setup(client):
    client.add_cog(Clear(client))
